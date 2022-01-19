# Course: CS 30
# Period: 3
# File created 11/25/21
# Last edited 01/19/22
# Name: Ethan Behl
# Description: File that controls functons integral to the application
# Imports
try:
    import ADD
    import sys
except ImportError:
    print("Import error on MAINFILE")
    sys.exit()

# Starting variable that determines code functions
contact = 1


def open_contact():
    """Modify contact menu"""
    ADD.INFO()
    mod_in = input("""
Would you like to do anything?
[1] Modify Contact
[2] Reset All Contacts
[3] Return To Menu""")
    if mod_in == "1":
        ADD.MODIFY_CONTACT()
    elif mod_in == "2":
        ADD.RESET_CONTACTS()
        f = open("SAVED_CONTACTS.txt", "r+")
        f. truncate(0)
    else:
        None
