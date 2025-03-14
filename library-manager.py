
import json  # Importing JSON module for data storage
import os  # Importing OS module to check file existence

# File where library data will be stored
data_file = "library.txt"

# Function to load library data from the file
def load_library():
    if os.path.exists(data_file):  # Check if file exists
        with open(data_file, "r") as file:
            return json.load(file)  # Load and return JSON data as a Python list
    return []  # Return an empty list if file does not exist

# Function to save library data to the file
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)  # Corrected variable name (was 'lebrary')

# Function to add a new book to the library
def add_book(library):
    book_title = input('Enter the title of the book: ')
    book_author = input('Enter the name of the author: ')
    publishing_year = input('Enter the year of publication: ')
    book_genre = input('Enter the genre of the book: ')
    read = input('Have you read this book before? (yes/no): ').lower() == 'yes'

    # Creating a dictionary to store book details
    new_book = {
        "title": book_title,  # Corrected incorrect dictionary keys
        "author": book_author,
        "year": publishing_year,
        "genre": book_genre,
        "read": read
    }
    
    library.append(new_book)  # Adding book to library list
    save_library(library)  # Save updated library
    print(f"Book '{book_title}' added successfully.")

# Function to remove a book from the library
def remove_book(library):
    title = input("Enter the book title to remove from the library: ").lower()
    initial_length = len(library)
    
    # Filtering out the book to remove
    library = [book for book in library if book['title'].lower() != title]
    
    if len(library) < initial_length:
        save_library(library)  # Save updated library
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"Book '{title}' not found in the library.")

# Function to search for a book
def search_library(library):
    search_by = input("Search by title or author: ").lower()  # Getting search criteria
    search_term = input(f"Enter the {search_by}: ").lower()  # Getting search term

    # Searching in the library based on the search criteria
    results = [book for book in library if search_term in book.get(search_by, '').lower()]
    
    if results:
        for book in results:
            status = "Read" if book['read'] else "Not Read"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No results found for '{search_term}' in the {search_by} field.")

# Function to display all books
def all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Not Read"  # Corrected missing quotes
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("No books found in the library.")

# Function to display library statistics
def display_statistics(library):
    total_books = len(library)  # Total number of books
    read_books = sum(1 for book in library if book['read'])  # Count of read books
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0  # Percentage calculation

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

# Main function to run the library system
def main():
    library = load_library()  # Load library data
    
    while True:
        print ("Welcome to the Library Management System")
        # Display menu options
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)  # Fixed incorrect function call (was search_book)
        elif choice == "4":
            all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Ensuring the script runs the main function when executed\n
if __name__ == "__main__":
    main()
