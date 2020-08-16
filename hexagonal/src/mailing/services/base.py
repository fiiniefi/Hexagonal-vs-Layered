from abc import ABC, abstractmethod


"""
Abstrakcja dla interfejsów mailingowych. Udostępnia metodę send.
"""


class BaseMailingService(ABC):
    @abstractmethod
    def send(
        self,
        sender: str,
        password: str,
        receiver: str,
        subject: str,
        body: str
    ) -> None:
        pass
