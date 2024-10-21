##################### Hard Starting Project ######################
import pandas as pd
import smtplib
from datetime import datetime
import random

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
today = datetime.now()
today_tuple = (today.month, today.day)
data = pd.read_csv('birthdays.csv')

birthdays_dict = {
    (row["month"], row["day"]): row for index, row in data.iterrows()
}

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
for birthday_tuple, birthday_row in birthdays_dict.items():
    if today_tuple == birthday_tuple:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
        letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        letter = random.choice(letter_list)
        with open(f"letter_templates/{letter}", "r") as f:
            full_message = f.read()
            birthday_message = full_message.replace("[NAME]", birthday_row["name"])
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



