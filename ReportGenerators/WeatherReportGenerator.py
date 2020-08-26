from datetime import datetime, timedelta
from typing import Dict

from ReportGenerators.ReportGeneratorBase import ReportGeneratorBase
import requests


class WeatherReportGenerator(ReportGeneratorBase):
    def generate_report(self) -> str:
        response = requests.get("https://api.openweathermap.org/data/2.5/forecast/daily?appid=b2d64a2fbedaa12f1f48ebd117b31e74&zip=77761,de&cnt=2")
        if response.status_code != 200:
            print(response.status_code)

        weather = response.json()
        city_name = weather["city"]["name"]
        today = weather["list"][0]

        average_temp = self.__kelvin_to_celsius__(today["temp"]["day"])
        min_temp = self.__kelvin_to_celsius__(today["temp"]["min"])
        max_temp = self.__kelvin_to_celsius__(today["temp"]["max"])
        sunset = datetime.utcfromtimestamp(today["sunset"]) + timedelta(seconds=int(weather["city"]["timezone"]))

        return "In " + city_name + " sind es heute "\
               + str(average_temp) + "°C. Die Minimaltemperatur wird heute "+ str(min_temp) + \
               "°C und die Maximaltemperatur " + str(max_temp)  + "°C betragen." + \
               self.__generate_weather_report__(today) +  " Die Sonne geht heute um " + str(sunset.hour) + "." + str(sunset.minute)+ " Uhr Ortszeit unter."

    @staticmethod
    def __generate_weather_report__(report: Dict) -> str:
        if "rain" in report.keys():
            return "Der Niederschlag beträgt etwa " + str(report["rain"]) + "mm."
        return "Es ist kein Niederschlag zu erwarten."

    @staticmethod
    def __kelvin_to_celsius__(kelvin: float):
        return round(kelvin -273.15, 2)
