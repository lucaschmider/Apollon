from Consumers.ConsoleConsumer import ConsoleConsumer
from Consumers.ConsumerBase import ConsumerBase
from ReportGenerators.WeatherReportGenerator.WeatherReportGenerator import WeatherReportGenerator
from Triggers.TimeTrigger import TimeTrigger
from Triggers.TriggerBase import TriggerBase

triggers = [TimeTrigger()]  # type: List[TriggerBase]
report_generators = [WeatherReportGenerator()]  # type: List[WeatherReportGenerator]
consumers = [ConsoleConsumer()]  # type: List[ConsumerBase]


def broadcast(message: str) -> None:
    for consumer in consumers:
        consumer.consume(message)


def send():
    reports = []
    for report_generator in report_generators:
        reports.append(report_generator.generate_report())

    report_text = "\n".join(reports)
    print(report_text)


def startup():
    for trigger in triggers:
        trigger.register_callback(send)
        trigger.start()


startup()
