from email.message import EmailMessage
import ssl
import smtplib

class Mailer:

    def __init__(self, sender, password):
        self.sender = sender
        self.password = password

    def sendMessage(self, santaEmail, santaName, receiverName):
            
        # Set subject and body of message
        subject = "Rich Homie Secret Santa 2023"
        body = "Hi " + santaName + ", looks like you're getting a gift for " + receiverName + " this year :)"

        # Initialize and Set Message Data
        em = EmailMessage()
        em['From'] = self.sender
        em['TO'] = santaEmail
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, santaEmail, em.as_string())