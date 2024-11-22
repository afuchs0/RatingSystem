import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {map} from 'rxjs/operators';
import {BookListItem} from '../models/book.model';
import {HttpClient} from '@angular/common/http';
import {User} from "../models/user.model";

@Injectable({
  providedIn: 'root',
})
export class BookService {
  private apiUrl = 'http://127.0.0.1:5000/api/'; // Base API URL

  constructor(private http: HttpClient) {
  }

  getBooks(userId: string, sortCriteria: string): Observable<BookListItem[]> {
    const params = { userId, sortCriteria }; // Query parameters
    const url = this.apiUrl + 'getBookList'; // Construct URL

    // Make HTTP GET request
    return this.http.get<{ books: any[], sortCriteria: string }>(url, { params }).pipe(
      map((response) => {
        // Map API response to the BookListItem array
        return response.books.map((item: any) => ({
          id: item.id,
          title: item.title,
          author: item.author,
          genres: item.genres, // Assume genres is already an array
          userRating: item.userRating, // Directly use userRating from response
          averageRating: item.averageRating, // Use averageRating from response
        }));
      })
    );
  }


  // New method to update user rating
  updateUserRating(userId: string, bookId: string, userRating: number | null): Observable<any> {
    const url = this.apiUrl + 'updateUserRating'; // Endpoint URL
    const body = { userId, bookId, userRating }; // Request payload

    // Make HTTP PUT request
    return this.http.put(url, body);
  }

  getUsers(): Observable<User[]> {
    const url = this.apiUrl + 'getUserList'; // Endpoint URL
    return this.http.get<{ id: string; generi_preferiti: string; age: string }[]>(url).pipe(
      map((users) =>
        users.map((user) => {
          const genres = JSON.parse(user.generi_preferiti.replace(/'/g, '"')).join(', '); // Parse and join genres
          return {
            id: user.id,
            name: `Age: ${user.age} | Prefers: ${genres}`,
          };
        })
      )
    );
  }
}
