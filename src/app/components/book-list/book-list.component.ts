import { Component, OnInit } from '@angular/core';
import { BookService } from '../../services/book.service';
import { Book } from '../../models/book.model';
import { NgClass, NgForOf, NgIf } from "@angular/common";

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
  user: string = 'Andreas'; // User's name for personalized data storage
  sortCriteria: string = 'likes'; // can be 'likes' or 'title'
  likedBooks: Set<string> = new Set<string>(); // Store liked book IDs in a Set for quick lookup

  constructor(private bookService: BookService) {}

  ngOnInit(): void {
    this.loadLikedBooks();
    this.bookService.getBooks().subscribe((data: Book[]) => {
      this.books = data.map(book => ({
        ...book,
        isLiked: this.likedBooks.has(book.id),
        amountLiked: this.getAmountLiked(book.id)
      }));
      this.sortBooks(); // Sort books after fetching
    });
  }

  likeBook(book: Book) {
    if (this.likedBooks.has(book.id)) {
      this.likedBooks.delete(book.id);
      this.bookService.updateAmountLiked(book.id, this.bookService.getAmountLiked(book.id) - 1);
    } else {
      this.likedBooks.add(book.id);
      this.bookService.updateAmountLiked(book.id, this.bookService.getAmountLiked(book.id) + 1);
    }

    this.saveLikedBooks();
    this.sortBooks(); // Re-sort after liking/unliking a book
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
    this.sortedBooks = this.books.sort((a, b) => {
      let comparison = 0;

      if (this.sortCriteria === 'likes') {
        const likesA = this.bookService.getAmountLiked(a.id);
        const likesB = this.bookService.getAmountLiked(b.id);
        comparison = likesA - likesB;
      } else if (this.sortCriteria === 'title') {
        comparison = a.title.localeCompare(b.title);
      }

      return this.sortOrder === 'asc' ? comparison : -comparison;
    });
  }

  loadLikedBooks() {
    const likedBooksString = localStorage.getItem('likedBooks_' + this.user);
    if (likedBooksString) {
      this.likedBooks = new Set<string>(JSON.parse(likedBooksString));
    } else {
      this.likedBooks = new Set<string>();
    }
  }

  saveLikedBooks() {
    localStorage.setItem('likedBooks_' + this.user, JSON.stringify(Array.from(this.likedBooks)));
  }

  changeUser(event: Event) {
    const selectElement = event.target as HTMLSelectElement;
    if (selectElement) {
      this.user = selectElement.value;
      this.loadLikedBooks();
      this.sortBooks();
    }
  }

  protected getAmountLiked(bookId: string): number {
    return this.bookService.getAmountLiked(bookId);
  }
}
