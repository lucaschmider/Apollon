from datetime import datetime
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
        sunset = datetime.utcfromtimestamp(today["sunset"])

        return "In " + city_name + " sind es heute "\
               + str(today["temp"]["day"]) + " Kelvin. Die Minimaltemperatur wird heute "+ str(today["temp"]["min"]) + \
               " Kelvin und die Maximaltemperatur " + str(today["temp"]["max"])  + " Kelvin betragen." + \
               self.__generate_weather_report__(today) +  " Die Sonne wird heute um " + str(sunset.hour) + "." + str(sunset.minute)+ " Uhr untergehen."

    @staticmethod
    def __generate_weather_report__(report: Dict) -> str:
        if "rain" in report.keys():
            return "Der Niederschlag beträgt etwa " + str(report["rain"]) + "mm."
        return "Es ist kein Niederschlag zu erwarten."
