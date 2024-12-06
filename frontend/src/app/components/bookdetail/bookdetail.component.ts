import {Component, EventEmitter, HostBinding, Input, Output, OnChanges, SimpleChanges} from '@angular/core';
import {BookService} from '../../services/book.service';
import {NgClass, NgForOf, NgIf, NgStyle} from '@angular/common';
import {BookDetail} from "../../models/book.model";

@Component({
  selector: 'app-bookdetail',
  standalone: true,
  imports: [
    NgIf,
    NgClass,
    NgStyle,
    NgForOf
  ],
  templateUrl: './bookdetail.component.html',
  styleUrls: ['./bookdetail.component.css']
})
export class BookdetailComponent implements OnChanges {
  @Input() selectedBook: string | undefined;
  protected subscribedBook: BookDetail | null | undefined;

  @HostBinding('class') cssClass = 'modal fade';

  constructor(private bookService: BookService) {
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['selectedBook'] && changes['selectedBook'].currentValue) {
      // Call BookService whenever selectedBook changes
      this.subscribedBook = undefined
      this.loadBookDetails(changes['selectedBook'].currentValue);
    }
  }


  loadBookDetails(bookId: string): void {
    // Hole Buchdetails vom Service
    this.bookService.getBookDetails(bookId).subscribe({
      next: (bookDetails) => {
        // Handle the book details response
        this.subscribedBook = bookDetails;
      },
      error: (error) => {
        // Handle error, e.g., book not found
        console.error('Fehler beim Laden der Buchdetails:', error);
      }
    });

  }

  getBadgeColor(rating: number | null | undefined): string {
    if (rating === null || rating === undefined) {
      return ''; // Return an empty string if the rating is undefined
    }

    // Normalize the rating to a scale between 0 and 1
    let normalizedRating = (rating - 1) / (5 - 1); // Normalize rating to [0, 1]

    // Calculate the color gradient from red (#ff0000) to green (#00ff00)
    const red = Math.round(255 - normalizedRating * 255);  // From 255 (red) to 0 (green)
    const green = Math.round(normalizedRating * 255);  // From 0 (red) to 255 (green)

    // Return the hex color
    return `#${this.rgbToHex(red, green, 0)}`;
  }

// Helper function to convert RGB values to hex
  private rgbToHex(r: number, g: number, b: number): string {
    return (1 << 24 | r << 16 | g << 8 | b).toString(16).slice(1).toUpperCase();
  }


  // Method to get ranking methods
  getRankingMethods() {
    if (!this.subscribedBook) {
      return [];
    }
    return Object.keys(this.subscribedBook.ranking).map(key => ({
      name: key,
      rank: this.subscribedBook?.ranking[key]
    }));
  }



  ngOnInit(): void {
    // You can also handle initialization logic here
  }
}
