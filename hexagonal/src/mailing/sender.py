import smtplib
from email.message import EmailMessage


"""
Wysyłanie maili przez SMTP.
"""


class Sender:
    def __init__(self, server) -> None:
        self.server = smtplib.SMTP_SSL(server, 465)

    def login(self, login: str, password: str) -> None:
        self.server.login(login, password)

    def send(self, sender: str, receiver: str, subject: str, body: str) -> None:
        self.server.send_message(
            from_addr=sender,
            to_addrs=receiver,
            msg=self._create_message(sender, receiver, subject, body)
        )

    @staticmethod
    def _create_message(login: str, receiver: str, subject: str, body: str) -> EmailMessage:
        message = EmailMessage()
        message['From'] = login
        message['To'] = receiver
        message['Subject'] = subject
        message['Body'] = body
        return message
