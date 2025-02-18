from typing import List
from ApplicationHooks.ApplicationHookBase import ApplicationHookBase
from ApplicationHooks.LedHook import LedHook
from Consumers.ConsoleConsumer import ConsoleConsumer
from Consumers.ConsumerBase import ConsumerBase
from Consumers.SpeechConsumer import SpeechConsumer
from ReportGenerators.CovidReportGenerator import CovidReportGenerator
from ReportGenerators.WeatherReportGenerator import WeatherReportGenerator
from Triggers.TimeTrigger import TimeTrigger
from Triggers.TriggerBase import TriggerBase
from Triggers.ButtonTrigger import ButtonTrigger
from Configuration import CONFIGURATION

triggers: List[TriggerBase] = [
    TimeTrigger(CONFIGURATION["TRIGGERS"]["DAILY_TRIGGER_TIME"]),
    ButtonTrigger(CONFIGURATION["TRIGGERS"]["BUTTON_TRIGGER_PIN"])
]
report_generators: List[WeatherReportGenerator] = [
    WeatherReportGenerator(CONFIGURATION["REPORT_GENERATORS"]["WEATHER"]),
    CovidReportGenerator()
]
consumer_hooks: List[ApplicationHookBase] = [LedHook(CONFIGURATION["APPLICATION_HOOKS"]["LED"])]
consumers: List[ConsumerBase] = [
    ConsoleConsumer(),
    SpeechConsumer(CONFIGURATION["CONSUMERS"]["SPEECH_CONSUMER"]["SERVICE_ACCOUNT_FILE"])
]


def broadcast(message: str) -> None:
    for consumer_hook in consumer_hooks:
        consumer_hook.report_generation_started()
    for consumer in consumers:
        consumer.prepare_consumption(message)
        
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
