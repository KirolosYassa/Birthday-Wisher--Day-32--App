##################### Extra Hard Starting Project ######################
import os
from dotenv import load_dotenv
import datetime as dt
import smtplib

load_dotenv()
email = os.getenv('MY_EMAIL')
passWord = os.getenv('EMAIL_PASSWORD')

# 1. Update the birthdays.csv
# TODO 1.DONE

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





