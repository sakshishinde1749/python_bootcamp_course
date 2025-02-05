# email SMTP : simple mail transfer protocol

import smtplib

my_email = "sgus7242@gmail.com"
my_password = "xwtj geui kzmy naar"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()       # to make connection secure and msg will get encrypt
    connection.login(user=my_email, password=my_password)   # login into my account
    connection.sendmail(from_addr=my_email,
                        to_addrs="sakshishinde01@yahoo.com",
                        msg="Subject:Hello\n\nthis is body msg")
    connection.close()
