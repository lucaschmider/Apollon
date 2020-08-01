from Consumers.ConsoleConsumer import ConsoleConsumer
from Consumers.ConsumerBase import ConsumerBase
from Triggers.TimeTrigger import TimeTrigger
from Triggers.TriggerBase import TriggerBase

triggers = [TimeTrigger()]  # type: List[TriggerBase]
consumers = [ConsoleConsumer()]  # type: List[ConsumerBase]


def broadcast(message: str) -> None:
    for consumer in consumers:
        consumer.consume(message)

def send():
    broadcast("Hallo")

def startup():
    for trigger in triggers:
        trigger.register_callback(send)
        trigger.start()


startup()
