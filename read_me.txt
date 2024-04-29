Web-Based Application for a Bookstore:

- Available for Registered and Unregistered users.

  - Unregistered users can:
    - search for books using the book name.
	- view list of all books in the application.
	- read book information (overview, authors, etc.).
	- add a book to the shopping basket.
	- modify the shopping basket.
	- choose to proceed and checkout.
	
  - Registered users can:
    (all of the above, plus:)
    - search for books by giving the name of an author or ISBN of the book.
	- access order history.
	- view account details.
	- modify account details (firstname, lastname, email and password.

- Registration process:
  - promps user to enter: firstname, lastname, email and password.
  - login using the email address and password.
  
'''	
'''
Before Application starts:
- Create a txt file to read from, containing all of the books in the bookstore
  in a dictionary / Class tuple.
- Create Functions for every step to start with.
- Create Classes for the books.
- Create Classes for book orders?

1) Ask users if they are already registered, would like to register or
   would like to continue without registering.

1a) User Registration Process:
 - register first user, open up a txt file to write to and read from.
 - prompt user for require registration details.
 - check that email address is not already registered,
   and contains '@' and '.'.
 - as user for password input twice, and check they match.
 - append details to the txt file, a new line for each, 
   and details joined with a comma.

1b) Login Process:
 - prompt user for a email to login with.
 - check that email is in txt file created in registration.
 - if so ask for password.
 - check if password is in txt file.
 - if not option user to register or login with another email.
 
1c) Continue straight to next section without registering, 
    but this restricts access to services.

2) Show menu of options:
    Search options:
	1 - search for books using the book name.
	2 - search for books using the name of author.
	3 - search for books using ISBN of the book.
	
	Information options:
	4 - view list of all books in the application.
	5 - view all book information in a readable format.
	
	Purchase options:
	6 - add a book to shopping list.
	7 - modify the shopping basket.
	8 - choose to proceed and checkout.
	
	Account options:
	9 - access order history.
	10 - view account details.
	11 - modify account details.
	12 - logout / exit.
	 
3)  Main Menu:
   1. - prompt user for input of a book name.
      - search string of book name in txt file dictionary.
	  - if found announce a match and give option to purchase.
	  - if not announce new match and allow a new search.
	  - option to exit.
	 
   2. - check if user is registered, if not give them option of 
        registering or exit.
      - prompt user for input of an author.
      - search for string of athor in txt file dictionary.
	  - if found announce a match and give option to purchase.
	  - if not announce new match and allow a new search.
	  - option to exit.
	  
   3. - check if user is registered, if not give them option of 
        registering or exit.
      - prompt user for input of an ISBN.
      - search for string of ISBN in txt file dictionary.
	  - if found announce a match and give option to purchase.
	  - if not announce new match and allow a new search.
	  - option to exit.
	  
   4. - print full list of book names from txt file.
   
   5. - print full list of information for all books from txt file,
        in a readable format.
		
   6. - create a new txt file to append to and read from, a shopping cart.
      - ask for input of information for which book to put into basket.
	  - print updated basket to user.
	  - ask if user would like to add another item? y/n
	  - if y ask for input again.
	  - if n return to main menu.
	  
   7. - check that there is a txt file for that user to view.
      - if so print shopping basket to user and ask what they would like 
	    to modify.
      - change details modified in txt file.
	  - print updated shopping basket.
	  - return to main menu.
   
   8. - give option to checkout, y/n
      - if y print order confirmed and change confirmation status to True.
	  - if n return to main menu.
	  
   9. - check if user is registered.
      - if not don't allow access.
	  - if they are, print all confirmed orders with details
	    in a readable format.
		
  10. - check if user is registered.
      - if not don't allow access.
	  - if they are, print all account details in a readable format.
  
  
  11. - check if user is registered.
      - if not don't allow access.
	  - if they are ask which details they would like to modify.
	  - ask for input of new data.
	  - re-write the txt file with updated data.
  
  
  12. - exit application.