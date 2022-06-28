import smtplib
import os

my_email = os.environ["MY_EMAIL"]
password = os.environ["MY_PASSWORD"]

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #tls Transport Layer Security -(Security connection)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="emilszczesniak@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")
