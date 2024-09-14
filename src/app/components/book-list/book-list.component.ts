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
  sortCriteria: string = 'likes'; // can be 'likes' or 'title'

  constructor(private bookService: BookService) {}

  ngOnInit(): void {
    this.bookService.getBooks().subscribe((data: Book[]) => {
      this.books = data;
      this.sortBooks(); // Sort books after fetching
    });
  }

  likeBook(book: Book) {
    book.isLiked = !book.isLiked;
    book.amountLiked = book.isLiked ? book.amountLiked + 1 : book.amountLiked - 1;
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
        comparison = a.amountLiked - b.amountLiked;
      } else if (this.sortCriteria === 'title') {
        comparison = a.title.localeCompare(b.title);
      }

      return this.sortOrder === 'asc' ? comparison : -comparison;
    });
  }
}
