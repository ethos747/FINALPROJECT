# Course: CS 30
# Period: 3
# File created 11/25/21
# Last edited 01/05/22
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
file = open("SAVED_CONTACTS.txt", "r")
list_of_lists = [(line.strip()).split() for line in file]
file.close()
print(list_of_lists)
ADD.CHECK_CONTACT()
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
        CONTACTS.contact += 1
    except IndexError:
        y = 10
        None
"""try:
    ADD.current_contact.append(str(list_of_lists[1]))  
    ADD.current_contact.append(str(list_of_lists[2]))
    ADD.current_contact.append(str(list_of_lists[3]))
    ADD.current_contact.append(str(list_of_lists[4]))
    CONTACTS.contact += 1
    try:
        ADD.CHECK_CONTACT()
        ADD.current_contact.append(str(list_of_lists[5]))
        ADD.current_contact.append(str(list_of_lists[6]))
        ADD.current_contact.append(str(list_of_lists[7]))
        ADD.current_contact.append(str(list_of_lists[8]))
        CONTACTS.contact += 1
        try:
            ADD.CHECK_CONTACT()
            ADD.current_contact.append(str(list_of_lists[9]))
            ADD.current_contact.append(str(list_of_lists[10]))
            ADD.current_contact.append(str(list_of_lists[11]))
            ADD.current_contact.append(str(list_of_lists[12]))
            CONTACTS.contact += 1
            try:
                ADD.CHECK_CONTACT()
                ADD.current_contact.append(str(list_of_lists[13]))
                ADD.current_contact.append(str(list_of_lists[14]))
                ADD.current_contact.append(str(list_of_lists[15]))
                ADD.current_contact.append(str(list_of_lists[16]))
                CONTACTS.contact += 1
                try:
                    ADD.CHECK_CONTACT()
                    ADD.current_contact.append(str(list_of_lists[17]))
                    ADD.current_contact.append(str(list_of_lists[18]))
                    ADD.current_contact.append(str(list_of_lists[19]))
                    ADD.current_contact.append(str(list_of_lists[20]))
                    CONTACTS.contact += 1
                    try:
                        ADD.CHECK_CONTACT()
                        ADD.current_contact.append(str(list_of_lists[21]))
                        ADD.current_contact.append(str(list_of_lists[22]))
                        ADD.current_contact.append(str(list_of_lists[23]))
                        ADD.current_contact.append(str(list_of_lists[24]))
                        CONTACTS.contact += 1
                        try:
                            ADD.CHECK_CONTACT()
                            ADD.current_contact.append(str(list_of_lists[25]))
                            ADD.current_contact.append(str(list_of_lists[26]))
                            ADD.current_contact.append(str(list_of_lists[27]))
                            ADD.current_contact.append(str(list_of_lists[28]))
                            CONTACTS.contact += 1
                            try:
                                ADD.CHECK_CONTACT()
                                ADD.current_contact.append(str(list_of_lists[25]))
                                ADD.current_contact.append(str(list_of_lists[26]))
                                ADD.current_contact.append(str(list_of_lists[27]))
                                ADD.current_contact.append(str(list_of_lists[28]))
                                CONTACTS.contact += 1
                                try:
                                    ADD.CHECK_CONTACT()
                                    ADD.current_contact.append(str(list_of_lists[25]))
                                    ADD.current_contact.append(str(list_of_lists[26]))
                                    ADD.current_contact.append(str(list_of_lists[27]))
                                    ADD.current_contact.append(str(list_of_lists[28]))
                                    CONTACTS.contact += 1
                                    try:
                                        ADD.CHECK_CONTACT()
                                        ADD.current_contact.append(str(list_of_lists[25]))
                                        ADD.current_contact.append(str(list_of_lists[26]))
                                        ADD.current_contact.append(str(list_of_lists[27]))
                                        ADD.current_contact.append(str(list_of_lists[28]))
                                        CONTACTS.contact += 1
                                    except IndexError:
                                        None
                                except IndexError:
                                    None
                            except IndexError:
                                None
                        except IndexError:
                            None
                    except IndexError:
                        None
                except IndexError:
                    None
            except IndexError:
                None
        except IndexError:
            None
    except IndexError:
        None
except IndexError:
    None"""


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
        #if MAIN == False:
            #print("You have no friends.")
        #else:
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
                try:
                    f.write("\n" + ADD.current_contact[0])
                    f.write("\n" + ADD.current_contact[1])
                    f.write("\n" + ADD.current_contact[2])
                    f.write("\n" + ADD.current_contact[3])
                    CONTACTS.contact -= 1 
                except IndexError:
                    None
        f.close()
        sys.exit()
    elif user_in == "4":
        # Adds a couple of contacts for ease of testing and showcase
        MAIN = True
        ADD.EXAMPLE_CONTACTS()
        example = False
