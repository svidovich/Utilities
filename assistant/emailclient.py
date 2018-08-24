# For now this is a test script to send emails via python
# later I am going to turn it into an API that makes the whole process easier

import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
# Let's begin talking with the server

try:
	server.starttls()
	server.login("","")
except Exception as e:
	print("Exception occured: {}".format(e))
	server.quit()

msg = "This is a test message from the assistant application. Do not panic."

try:
	print("Sending email message.")
	server.sendmail("", "", msg)
except Exception as e:
	print("Exception occured: {}".format(e))
finally:
	server.quit()
