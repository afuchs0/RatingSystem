import {Component, OnInit} from '@angular/core';
import {BookService} from '../../services/book.service';
import {Book} from '../../models/book.model';
import {NgClass, NgForOf, NgIf} from "@angular/common";

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [
    NgIf,
    NgForOf,
    NgClass
  ],
  templateUrl: './book-list.component.html',
  styleUrl: './book-list.component.css'
})
export class BookListComponent implements OnInit {
  books: Book[] = [];
  sortedBooks: Book[] = [];
  sortOrder: string = 'asc'; // can be 'asc' or 'desc'

  userOptions: string[] = ['Andreas', 'Callista', 'Laurent', 'Leo', 'Luca', 'Filippo'];
  user: string = 'Andreas'; // User's name for personalized data storage
  sortOptions: string[] = ['Title', 'Average Rating', 'Similar Authors', 'Similar Content', 'Similar Categories', 'Similar Page-length'];
  sortCriteria: string = this.sortOptions[0];
  ratedBooks: { [user: string]: { [bookId: string]: number } } = {}; // Store ratings for each user

  constructor(private bookService: BookService) {
  }

  ngOnInit(): void {
    this.loadRatedBooks();
    this.bookService.getBooks().subscribe((data: Book[]) => {
      this.books = data.map(book => ({
        ...book,
        userRating: this.ratedBooks[this.user]?.[book.id] || 0 // Set initial rating for current user
      }));
      this.sortBooks(); // Sort books after fetching
    });
  }

  rateBook(book: Book, star: number) {
    if (!this.ratedBooks[this.user]) {
      this.ratedBooks[this.user] = {};
    }

    if (this.ratedBooks[this.user][book.id] === star) {
      delete this.ratedBooks[this.user][book.id]; // Remove rating if the same star is selected again
    } else {
      this.ratedBooks[this.user][book.id] = star; // Set the new rating
    }

    this.saveLikedBooks();
    this.sortBooks(); // Re-sort after rating a book
  }

  getBookRating(book: Book) {
    return this.ratedBooks[this.user]?.[book.id] || 0;
  }

  changeSortCriteria(event: Event) {
    const selectElement = event.target as HTMLSelectElement;
    if (selectElement) {
      this.sortCriteria = selectElement.value;
      this.sortBooks();
    }
  }

  toggleSortOrder() {
    this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
    this.sortBooks();
  }

  sortBooks() {
    if(this.sortCriteria !== this.sortOptions[0] && this.sortCriteria !== this.sortOptions[1]){
      //http get from bookservice to retrieve order from backend. body: {activeUser, ratedBooks, sortCriteria}
      //i dont know how the response looks like, just log it

      this.bookService.getOrderOfBooks(this.user, this.ratedBooks, this.sortCriteria).subscribe({
        next: (response) => {
          console.log(response); //TODO: implement
        },
        error: (error) => {
          console.error(error);
          this.sortCriteria = this.sortOptions[0];
        }
      });
      return
    }

    this.sortedBooks = this.books.sort((a, b) => {
      let comparison = 0;

      if (this.sortCriteria === this.sortOptions[1]) {
        //Rating
        const ratingA = a.rating;
        const ratingB = b.rating;
        comparison = ratingA - ratingB;
      } else if (this.sortCriteria === this.sortOptions[0]) {
        //Title
        comparison = a.title.localeCompare(b.title);
      } else {
        //TODO: implement
      }

      return this.sortOrder === 'asc' ? comparison : -comparison;
    });
  }

  loadRatedBooks() {
    const ratedBooksString = localStorage.getItem('ratedBooks');
    if (ratedBooksString) {
      this.ratedBooks = JSON.parse(ratedBooksString);
    } else {
      this.ratedBooks = {};
    }
  }

  saveLikedBooks() {
    localStorage.setItem('ratedBooks', JSON.stringify(this.ratedBooks));
  }

  changeUser(event: Event) {
    const selectElement = event.target as HTMLSelectElement;

    this.sortCriteria = this.sortOptions[0]; // Reset sort criteria


    if (selectElement) {
      this.user = selectElement.value;
      this.loadRatedBooks();
      this.sortBooks();
    }
  }
}
