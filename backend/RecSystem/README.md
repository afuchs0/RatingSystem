# Recommendation System API Documentation

This document explains how to use the different recommendation system functionalities implemented in this project. The system provides three main recommendation techniques:

1. **Content-Based Filtering (CBF)**  
2. **Collaborative Filtering (User-Based) (CFU)**  
3. **Collaborative Filtering (Item-Based) (CFI)**  

Below, you’ll find the details for each system, including how to call the functions, their inputs, and outputs.

---

## **1. Content-Based Filtering (CBF)**

- **File:** `cbf.py`
- **Function to Call:** `cbf(user_id=None)`

### **Description**
This method generates recommendations by analyzing the user's preferred genres and comparing them with the genres of books in the dataset. It excludes books the user has already read.

### **Input**
- `user_id` (integer, required): The ID of the user for whom recommendations are being generated.

### **Output**
- A list of 3 recommended book titles based on the user's preferred genres.

### **How to Use**
1. Open the `cbf.py` file.
2. Call the `cbf` function, passing the `user_id` as an argument:
   ```python
   cbf(56)

## **2. Collaborative Filtering (User-Based) (CFU)**
- **File:** `cfu.py`
- **Function to Call:** `cfu(user_id=None)`

### **Description**
This method generates recommendations by analyzing the user's preferred genres and comparing them with the genres of books in the dataset. It excludes books the user has already read.

### **Input**
- `user_id` (integer, required): The ID of the user for whom recommendations are being generated.

### **Output**
- A list of 3 recommended book titles based on the user's preferred genres.

### **How to Use**
1. Open the `cfu.py` file.
2. Call the `cfu` function, passing the `user_id` as an argument:
   ```python
   cfu(56)

3. **Collaborative Filtering (Item-Based) (CFI)**
- **File:** `cfi.py`
- **Function to Call:** `cfi(user_id=None)`

### **Description**
This method generates recommendations by analyzing the user's preferred genres and comparing them with the genres of books in the dataset. It excludes books the user has already read.

### **Input**
- `user_id` (integer, required): The ID of the user for whom recommendations are being generated.

### **Output**
- A list of 3 recommended book titles based on the user's preferred genres.

### **How to Use**
1. Open the `cfi.py` file.
2. Call the `cfi` function, passing the `user_id` as an argument:
   ```python
   cfi(56)
