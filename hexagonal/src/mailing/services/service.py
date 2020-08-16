from src.mailing.services.base import BaseMailingService
from src.mailing.sender import Sender


"""
Interfejs produkcyjnej wersji interfejsu do wysyłania maili.
"""


class MailingService(BaseMailingService):
    DOMAIN_SERVER_MAP = {
        "wp": 'smtp.wp.pl',
    }

    def __init__(self, domain: str) -> None:
        self.sender = Sender(self._get_server(domain))

    def send(
        self,
        sender: str,
        password: str,
        receiver: str,
        subject: str,
        body: str
    ) -> None:
        self.sender.login(sender, password)
        self.sender.send(sender, receiver, subject, body)

    def _get_server(self, domain: str) -> str:
        return self.DOMAIN_SERVER_MAP[domain]
