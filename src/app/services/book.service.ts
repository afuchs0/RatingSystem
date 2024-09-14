import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import * as Papa from 'papaparse';
import { Book } from '../models/book.model';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class BookService {
  private amountLikedMap: Map<string, number> | undefined;

  constructor(private http: HttpClient) {
    this.loadAmountLikedFromLocalStorage();
  }

  private loadAmountLikedFromLocalStorage(): void {
    const storedMap = localStorage.getItem('amountLikedMap');
    if (storedMap) {
      this.amountLikedMap = new Map<string, number>(JSON.parse(storedMap));
    } else {
      this.amountLikedMap = new Map<string, number>();
    }
  }

  private saveAmountLikedToLocalStorage(): void {
    // @ts-ignore
    localStorage.setItem('amountLikedMap', JSON.stringify(Array.from(this.amountLikedMap.entries())));
  }

  private getRandomNumber(): number {
    return Math.floor(Math.random() * 101); // Generates a random number between 0 and 100
  }

  getBooks(): Observable<Book[]> {
    return this.http.get('assets/books.csv', { responseType: 'text' }).pipe(
      map((data) => {
        const books: Book[] = [];
        Papa.parse(data, {
          header: true,
          skipEmptyLines: true,
          complete: (result) => {
            result.data.forEach((item: any) => {
              const id = item['bookId'];

              if (!this.getAmountLiked(id)){
                const randomAmountLiked = this.getRandomNumber();
                this.updateAmountLiked(id, randomAmountLiked); // Update the map with the random number

              } // Generate a random number
              books.push({
                id: id,
                title: item['title'],
                author: item['author'],
                description: item['description'],
                genres: item['genres']
                  .replace(/[\[\]']/g, '') // Remove square brackets and single quotes
                  .split(',')
                  .map((genre: string) => genre.trim()), // Split and trim each genre
                coverImg: item['coverImg'],
                // Removed amountLiked from Book
              });
            });
          },
        });
        return books;
      })
    );
  }

  updateAmountLiked(bookId: string, amount: number): void {
    // @ts-ignore
    this.amountLikedMap.set(bookId, amount);
    this.saveAmountLikedToLocalStorage();
  }

  getAmountLiked(bookId: string): number {
    // @ts-ignore
    return this.amountLikedMap.get(bookId) || 0; // Return 0 if not found
  }
}
