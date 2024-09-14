// src/app/models/book.model.ts
export interface Book {
  id: string;
  title: string;
  author: string;
  description: string;
  genres: string[];
  coverImg: string;
  amountLiked: number;
  // Add more fields as necessary based on your CSV structure
}
