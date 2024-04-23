library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
no_dupes = True

def add_new_book():
    return

print("Welcome to the book adder program. \nPlease answer the following questions about the book to be added.")

while True:
    year_entry = input("What is the book's title? ")
    author_entry = input("Who wrote the book? ")
    new_book_tuple = (year_entry, author_entry)

    for book in range(0, len(library)):
        if new_book_tuple == library[book]:
            print("You can't enter a duplicate book.")
            no_dupes = False
            break
        else:
            pass
    if no_dupes == True:
        library.append(new_book_tuple)
        print("Books in list: ", library)
    
    no_dupes = True
    end_choice = input("Would you like to enter another book? Y or N. ").upper()
    if end_choice == 'N':
        break
