from Consumers.ConsoleConsumer import ConsoleConsumer
from Consumers.ConsumerBase import ConsumerBase

consumers = [ConsoleConsumer()]  # type: List[ConsumerBase]


def broadcast(message: str) -> None:
    for consumer in consumers:
        consumer.consume(message)


broadcast("Hallo Welt")
