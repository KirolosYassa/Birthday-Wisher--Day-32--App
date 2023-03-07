##################### Extra Hard Starting Project ######################
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import datetime as dt
import smtplib
import pandas
from random import choice

load_dotenv()
email = os.getenv('MY_EMAIL')
passWord = os.getenv('EMAIL_PASSWORD')

# 1. Update the birthdays.csv
# TODO 1.DONE

# 2. Check if today matches a birthday in the birthdays.csv

with open("./letter_templates/letter_1.txt") as data:
    letter_1 = data.read()
with open("./letter_templates/letter_2.txt") as data:
    letter_2 = data.read()
with open("./letter_templates/letter_3.txt") as data:
    letter_3 = data.read()

birthdays = pandas.read_csv("birthdays.csv")
# print(birthdays)
now = dt.datetime.now()
this_day = now.day
this_month = now.month


for (index, row) in birthdays.iterrows():
    if this_month == row["month"] and this_day == row["day"]:
        name = row["name"]
        print(f"Today is {name}'s Birthday")
        letter_1 = letter_1.replace("[NAME]", name)
        letter_2 = letter_2.replace("[NAME]", name)
        letter_3 = letter_3.replace("[NAME]", name)
        subject = f"Today Don't forget to Celebrate for {name}'s Birthday"
        message = choice([letter_1, letter_2, letter_3])
        
        msg = EmailMessage()
        msg['Subject'] = f"Today Don't forget to Celebrate for {name}'s Birthday"
        msg['From'] = email 
        msg['To'] = row["email"]
        msg.set_content(message, subtype='html')

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=passWord)
            connection.send_message(msg)
            # connection.sendmail(
            #     from_addr=email,
            #     to_addrs=to_mail,
            #     msg=f"Subject:{subject}\n{message}")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





