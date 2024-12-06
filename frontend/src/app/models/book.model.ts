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

export interface BookDetail {
  id: string;
  title: string;
  author: string;
  description: string;
  genres: string[];  // Array of genres
  price: number;
  averageRating: number | null;
  userRating: number | null;
  coverImg: string | null;
  ranking: {  // New property for ranking
    [algorithm: string]: number;  // Key-value pair where algorithm is a string and ranking is a number
  };
}
