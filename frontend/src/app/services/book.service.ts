import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {map} from 'rxjs/operators';
import * as Papa from 'papaparse';
import {Book} from '../models/book.model';
import {HttpClient} from '@angular/common/http';
import * as http from "node:http";

@Injectable({
  providedIn: 'root',
})
export class BookService {

  constructor(private http: HttpClient) {
  }

  getBooks(): Observable<Book[]> {
    return this.http.get('assets/books.csv', {responseType: 'text'}).pipe(
      map((data) => {
        const books: Book[] = [];
        Papa.parse(data, {
          header: true,
          skipEmptyLines: true,
          complete: (result) => {
            result.data.forEach((item: any) => {
              books.push({
                id: item['bookId'],
                title: item['title'],
                author: item['author'],
                description: item['description'],
                genres: item['genres']
                  .replace(/[\[\]']/g, '') // Remove square brackets and single quotes
                  .split(',')
                  .map((genre: string) => genre.trim()), // Split and trim each genre
                coverImg: item['coverImg'],
                rating: +item['rating'],
              });
            });
          },
        });
        return books;
      })
    );
  }

  getOrderOfBooks(user: string, ratedBooks: { [p: string]: { [p: string]: number } }, sortCriteria: string) {
    //get order from backend
    return this.http.post('http://localhost:8080/getOrder', {
        currentUser: user,
        ratedBooks: ratedBooks,
        sortCriteria: sortCriteria
      }
    );
  }
}
