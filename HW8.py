# HW8.py
# Author: Jonathan Welch 

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.
st.subheader("This web application will count the number of days until a certain date.")
st.title("Date Counter Web Application")
st.subheader("This Web Application will count the number of days until a certain date.")
date = st.date_input("Enter a date: ", value=dt.datetime.now())
button = st.button("Calculate")
def calculate_days(date): int 
"""returns the number of days until the date entered by the user.
args:

date (date): the date entered by the user. Format: YYYY-MM-DD

returns:
int: the number of days until the date entered by the user."""

current_date = dt.datetime.now().date()

days = date - current_date 
days_difference = date - current_date
if days_difference.days < 0:
    raise ValueError("The date entered is in the past.")

def calculate_days(date):
    """returns the number of days until the date entered by the user.
    args:
    date (date): the date entered by the user. Format: YYYY-MM-DD
    returns:
    int: the number of days until the date entered by the user."""
    days_difference = date - current_date
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days

def app():
    if button:
        try:
            result = calculate_days(date)
        except ValueError:
            st.write("Please enter a valid date.")
            return
        st.write(f"current date: {dt.datetime.now().date()}")
        st.write(f"selected date: {date}")
        st.write(f"days until selected date: {result}")
# Import statements (activate venv and install streamlit if you haven't already)
import streamlit as st
import datetime as dt

# Streamlit title, subtitle, date, and button
# The calculate_days function from Lab9.py
# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.
calculate_days_until_birthday = st.date_input("Enter your birthday: ", value=dt.datetime.now())
def calculate_days_until_birthday(date):
    """returns the number of days until the date entered by the user.
    args:
    date (date): the date entered by the user. Format: YYYY-MM-DD
    returns:
    int: the number of days until the date entered by the user."""
    days_difference = date - current_date
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days


# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)
days_until_semester_ends = st.date_input("Enter the end of the semester: ", value=dt.datetime.now())
def days_until_semester_ends(date):
    """returns the number of days until the date entered by the user.
    args:
    date (date): the date entered by the user. Format: YYYY-MM-DD
    returns:
    int: the number of days until the date entered by the user."""
    days_difference = date - current_date
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days
# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include 
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")
days_until_new_years = st.date_input("Enter the end of the semester: ", value=dt.datetime.now())
def days_until_new_years(date):
    new_years = dt.date(2024, 1, 1)
    st.write("🎉")
    """returns the number of days until the date entered by the user.
    args:
    date (date): the date entered by the user. Format: YYYY-MM-DD
    returns:
    int: the number of days until the date entered by the user."""
    days_difference = date - current_date
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days

# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.
button = st.button("Days until New Year's Day")
def days_until_new_years(date):
    new_years = dt.date(2024, 1, 1)
    st.write("🎉")
    below = st.button("Calculate")
    """returns the number of days until the date entered by the user.
    args:
    date (date): the date entered by the user. Format: YYYY-MM-DD
    returns:
    int: the number of days until the date entered by the user."""
    days_difference = date - current_date
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days 
# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# app function from Lab9.py



if __name__ == '__main__':
    app()