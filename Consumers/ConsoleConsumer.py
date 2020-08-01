from Consumers.ConsumerBase import ConsumerBase


class ConsoleConsumer(ConsumerBase):
    def consume(self, message: str) -> None:
        print(message)
