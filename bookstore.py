'''
Link to view python file in command line:

python bookstore.py

user_data = {idx: ele for idx, ele in enumerate(user_string.split(';'))}

        user_string = f"\n{new_username};{new_password};{first_name};{last_name}"
        user_data = str(user_string)
'''
       
#=============Importing Libraries==========



#===============Defining Classes===========

class Book:

    def __init__(self, book_name, author, isbn, year_published, overview, price, itinerary):
        
        self.book_name = book_name
        self.author = author
        self.isbn = isbn
        self.year_published = year_published
        self.overview = overview
        self.price = price
        self.itinerary = itinerary
        
    def __str__(self):
        return f"Book:\t\t{self.book_name}\n\
Author:\t\t{self.author}\n\
ISBN:\t\t{self.isbn}\n\
Year Published:\t{self.year_published}\n\
Overview:\t{self.overview}\n\
Price:\t\t{price}\n\
itinerary:\t{itinerary}\n"
        
        
b01 = Book("Harry Potter and the Sorcerer's Stone","J.K. Rowling","978-0590353427","1997","Follow Harry Potter, an orphaned boy who discovers he is a wizard, as he begins his magical education at Hogwarts School of Witchcraft and Wizardry.","7.99","6")
b02 = Book("Matilda","Roald Dahl","978-0142410370","1988","Matilda is a brilliant girl with telekinetic powers who uses her abilities to stand up against her neglectful parents and the tyrannical school headmistress, Miss Trunchbull.","8.99","5")
b03 = Book("Charlotte's Web","E.B. White","978-0061124952","1952","This timeless classic tells the story of the unlikely friendship between a pig named Wilbur and a clever spider named Charlotte, who saves Wilbur from being slaughtered.","2.99","4")
b04 = Book("The Lion, the Witch, and the Wardrobe","C.S. Lewis","978-0064471046","1950","Four siblings stumble upon the magical land of Narnia through a wardrobe and find themselves caught in an epic battle between good and evil.","5.99","4")
b05 = Book("The Tale of Peter Rabbit","Beatrix Potter","978-0723247708","1902","Join Peter Rabbit as he disobeys his mother's warnings and sneaks into Mr. McGregor's garden, facing various adventures and mishaps.","6.99","7")
b06 = Book("Winnie-the-Pooh","A.A. Milne","978-0525444435","1926","Enter the Hundred Acre Wood and join Winnie-the-Pooh, Piglet, Eeyore, and friends on their whimsical adventures filled with friendship and discovery.","5.99","3")
b07 = Book("Alice's Adventures in Wonderland","Lewis Carroll","978-1503210566","1865","Follow Alice as she falls down a rabbit hole into a fantastical world filled with peculiar characters and nonsensical adventures.","6.99","1")
b08 = Book("Charlie and the Chocolate Factory","Roald Dahl","978-0142410318","1964","Join Charlie Bucket as he wins a golden ticket to tour Willy Wonka's chocolate factory, where he encounters magical wonders and mischievous children.","6.99","4")
b09 = Book("The Hobbit","J.R.R. Tolkien","978-0547928227","1937","Bilbo Baggins, a hobbit, embarks on an unexpected journey to reclaim the lost Dwarf Kingdom of Erebor, encountering trolls, elves, and a fearsome dragon named Smaug.","5.99","3")
b10 = Book("Where the Wild Things Are","Maurice Sendak","978-0064431781","1963","Max, a mischievous boy, sails to an island inhabited by wild creatures where he becomes their king, but soon realizes that he misses the comfort of home.","7.99","4")
b11 = Book("The Secret Garden","Frances Hodgson Burnett","978-0143106457","1911","Orphaned Mary Lennox discovers a hidden garden on her uncle's estate, and with the help of a robin and her cousin Colin, she brings the garden back to life while finding healing and friendship.","5.99","7")
b12 = Book("Pippi Longstocking","Astrid Lindgren","978-0142402498","1945","Pippi Longstocking is a free-spirited and unconventional girl with superhuman strength who lives without parents and embarks on whimsical adventures with her friends Tommy and Annika.","7.99","5")
b13 = Book("The Wind in the Willows","Kenneth Grahame","978-0141321134","1908","Join the adventures of Mole, Rat, Badger, and Toad as they navigate the idyllic countryside of Edwardian England in this timeless classic of friendship and camaraderie.","4.99","8")
b14 = Book("The Adventures of Tom Sawyer","Mark Twain","978-0143039563","1876","Follow Tom Sawyer and his friend Huckleberry Finn as they embark on adventures along the Mississippi River, encountering treasure hunts, pirates, and other escapades.","8.99","6")
b15 = Book("Bridge to Terabithia","Katherine Paterson","978-0064401845","1977","Jess and Leslie create an imaginary kingdom in the woods called Terabithia, where they reign as king and queen, forging a deep friendship that helps them cope with the challenges of growing up.","6.99","5")
b16 = Book("The BFG (Big Friendly Giant)","Roald Dahl","978-0142410387","1982","Sophie befriends the Big Friendly Giant, who takes her on a journey to Giant Country where they must stop other giants from eating children by enlisting the help of the Queen of England.","8.99","2")
b17 = Book("The Phantom Tollbooth","Norton Juster","978-0394820378","1961","Milo embarks on a fantastical journey through the Kingdom of Wisdom, where he learns about the importance of curiosity, imagination, and learning.","6.99","4")
b18 = Book("The Tale of Despereaux","Kate DiCamillo","978-0763680893","2003","Despereaux, a brave mouse with unusually large ears, embarks on a quest to rescue a princess and save the kingdom from darkness, proving that even the smallest creature can be a hero.","7.99","7")
b19 = Book("A Wrinkle in Time","Madeleine L'Engle","978-0312367541","1962","Meg Murry, her brother Charles Wallace, and their friend Calvin O'Keefe embark on a journey through space and time to rescue Meg's father from the clutches of evil forces.","5.99","4")
b20 = Book("Little House on the Prairie","Laura Ingalls Wilder","978-0064400022","1935","Join the Ingalls family as they leave their home in the Big Woods of Wisconsin and settle in the vast prairies of the American Midwest, facing challenges and joys along the way.","8.99","6")
b21 = Book("The Indian in the Cupboard","Lynne Reid Banks","978-0375847530","1980","When Omri receives an old cupboard for his birthday, he discovers that it has the power to bring plastic toys to life, including a miniature Native American named Little Bear.","4.99","6")
b22 = Book("The Velveteen Rabbit","Margery Williams","978-0385077255","1922","A stuffed rabbit longs to become real through the love of his owner, a young boy, and learns about the transformative power of love and the nature of being truly alive.","2.99","8")
b23 = Book("James and the Giant Peach","Roald Dahl","978-0142410363","1961","James, an orphaned boy, escapes from his cruel aunts by entering a magical giant peach, embarking on a journey with insect friends to New York City.","6.99","8")
b24 = Book("Anne of Green Gables","L.M. Montgomery","978-0147514004","1908","Anne Shirley, an imaginative and spirited orphan, is adopted by siblings Marilla and Matthew Cuthbert, leading to delightful adventures and mishaps in the town of Avonlea.","7.99","5")
b25 = Book("The Boxcar Children","Gertrude Chandler Warner","978-0807508527","1924","Follow the adventures of the Alden siblings—Henry, Jessie, Violet, and Benny—as they make a home in an abandoned boxcar and solve mysteries in their small town.","4.99","7")
b26 = Book("The Wonderful Wizard of Oz","L. Frank Baum","978-0143106631","1900","Dorothy, a Kansas farm girl, is swept away to the magical land of Oz, where she embarks on a journey to meet the Wizard and find her way back home, encountering friends and foes along the way.","3.99","7")
b27 = Book("The Giving Tree","Shel Silverstein","978-0060256654","1964","A touching story about the enduring friendship between a boy and a tree who gives everything she has to make him happy, illustrating the beauty of selfless love and sacrifice.","7.99","8")
b28 = Book("The Cat in the Hat","Dr. Seuss","978-0394800011","1957","The mischievous Cat in the Hat visits two children on a rainy day, turning their house upside down with his playful antics and introducing them to a world of imagination and fun.","9.99","8")
b29 = Book("Stuart Little","E.B. White","978-0064400565","1945","Stuart Little, a small mouse born to a human family in New York City, embarks on a series of adventures to find his friend Margalo the bird and discover where he truly belongs.","4,99","7")
b30 = Book("The Little Prince","Antoine de Saint-Exupéry","978-0156012195","1943","A philosophical tale about a young prince who travels from planet to planet, encountering various characters and learning important lessons about love, friendship, and the meaning of life.","6.99","7")

books_dict = {}

books_dict[b01.book_name] = b01
books_dict[b02.book_name] = b02
books_dict[b03.book_name] = b03
books_dict[b04.book_name] = b04
books_dict[b05.book_name] = b05
books_dict[b06.book_name] = b06
books_dict[b07.book_name] = b07
books_dict[b08.book_name] = b08
books_dict[b09.book_name] = b09
books_dict[b10.book_name] = b10
books_dict[b11.book_name] = b11
books_dict[b12.book_name] = b12
books_dict[b13.book_name] = b13
books_dict[b14.book_name] = b14
books_dict[b15.book_name] = b15
books_dict[b16.book_name] = b16
books_dict[b17.book_name] = b17
books_dict[b18.book_name] = b18
books_dict[b19.book_name] = b19
books_dict[b20.book_name] = b20
books_dict[b21.book_name] = b21
books_dict[b22.book_name] = b22
books_dict[b23.book_name] = b23
books_dict[b24.book_name] = b24
books_dict[b25.book_name] = b25
books_dict[b26.book_name] = b26
books_dict[b27.book_name] = b27
books_dict[b28.book_name] = b28
books_dict[b29.book_name] = b29
books_dict[b30.book_name] = b30


with open('book_stocklist.txt', 'w+') as file:
    for book_name, book in books_dict.items():
        file.write(f"{book.book_name};")
        file.write(f"{book.author};")
        file.write(f"{book.isbn};")
        file.write(f"{book.year_published};")
        file.write(f"{book.overview};")
        file.write(f"{book.price};")
        file.write(f"{book.itinerary};\n")


# Read data in book_stocklist.txt file, and split lines into lists,
# saving the 2D list as book_data.
with open("book_stocklist.txt", 'r') as book_file:
    book_data = book_file.read().split("\n")

#=============Defining Functions===========


def printline(symbol='-', num=79):
    '''
    Creates a line in the code, 79 characters long to break up the code.
    '''
    print(symbol * num)


def print_heading(title):
    '''
    Print title in the middle of the code.
    '''
    print((' '*(40-(len(title)//2))), title)
    

def reg_user():
    '''
    Register a new user and password to the user.txt file.
    '''
    printline()
    print_heading("Register a New User")
    printline()

    while True:
        # Opens the file for storing usernames, creates one if one doesn't yet exist.
        with open("user.txt", 'r+') as file_obj:
            # Request input of a new username.
            new_username = input("New Username: ")
            user_exists_check = file_obj.read()
        # Adds the new username to file, if it does not yet exist.    
        if new_username not in user_exists_check:
            break
        else:
            # Error handling, so no 2 usernames are the same.
            print("ERROR: Username already in use, please re-enter:")
            return False
    
    # Request user to input a new password.
    new_password = input("New Password: ")

    # Request user to input password agin to confirm.
    confirm_password = input("Confirm Password: ")

    # Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # If they are the same, ask for first anme and last name,
        # and add them to the user.txt file.
        
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")

        with open("user.txt", "a") as reg_file:
            user_string = f"{new_username};{new_password};{first_name};{last_name};\n"
            reg_file.write(user_string)
            user_data = user_string.split(";")
            user_list = []
            user_list.append(user_data)

            
            print("New user added.")
    # Otherwise passwords dont match, and returns to main menu.
    else:
        print("ERROR: Passwords do no match")

    
    
def search_book_name():

    printline()
    print_heading("Search a Book Name")
    printline()
    with open("book_stocklist.txt", 'r+') as file_obj:
        # Request input of a book name to search.
        book_name = input("Enter a book name: ")
        book_name_check = file_obj.read()
        if book_name in book_name_check:
            print(f"Yes, we stock {book_name}.")
        else:
            print(f"No, we do not stock {book_name}.")


def search_book_author():

    printline()
    print_heading("Search a Book Author")
    printline()   
    with open("book_stocklist.txt", 'r+') as file_obj:
    # Request input of an author to search.
        book_author = input("Enter an author: ")
        book_author_check = file_obj.read()
        if book_author in book_author_check:
            print(f"Yes, we stock {book_author}.")
        else:
            print(f"No, we do not stock {book_author}.")


def search_isbn():
    
    printline()
    print_heading("Search a Book ISBN")
    printline()
    with open("book_stocklist.txt", 'r+') as file_obj:
    # Request input of an ISBN to search.
        book_isbn = input("Enter an ISBN: ")
        book_isbn_check = file_obj.read()
        if book_isbn in book_isbn_check:
            print(f"Yes, we stock {book_isbn}.")
        else:
            print(f"No, we do not stock {book_isbn}.")

    
def list_books():
    
    printline()
    print_heading("List All Books")
    printline()
    # Print all books in bookstore.
    for books in books_dict.keys():
        print(books)


def read_book_info():
    '''
    Reads all of the book information stored in the book_stocklist.txt file
    and prints to the console in a readable format. 
    '''
    printline()
    print_heading("All Book Information")
    printline()

    with open("book_stocklist.txt", 'r+') as file_obj:
        for books in file_obj.readlines():
            print(books)
    
    
def add_book():
    
    printline()
    print_heading("Add Book to Shopping Basket")
    printline()
    with open("shopping_basket.txt", 'a') as basket:
        book_to_basket = input("Enter the Book Name you would like to add to basket: ")
        if book_to_basket in books_dict.keys():
            basket.write(user_basket)
        else:
            print("ERROR: Please enter a book we stock.")


def modify_basket():
    
    printline()
    print_heading("Modify Shopping Basket")
    printline()
    pass
    
    
def checkout():
    
    printline()
    print_heading("Checkout")
    printline()    
    pass
    
    
def order_his():
    
    printline()
    print_heading("Account Order History")
    printline()
    pass
    
    
def view_acc_info():

    printline()
    print_heading("View Account Information")
    printline()
    with open("user.txt", 'r+') as file_obj:
        for acc_info in file_obj.readlines():
            print(acc_info)
    
    
def modify_acc_info():
    
    printline()
    print_heading("Modify Account Information")
    printline()
    with open("user.txt", 'r+') as file_obj:
        '''user_data = file_obj.read().split("\n")
        total_users = len(user_data)
        print(total_users)'''
        user_list = []
        for i in file_obj:
            user_data = i.split(";")
            user_list.append(user_data)
        for index, value in enumerate(user_list, start=1):
            print(f"ID no.: {index} = Account Details: {value}")
            printline()
            print("1 - Username\n\
2 - Password\n\
3 - First Name\n\
4 - Last Name")
            printline()
            id_modify = input("Enter which user ID no. you would like to modify: ")
            id_modify = int(id_modify)
            data_modify = input("Enter which account detail (1-4) would you like to modify: ")
            data_modify = int(data_modify)
            data_modify = data_modify - 1
            updated_data = input("Enter what you would like to modify this to: ")
            updated_data = str(updated_data)
            
            if id_modify == 0:
                user_list[id_modify][0] = updated_data

            elif id_modify == 1:
                user_list[id_modify][1] = updated_data

            elif id_modify == 2:
                user_list[id_modify][2] = updated_data

            elif id_modify == 3:
                user_list[id_modify][3] = updated_data

            else:
                print("ERROR: Enter a number between 1-4.")


#============End of Functions===========

#===========Start of Main Code==========


# Create user.txt if it doesn't exist.
with open("user.txt", "a") as default_file:
    pass

# Create shopping_basket.txt if it doesn't exist.
with open("shopping_basket.txt", "a") as default_file:
    pass

# Read data in user.txt file, and split lines into lists,
# saving the 2D list as user_data.
#with open("user.txt", 'r') as user_file:
    #user_data = user_file.read().split("\n")
    
# Read data in shopping_basket.txt file, and split lines into lists,
# saving the 2D list as user_basket.
#with open("shopping_basket.txt", 'r') as basket_file:
    #user_basket = basket_file.read().split("\n")
    

# Welcome message.
printline()
print_heading("Welcome to Steph's Bookstore!!")
printline()
            
#print(user_data)
#print(user_basket)

# Registration status.
reg_status = input("Are you already registered?\n\
Enter 'y' to login or 'n' to continue to other options: ")

reg_status = reg_status.lower()

if reg_status == 'y':
    '''
    Login Section: 
    This code reads usernames and passwords from the user.txt file to
    allow a user to login.
    '''
    logged_in = False
    while not logged_in:
        printline()
        print_heading("Login")
        printline()
        print()
        with open("user.txt", 'r+') as file_obj:
        # Request input of an username and password to search.     
            curr_user = input("Username: ")
            curr_pass = input("Password: ")
            print()
            user_details = file_obj.read()
            if curr_user not in user_details:
                print("User does not exist")
                continue
            elif curr_pass not in user_details:
                print("Wrong password")
                continue
            else:
                print("Login Successful!\n")
                logged_in = True

    # Logged in user's Main menu.
    print("Search Options:\n\
1 - search for books using the book name\n\
2 - search for books using the name of author\n\
3 - search for books using ISBN of the book\n\n\
Information Options:\n\
4 - view list of all books in the application\n\
5 - view all book information in a readable format\n\n\
Purchase Options:\n\
6 - add a book to shopping list\n\
7 - modify the shopping basket\n\
8 - choose to proceed and checkout\n\n\
Account Options:\n\
9 - access order history\n\
10 - view account details\n\
11 - modify account details\n\
12 - logout / exit")

    user_choice = input("Enter the number (between 1-12) as your select choice: ")

    if user_choice == '1':
        search_book_name()
        
    elif user_choice == '2':
        search_book_author()

    elif user_choice == '3':
        search_isbn()

    elif user_choice == '4':
        list_books()

    elif user_choice == '5':
        read_book_info()

    elif user_choice == '6':
        add_book()

    elif user_choice == '7':
        modify_basket()

    elif user_choice == '8':
        checkout()

    elif user_choice == '9':
        order_his()

    elif user_choice == '10':
        view_acc_info()

    elif user_choice == '11':
        modify_acc_info()

    elif user_choice == '12':
        printline()
        print_heading("Thankyou for visiting Steph's Bookstore!")
        printline()
        exit()

    else:
        print("ERROR: Please enter the number (between 1-12) as your select choice")


elif reg_status == 'n':   

    reg_option = input("Would you like to register or continue without registering?\n\
Enter 'r' to register or 'c' to continue without registering: ")

    reg_option = reg_option.lower()

    if reg_option == 'r':
        reg_user()
        
    elif reg_option == 'c':
        # Non-logged in user's Main menu.
        print("\nSearch Options:\n\
1 - search for books using the book name\n\n\
Information Options:\n\
2 - view list of all books in the application\n\
3 - view all book information in a readable format\n\n\
Purchase Options:\n\
4 - add a book to shopping list\n\
5 - modify the shopping basket\n\
6 - choose to proceed and checkout\n\n\
7 - logout / exit")

        user_choice = input("Enter the number (between 1-7) as your select choice: ")

        if user_choice == '1':
            search_book_name()

        elif user_choice == '2':
            list_books()

        elif user_choice == '3':
            read_book_info()

        elif user_choice == '4':
            add_book()

        elif user_choice == '5':
            modify_basket()

        elif user_choice == '6':
            checkout()

        elif user_choice == '7':
            printline()
            print_heading("Thankyou for visiting Steph's Bookstore!")
            printline()
            exit()

        else:
            print("ERROR: Please enter the number (between 1-7) as your select choice")
        
    else:
        print("ERROR: Please enter 'r' or 'c': ")
        
else:
    print("ERROR: Please enter 'y' or 'n': ")

