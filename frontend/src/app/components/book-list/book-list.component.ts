import {Component, OnInit} from '@angular/core';
import {BookService} from '../../services/book.service';
import {BookListItem} from '../../models/book.model';
import {User} from '../../models/user.model'; // Importiere das User-Interface
import {NgClass, NgForOf, NgIf} from "@angular/common";
import {first} from "rxjs";
import {BookdetailComponent} from "../bookdetail/bookdetail.component";

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [
    NgIf,
    NgForOf,
    NgClass,
    BookdetailComponent
  ],
  templateUrl: './book-list.component.html',
  styleUrl: './book-list.component.css'
})
export class BookListComponent implements OnInit {
  books: BookListItem[] = [];
  sortOrder: string = 'asc'; // can be 'asc' or 'desc'

  userOptions: User[] = [];
  userSelected: string = '';
  sortOptions: string[] = ['Content Based Filtering', 'Collaborative Filtering Userbased','Collaborative Filtering Itembased','Q-Learning','DQN'];
  sortCriteria: string = this.sortOptions[0];

  selectedBook: string | undefined;


  constructor(private bookService: BookService) {
  }

  ngOnInit(): void {
    this.loadUsersAndBooks();
  }

  rateBook(book: BookListItem, starClicked: number) {
    // Reset the rating if the clicked star matches the current userRating
    const ratingToUpdate = book.userRating === starClicked ? null : starClicked;

    // Call the service to update the rating
    this.bookService.updateUserRating(this.userSelected, book.id, ratingToUpdate).subscribe({
      next: (updatedBook) => {
        // Update the local book object with the response from the backend
        book.userRating = updatedBook.userRating;
      },
      error: (err) => {
        console.error('Failed to update rating', err);
      },
    });
  }


  toggleSortOrder() {
    this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
  }

  changeSortCriteria(event: Event) {
    const selectElement = event.target as HTMLSelectElement;

    if (selectElement) {
      if (this.sortCriteria !== selectElement.value) {
        this.sortCriteria = selectElement.value;
        this.loadBooks();
      }
    }
  }

  changeUser(event: Event) {
    const selectElement = event.target as HTMLSelectElement;

    if (selectElement) {
      if (this.userSelected !== selectElement.value) {
        this.userSelected = selectElement.value;
        this.loadBooks();
      }
    }
  }

  loadBooks() {
    this.bookService.getBooks(this.userSelected, this.sortCriteria).subscribe((data: BookListItem[]) => {
      this.books = data.map(book => ({
        ...book
      }));
    });
  }

  private loadUsersAndBooks() {
    this.bookService.getUsers().subscribe({
      next: (users: User[]) => {
        this.userOptions = users;

        if (users.length > 0) {
          this.userSelected = users[0].id; // Set default user
          this.loadBooks();
        }
      },
      error: (err) => {
        console.error('Fehler beim Laden der Benutzer', err);
      }
    });
  }

  getDisplayedBooks(): any[] {
    return this.sortOrder === 'asc'
      ? this.books
      : [...this.books].reverse(); // Copy of reverse list
  }

  // Open modal and pass the selected book data
  openBookDetails(book: BookListItem): void {
    console.log(book.id)
    this.selectedBook = book.id;
  }
}
