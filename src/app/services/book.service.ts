import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import * as Papa from 'papaparse';
import { Book } from '../models/book.model';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root',
})
export class BookService {
  constructor(private http: HttpClient) {}

  getBooks(): Observable<Book[]> {
    return this.http.get('assets/books.csv', { responseType: 'text' }).pipe(
      map((data) => {
        const books: Book[] = [];
        Papa.parse(data, {
          header: true,
          skipEmptyLines: true,
          complete: (result) => {
            result.data.forEach((item: any) => {
              books.push({
                id: +item['bookId'],
                title: item['title'],
                author: item['author'],
                description: item['description'],
                genres: item['genres'],
                coverImg: item['coverImg'],
                isLiked: false
                // Map other fields as necessary
              });
            });
          },
        });
        return books;
      })
    );
  }
}
