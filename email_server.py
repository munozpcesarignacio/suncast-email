# -*- encoding: utf-8 -*-

import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line

# User configuration

sender_email = 'munozpcesarignacio@gmail.com' #Correo
sender_name = 'Suncast Team'
password = 'nuevocomienzo2021' #Contraseña

receiver_emails = ['cezarignacio2021@gmail.com']
receiver_names = ['César Ignacio Munoz Penailillo']

# Email body
email_html = open('email.html')
email_body = email_html.read()

for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
		print("Sending the email...")
		# Configurating user's info
		msg = MIMEMultipart()
		msg['To'] = formataddr((receiver_name, receiver_email))
		msg['From'] = formataddr((sender_name, sender_email))
		msg['Subject'] = 'Predicción del equipo de Suncast '
		
		msg.attach(MIMEText(email_body, 'html'))

		try:
				# Creating a SMTP session | use 587 with TLS, 465 SSL and 25
				server = smtplib.SMTP('smtp.gmail.com', 587)
				# Encrypts the email
				context = ssl.create_default_context()
				server.starttls(context=context)
				# We log in into our Google account
				server.login(sender_email, password)
				# Sending email from sender, to receiver with the email body
				server.sendmail(sender_email, receiver_email, msg.as_string())
				print('Email sent!')
		except Exception as e:
				print(f'Oh no! Something bad happened!\n{e}')
				break
		finally:
				print('Closing the server...')
				server.quit()
