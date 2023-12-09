import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

class EmailSender:
    def __init__(self):
        self.from_email = os.getenv("EMAIL_BOT")
        self.password = os.getenv("PWD_EMAIL_BOT")

    def send_email(self, subject, message, to_email, image_path):
        msg = MIMEMultipart('related')
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        html = f"""\
        <html>
          <head></head>
          <body>
            <p>{message}</p>
          </body>
        </html>
        """
        #<img src="cid:image1">
        msg.attach(MIMEText(html, 'html'))

        # Embedding the image
        #with open(image_path, 'rb') as img:
        #    mime_image = MIMEImage(img.read(), _subtype=False)
        #    mime_image.add_header('Content-ID', '<image1>')  # Use Content-ID as reference in HTML
        #    msg.attach(mime_image)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        server.login(self.from_email, self.password)

        server.send_message(msg)

        server.quit()

