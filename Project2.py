# Project 2
# Name:
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv
import datetime as dt

# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.


# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.
def import_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        contacts = {}
        for row in reader:
            contacts[row[0]] = {
                "Phone": row[1],
                "Email": row[2],
                "Birthday": dt.datetime.strptime(row[3], "%m/%d/%Y"),
            }
    return contacts


# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]
def add_contact(name, phone, email, birthday, contacts):
    """
    Add a contact to the contacts dictionary.

    Parameters:
    name (str): The name of the contact.
    phone (str): The phone number of the contact.
    email (str): The email address of the contact.
    birthday (str): The birthday of the contact in the format 'mm/dd/yyyy'.
    contacts (dict): The dictionary containing the contacts.

    Returns:
    bool: True if the contact is successfully added, False if the contact already exists.

    """
    if name in contacts:
        print("Contact already exists")
        return False
    else:
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Birthday": dt.datetime.strptime(birthday, "%m/%d/%Y"),
        }
        return True

# next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.
def next_birthday(contacts):
    today = dt.datetime.today()
    upcoming_birthdays = []
    for name in contacts:
        birthday = contacts[name]["Birthday"]
        birthday = birthday.replace(year=today.year)
        if birthday >= today:
            upcoming_birthdays.append((birthday, name))
    if len(upcoming_birthdays) == 0:
        print("No birthdays in the next 30 days")
    else:
        upcoming_birthdays.sort()
        print(
            "Next Birthday: {} {}".format(
                upcoming_birthdays[0][0].strftime("%m/%d/%Y"), upcoming_birthdays[0][1]
            )
        )


# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.
def save_csv(filename, contacts):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Birthday"])
        for name in contacts:
            writer.writerow(
                [
                    name,
                    contacts[name]["Phone"],
                    contacts[name]["Email"],
                    contacts[name]["Birthday"].strftime("%m/%d/%Y"),
                ]
            )
    return True


# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.


def main():
    """Add Code here to call the functions and run the program"""
    pass  # Remove this line when you start writing your code

    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?
import csv

with open("contacts.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    contacts = {}
    for row in reader:
        contacts[row[0]] = {
            "Phone": row[1],
            "Email": row[2],
            "Birthday": dt.datetime.strptime(row[3], "%m/%d/%Y"),
        }
    # How many emails are yahoo emails?

    # How many .org emails are there?

    # How many contacts have a birthday in January?


if __name__ == "__main__":
    main()
