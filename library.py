allBooks = [
    ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
    ['9780134494166', "The Human Body", "Dave R", 1, []],
    ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
]

borrowedISBNs = []
# This is the first function that prints and displays the menu for the user
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')
    return

# This is the second function that allows users to add books
def addBook():
    bookName = input("Book name> ")
    while '*' in bookName:
        print('Invalid book name!')
        bookName = input("Book name> ")
    while '%' in bookName:
        print('Error')
        bookName = input("Book name> ")
    authorName = input("Enter author name: ")
    edition = int(input("Enter edition number: "))
    # Make sure user enters interger value here, if not show error message and repeatedly ask for a valid input^

    internationalStandardBookNumber = input("Enter the international standard book number (unique 13 digits number): ")
    while not internationalStandardBookNumber.isdigit() or len(internationalStandardBookNumber) != 13:
        internationalStandardBookNumber = input("Enter the international standard book number (unique 13 digits number): ")

    evenValidISBN = (int(internationalStandardBookNumber[0]) + int(internationalStandardBookNumber[2]) + int(
        internationalStandardBookNumber[4])
                     + int(internationalStandardBookNumber[6]) + int(internationalStandardBookNumber[8]) +
                     int(internationalStandardBookNumber[10]) + int(internationalStandardBookNumber[12]))
    oddValidISBN = ((int(internationalStandardBookNumber[1]) * 3) + (int(internationalStandardBookNumber[3]) * 3) +
                    (int(internationalStandardBookNumber[5]) * 3) + (int(internationalStandardBookNumber[7]) * 3) +
                    (int(internationalStandardBookNumber[9]) * 3) + int(internationalStandardBookNumber[11]) * 3)
    trulyValidISBN = (evenValidISBN + oddValidISBN)
#this part checks if the international standard book number is valid, a valid ISBN is an ISBN that follows this formula... 
#((all (even integer values x 1) + all(odd integer values x 3))/10)
# ex (([0]x1)+([1]x3)+[2]x1)+([3]x3)....+[12]x1)+([13]x3))
# if the sum of this value is divisable by 10 the ISBN is valid
# Valid ISBNs include...
# '9780132350884'
# '9780321125217'
# '9780596007126'
# '9780134494166'
# '9780321344755'
# etc
    
    if int(trulyValidISBN) % 10 == 0:
        for i in allBooks:
            if internationalStandardBookNumber in i:
                print('ISBN already valid')
                return
            allBooks.append([internationalStandardBookNumber, bookName, authorName, edition, []])
            print('Book added successfully!')
            print(allBooks)
            print(borrowedISBNs)
            return
            
#This is the function that helps allow the user to borrow a book
def borrowBook():
    borrowerName = input("Enter the borrower name> ")
    borrowingBook = input('Search term> ')
    matchFound = False

    # Finds book if it doesn't have a suffix
    for book in allBooks:
        if borrowingBook.lower() in book[1].lower():
            print(book[1])
            print('Book borrowed!')
            book[-1].append(borrowerName)
            matchFound = True
            borrowedISBNs.append([book[0]])

    # Matches with book(s) if the borrowing statment ends with *
    if '*' in borrowingBook[-1]:
        borrowingBook = borrowingBook[:-1]
        for book in allBooks:
            if borrowingBook.lower() in book[1].lower():
                print(book[1])
                print('Book borrowed!')
                book[-1].append([borrowerName])
                matchFound = True
                borrowedISBNs.append([book[0]])

    # Matches with the book(s) with the first word if the borrowing statement ends with %
    if '%' in borrowingBook[-1]:
        borrowingBook = borrowingBook[:-1]
        borrowedBookFirstWord = borrowingBook.split()[0]
        for book in allBooks:
            if borrowedBookFirstWord.lower() == book[1].split()[0].lower():
                print(book[1])
                print('Book borrowed!')
                book[-1].append(borrowerName)
                matchFound = True
                borrowedISBNs.append([book[0]])
                
    # if no matches are found this output will let the user know
    if not matchFound:
        print('No book found!')

    print(borrowedISBNs)
    return

    #return book function to allow the user to return a certain book
def returnBook():
    returnedISBN = input("ISBN> ")

    if [returnedISBN] in borrowedISBNs:
        borrowedISBNs.remove([returnedISBN])
        for book in allBooks:
            if returnedISBN in book[0]:
                print(f'"{book[1]}", has been returned')
            else:
                print('No book found!')
    return
def listBooks():
    for book in allBooks:
        if book[0] in [isbn[0] for isbn in borrowedISBNs]:
            print('---------------')
            print('Unavailable')
            print(book[1], '-', book[2])
            print('E:', book[3], 'ISBN:', book[0])
            print('Borrowed by:', book[4])
        else:
            print('---------------')
            print('Available')
            print(book[1], '-', book[2])
            print('E:', book[3], 'ISBN:', book[0])
            print('Borrowed by:', book[4])
def exit():
    print('$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$')

def start():
    while True:
        printMenu()
        userInput = (input("Your selection> "))
        if userInput.lower() == ('x') or userInput == "5":
            exit()
            listBooks()
            break
        elif userInput.lower() not in ('1', '2', '3', '4', '5', 'a', 'r', 't', 'l', 'x'):
            print('Wrong Selection!')
        elif userInput.lower() == ('a') or userInput == "1":
            addBook()
        elif userInput.lower() == ('r') or userInput == "2":
            borrowBook()
        elif userInput.lower() == ('t') or userInput == "3":
            returnBook()
        elif userInput.lower() == ('l') or userInput == "4":
            listBooks()


start()
