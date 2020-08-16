from src.mailing.services.base import BaseMailingService


class FakeMailingService(BaseMailingService):
    def send(
        self,
        sender: str,
        password: str,
        receiver: str,
        subject: str,
        body: str
    ) -> None:
        pass
