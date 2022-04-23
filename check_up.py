import datetime as datime
import smtplib

my_email = "jeremiah.bot@yahoo.com"
my_pass = "hiyhkysgjdgzicrl()"
for x in range(len(lines)):
    if datime.hour == 18:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password = my_pass )
            connection.sendmail(from_addr=my_email, to_addrs="jeremiahhawthorne828@gmail.com",
            msg=f"Subject: Time to record your daliy workouts, Jeremiah"
            f"Please go over to your repl github to record them")
if datime.hour == 18:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password = my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="jeremiahhawthorne828@gmail.com",
            msg=f"Subject: Time to record your daliy workouts, Jeremiah"
            f"Please go over to your repl github to record them")

