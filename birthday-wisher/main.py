"""Birthday Wisher"""
import smtplib
import datetime as dt
import random
import pandas

df = pandas.read_csv("birthdays.csv")
birthday_data = df.to_dict(orient='records')
now = dt.datetime.now()

MY_EMAIL = "sundalei2011@163.com"
APP_PASSWORD = "TJyWaHHSdws95bjq"

birthday_templates = []
PLACEHOLDER = "[NAME]"

for index in range(1, 4):
    with open(f"letter_templates/letter_{index}.txt", encoding="utf-8") as letter_data:
        birthday_templates.append(letter_data.read())


def send_email(email, content):
    """send email"""
    with smtplib.SMTP(host="smtp.163.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{content}")


for data in birthday_data:
    if data["month"] == now.month and data["day"] == now.day:
        mail_template = random.choice(birthday_templates)
        mail_content = mail_template.replace(PLACEHOLDER, data["name"])
        send_email(data["email"], mail_content)
