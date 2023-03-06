import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('MY_EMAIL')
passWord = os.getenv('EMAIL_PASSWORD')

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=passWord)
    connection.sendmail(
        from_addr=email,
        to_addrs="kirolosyassa2017@gmail.com",
        msg="Subject:New msg with env trial\nHey its okay again, Don't worry.")

# print(email, passWord)