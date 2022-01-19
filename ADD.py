# Course: CS 30
# Period: 3
# File created 11/25/21
# Last edited 01/19/22
# Name: Ethan Behl
# Description: File that carries functions and beginning variables
# Imports
try:
    import CONTACTS
    from os import system, name
    import sys
except ImportError:
    print("Import error on MAINFILE")
    sys.exit()


def clear():
    """Function that clears the user's screen"""
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# Contact lists
contact_1 = []
contact_2 = []
contact_3 = []
contact_4 = []
contact_5 = []
contact_6 = []
contact_7 = []
contact_8 = []
contact_9 = []
contact_10 = []
# Starting variables that determine code functions
current_contact = contact_1
full_name = None
phone_number = None
email = None
con_num = 1
skip = 0


def CHECK_CONTACT():
    """Adjusts the current contact to the appropriate list"""
    global current_contact
    if CONTACTS.contact == 1:
        current_contact = contact_1
    elif CONTACTS.contact == 2:
        current_contact = contact_2
    elif CONTACTS.contact == 3:
        current_contact = contact_3
    elif CONTACTS.contact == 4:
        current_contact = contact_4
    elif CONTACTS.contact == 5:
        current_contact = contact_5
    elif CONTACTS.contact == 6:
        current_contact = contact_6
    elif CONTACTS.contact == 7:
        current_contact = contact_7
    elif CONTACTS.contact == 8:
        current_contact = contact_8
    elif CONTACTS.contact == 9:
        current_contact = contact_9
    elif CONTACTS.contact == 10:
        current_contact = contact_10


def ADD_CONTACT():
    """The function that adds contacts (Info into a list)"""
    CHECK_CONTACT()
    first_name_in = input("What is the first name of your contact?")
    last_name_in = input("What is the last name of your contact?")
    if first_name_in == "":
        if last_name_in == "":
            current_contact.append("No name entered.")
    else:
        full_name = (str(first_name_in) + " " + str(last_name_in))
        current_contact.append(full_name)
    phone_in = input("""
Would you like to enter a phone number?
[1] Yes
[2] No
""")
    if phone_in == "1":
        # Phone number information input
        phone_area_in = input("What is the area code of" +
        "their phone number?")
        phone_3diget_in = input("What is the 3 diget" +
        "set of their phone number?")
        phone_4digit_in = input("What is the 4 digit" +
        "set of their phone number?")
        phone_number = ("(" + str(phone_area_in) + ") " +
        str(phone_3diget_in) + "-" + str(phone_4digit_in))
        current_contact.append(phone_number)
    else:
        # Stand in when phone number not added
        print("\nNo phone number entered.")
        current_contact.append("No phone number entered.")
    email_in = input("""
Would you like to enter an email?
[1] Yes
[2] No
""")
    if email_in == "1":
        # Email information input
        email = input("What is their email?")
        current_contact.append(email)
    else:
        # Stand in when email not added
        print("\nNo email entered.")
        current_contact.append("No email entered.")
    desc_in = input("""
Would you like to enter any additional information?
[1] Yes
[2] No
""")
    if desc_in == "1":
        # Description information input
        desc = input("What information would you like to add?")
        current_contact.append(desc)
    else:
        # Stand in when description not added
        print("No description entered.")
        current_contact.append("No description entered.")
    CONTACTS.contact += 1


# contact goes down, num goes up
def INFO():
    """Prints out the contact information"""
    global con_num
    CONTACTS.contact -= 1
    CHECK_CONTACT()
    con_num = 0
    only_alpha = ""
    try:
        for char in current_contact[0]:
            if char.isalpha():
                only_alpha += char
    except IndexError:
        None
    while CONTACTS.contact >= 1:
        # Prints out contacts for display
        CHECK_CONTACT()
        print("\n" + current_contact[0])
        print(" > " + current_contact[1])
        print(" > " + current_contact[2])
        print(" > " + current_contact[3])
        con_num += 1
        CONTACTS.contact -= 1
    CONTACTS.contact = con_num
    CONTACTS.contact += 1
    CHECK_CONTACT()


def EXAMPLE_CONTACTS():
    """ Applies the example contacts"""
    CHECK_CONTACT()
    current_contact.append("Mike Untz")
    current_contact.append("(306) 241-6968")
    current_contact.append("sussybaka@hotmail.com")
    current_contact.append("No description entered.")
    CONTACTS.contact += 1
    CHECK_CONTACT()
    current_contact.append("Ashoosh Poonda")
    current_contact.append("No phone number entered.")
    current_contact.append("pandalad@icloud.com")
    current_contact.append("No description entered.")
    CONTACTS.contact += 1
    CHECK_CONTACT()
    current_contact.append("Biga Sole")
    current_contact.append("(639) 555-4336")
    current_contact.append("No email entered.")
    current_contact.append("No description entered.")
    CONTACTS.contact += 1
    CHECK_CONTACT()


def MODIFY_CONTACT():
    """Controls the modifications of all contacts"""
    global con_num
    global skip
    clear()
    print("Which contact would you like to modify?")
    CONTACTS.contact -= 1
    CHECK_CONTACT()
    con_num = 0
    while CONTACTS.contact >= 1:
        # Loop that prints out contacts to user for modification
        CHECK_CONTACT()
        print((str(CONTACTS.contact)) + "\n" + (str(current_contact[0])) +
        "\n > " + (str(current_contact[1])) +
        "\n > " + (str(current_contact[2])) +
        "\n > " + (str(current_contact[3])))
        con_num += 1
        CONTACTS.contact -= 1
    mod_contact_in = input(" ")
    try: 
        CONTACTS.contact = int(mod_contact_in)
    except ValueError:
        skip = 1
    if skip == 1:
        skip = 0
    elif con_num < int(mod_contact_in):
        None
    else:
        CHECK_CONTACT()
        print(str(current_contact))
        # Mod menu
        mod_info_in = input("""
What information do you want to modify?
[1] Name
[2] Phone Number
[3] Email
[4] Description
[5] Delete Contact
""")
        if mod_info_in == "1":
            # Replace the current contact's name
            first_name_in = input("What is the first name of your contact?")
            last_name_in = input("What is the last name of your contact?")
            full_name = (str(first_name_in) + " " + str(last_name_in))
            current_contact[0] = full_name
        elif mod_info_in == "2":
            # Replace the current contact's phone number
            phone_area_in = input("What is the area code of" +
            "their phone number?")
            phone_3diget_in = input("What is the 3 diget" +
            "set of their phone number?")
            phone_4digit_in = input("What is the 4 digit" +
            "set of their phone number?")
            phone_number = ("(" + str(phone_area_in) + ") " +
            str(phone_3diget_in) + "-" + str(phone_4digit_in))
            current_contact[1] = phone_number
        elif mod_info_in == "3":
            # Replace the current contact's email
            email = input("What is their email?")
            current_contact[2] = email
        elif mod_info_in == "4":
            # Replace the current contact's description
            desc = input("What information would you like to add?")
            current_contact[3] = desc
        elif mod_info_in == "5":
            # Delete the current contact, replaced with place holders
            current_contact.clear()
            current_contact.append("CONTACT DELETED")
            current_contact.append("Reload application to delete this.")
            current_contact.append(" ")
            current_contact.append(" ")
        CONTACTS.contact = con_num
        CONTACTS.contact += 1
        CHECK_CONTACT()


def RESET_CONTACTS():
    """Resets all contacts"""
    global current_contact
    CONTACTS.contact -= 1
    while CONTACTS.contact >= 1:
        CHECK_CONTACT()
        current_contact.clear()
        CONTACTS.contact -= 1
    CONTACTS.contact += 1
