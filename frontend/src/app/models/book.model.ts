// src/app/models/book.model.ts
export interface BookListItem {
  id: string;
  title: string;
  author: string;
  genres: string[];
  averageRating: number;
  userRating: number;
  // Add more fields as necessary based on your CSV structure
}
