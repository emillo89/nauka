import smtplib

my_email = "appbrewery5@gmail.com"
password = "testowe1234"

with smtplib.SMTP("smtp.gmail.com") as connection:
    #tls Transport Layer Security -(Security connection)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="emilszczesniak@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")
