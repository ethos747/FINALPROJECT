# Course: CS 30
# Period: 3
# File created 11/25/21
# Last edited 01/19/22
# Name: Ethan Behl
# Description: Main file for the Contact Organizer
# Imports
try:
    import ADD
    import CONTACTS
    import sys
except ImportError:
    print("Import error on MAINFILE")
    sys.exit()
# Starting variables that determine a couple code functions
example = True
MAIN = False
# Initiates the text files of the program for saved contacts
file = open("SAVED_CONTACTS.txt", "r")
list_of_lists = [(line.strip()).split() for line in file]
file.close()
print(list_of_lists)
ADD.CHECK_CONTACT()
# The following variables control the while loop for applying the saved contact
y = 1
x = 1
while y <= 9:
    try:
        ADD.CHECK_CONTACT()
        ADD.current_contact.append(str(list_of_lists[x]))
        x += 1
        ADD.current_contact.append(str(list_of_lists[x]))
        x += 1
        ADD.current_contact.append(str(list_of_lists[x]))
        x += 1
        ADD.current_contact.append(str(list_of_lists[x]))
        x += 1
        y += 1
        ADD.current_contact[0] = ADD.current_contact[0].replace("[", "")
        ADD.current_contact[0] = ADD.current_contact[0].replace("]", "")
        ADD.current_contact[0] = ADD.current_contact[0].replace("'", "")
        ADD.current_contact[0] = ADD.current_contact[0].replace(",", "")
        ADD.current_contact[1] = ADD.current_contact[1].replace("[", "")
        ADD.current_contact[1] = ADD.current_contact[1].replace("]", "")
        ADD.current_contact[1] = ADD.current_contact[1].replace("'", "")
        ADD.current_contact[1] = ADD.current_contact[1].replace(",", "")
        ADD.current_contact[2] = ADD.current_contact[2].replace("[", "")
        ADD.current_contact[2] = ADD.current_contact[2].replace("]", "")
        ADD.current_contact[2] = ADD.current_contact[2].replace("'", "")
        ADD.current_contact[2] = ADD.current_contact[2].replace(",", "")
        ADD.current_contact[3] = ADD.current_contact[3].replace("[", "")
        ADD.current_contact[3] = ADD.current_contact[3].replace("]", "")
        ADD.current_contact[3] = ADD.current_contact[3].replace("'", "")
        ADD.current_contact[3] = ADD.current_contact[3].replace(",", "")
        CONTACTS.contact += 1
    except IndexError:
        y = 10
        None


# Main menu loop
while True:
    # Clears the screen, prints the title and menu
    ADD.clear()
    print("C O N T A C T  O R G A N I Z E R\n")
    """f = open("SAVED_CONTACTS.txt","r+")
    f. truncate(0)"""
    print("""
What would you like to do?
\n[1] View current contacts
\n[2] Add new contact
\n[3] Save contacts and quit""")
    if example == True:
        print("\n[4] Add  example contacts because you have no friends")
    user_in = input(" ")
    ADD.clear()
    if user_in == "1":
        # Opens and displays contacts for the user
        CONTACTS.open_contact()
    elif user_in == "2":
        # Starts adding a contact
        MAIN = True
        ADD.ADD_CONTACT()
    elif user_in == "3":
        # Prints out current saved contacts
        while CONTACTS.contact >= 1:
            CONTACTS.contact -= 1
            ADD.CHECK_CONTACT()
            f = open("SAVED_CONTACTS.txt", "w")
            while CONTACTS.contact >= 1:
                ADD.CHECK_CONTACT()
                if ADD.current_contact[0] == "CONTACT DELETED":
                    ADD.current_contact.clear()
                    CONTACTS.contact -= 1
                    ADD.CHECK_CONTACT()
                else:
                    try:
                        f.write("\n" + ADD.current_contact[0])
                        f.write("\n" + ADD.current_contact[1])
                        f.write("\n" + ADD.current_contact[2])
                        f.write("\n" + ADD.current_contact[3])
                    except IndexError:
                        None
                CONTACTS.contact -= 1
        f = open("SAVED_CONTACTS.txt", "w")
        f.close()
        sys.exit()
    elif user_in == "4":
        # Adds a couple of contacts for ease of testing and showcase
        MAIN = True
        ADD.EXAMPLE_CONTACTS()
        example = False
