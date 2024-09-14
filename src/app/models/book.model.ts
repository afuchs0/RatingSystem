// src/app/models/book.model.ts
export interface Book {
  id: number;
  title: string;
  author: string;
  description: string;
  genres: string;
  coverImg: string;
  isLiked: boolean;
  // Add more fields as necessary based on your CSV structure
}
