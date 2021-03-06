import smtplib
import datetime as dt
import random


MY_EMAIL = "teste@gmail.com"
MY_PASSWORD = "teste"

#E-mail
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="appbrewerytesting@yahoo.com",
#                         msg="Subject:Hello!!\n\nThis is the body of my email"
#     )


#Datetime
date = dt.datetime.now()
weekday = date.weekday()


#Quotes
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Motivation\n\n{quote}"
        )