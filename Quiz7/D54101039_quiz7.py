library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here
    #輸入要加入的內容，用"|"分開，再依照形式存入library
    a=input("\nEnter the title, genre, and price of the book (separated by |): ")
    a=a.split("|")
    library[a[0]]=(a[1],float(a[2]))
    print("\nAdded",a[0],"to the library.")
    return library

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here
    #輸入要刪除的標題，如果library裡面有此內容就刪除，沒有的話就印出error
    a=input("Enter the title of the book to remove: ")
    if a in library:
        del library[a]
        print("\nRemove",a,"from the library.")
        return library
    else:
        print("\nError：",a,"not found in the library.\n")


def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    #輸入要查詢的標題，如果library裡面有此內容就印出內容，沒有的話就印出error
    a=input("Enter the title of the book: ")
    if a in library:
        print("\nTitle:",a)
        print("Genre:",library[a][0])
        print("Price:",library[a][1],"\n")
    else:
        print("\nError:",a,"not found in the library.\n")

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here
    #輸入要查詢的genre，如果library裡面有此內容就印出內容，沒有的話就印出error
    a=input("Enter the genre to search for: ")
    i=0
    print("")
    for title, (genre, price) in sorted(library.items()):
        if library[title][0]==a:
            print("%s (%s, $%.2f)" % (title, genre, price))
            i+=1
    if i==0:
        print("No books found in the",a,"genre.")
    print("")

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

