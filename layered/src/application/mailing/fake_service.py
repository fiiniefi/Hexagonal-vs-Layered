class FakeMailingService:
    def send(
        self,
        sender: str,
        password: str,
        receiver: str,
        subject: str,
        body: str
    ) -> None:
        pass
