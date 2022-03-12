# PROJECT : Library Management System With OOP Concepts
# NAME : Anas Ali Siddiqui

class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} THE BOOKS AVAILABLE ARE: ")
        for book in self.books:
            print(" *--- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE AT THE MOMENT THE BOOK IS TAKEN BY SOMEONE ELSE.\n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED : THANK YOU \n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)


class Student():
    def requestBook(self):
        print("YOU ARE REQUESTED TO BORROW A BOOK !")
        self.book = input("ENTER A BOOK NAME FOR BORROW: ")
        return self.book

    def returnBook(self):
        print("YOU ARE REQUESTED TO RETURN A BOOK !")
        name = input("PLEASE ENTER YOUR NAME: ")
        self.book = input("ENTER A BOOK NAME FOR RETURN: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("Okay! YOU WANT TO DONATE BOOK!")
        self.book = input("ENTER A BOOK NAME FOR DONATE: ")
        return self.book


# MAIN METHOD
if __name__ == "__main__":

    IU_Library = Library(
        ["DESIGN AND ANALYSIS OF ALGORITHMS", "MACHINE LEARNING", "DATA STRUCTURES", "OOP", "ARTIFICIAL INTELLIGENCE", "PYTHON PROGRAMMING"])
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t******** WELCOME TO THE IU LIBRARY ********\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n""")

    while (True):
        # print(track)
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                IU_Library.displayAvailableBooks()
            elif usr_response == 2:  # borrow
                IU_Library.borrowBook(
                    input("PLEASE ENTER YOUR NAME: "), student.requestBook())
            elif usr_response == 3:  # return
                IU_Library.returnBook(student.returnBook())
            elif usr_response == 4:  # donate
                IU_Library.donateBook(student.donateBook())
            elif usr_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} BOOK IS TAKEN/ISSUED BY {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")

            elif usr_response == 6:  # exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:  # catch errors
            print(f"{e}---> INVALID INPUT!,PLEASE ENTER VALID INPUT \n")
