from typing import List
from ApplicationHooks.ApplicationHookBase import ApplicationHookBase
from ApplicationHooks.LedHook import LedHook
from Consumers.ConsoleConsumer import ConsoleConsumer
from Consumers.ConsumerBase import ConsumerBase
from Consumers.SpeechConsumer import SpeechConsumer
from ReportGenerators.WeatherReportGenerator.WeatherReportGenerator import WeatherReportGenerator
from Triggers.TimeTrigger import TimeTrigger
from Triggers.TriggerBase import TriggerBase
from Triggers.ButtonTrigger import ButtonTrigger
from Configuration import CONFIGURATION

triggers = [
    TimeTrigger(CONFIGURATION["TRIGGERS"]["DAILY_TRIGGER_TIME"]),
    ButtonTrigger(CONFIGURATION["TRIGGERS"]["BUTTON_TRIGGER_PIN"])
]  # type: List[TriggerBase]
report_generators = [WeatherReportGenerator()]  # type: List[WeatherReportGenerator]
consumer_hooks = [LedHook(CONFIGURATION["APPLICATION_HOOKS"]["LED"])]  # type: List[ApplicationHookBase]
consumers = [
    ConsoleConsumer(),
    SpeechConsumer(CONFIGURATION["CONSUMERS"]["SPEECH_CONSUMER"]["SERVICE_ACCOUNT_FILE"])
]  # type: List[ConsumerBase]


def broadcast(message: str) -> None:
    for consumer_hook in consumer_hooks:
        consumer_hook.before_consumers_started()
    for consumer in consumers:
        consumer.consume(message)
    for consumer_hook in consumer_hooks:
        consumer_hook.after_consumers_finished()


def send():
    reports = []
    for report_generator in report_generators:
        reports.append(report_generator.generate_report())

    report_text = "\n".join(reports)
    broadcast(report_text)


def startup():
    for trigger in triggers:
        trigger.register_callback(send)
        trigger.start()
    for consumer_hook in consumer_hooks:
        consumer_hook.application_ready()


startup()
