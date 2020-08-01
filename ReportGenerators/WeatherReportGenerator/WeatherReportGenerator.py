from ReportGenerators.ReportGeneratorBase import ReportGeneratorBase
import requests


class WeatherReportGenerator(ReportGeneratorBase):
    def generate_report(self) -> str:
        #response = requests.get("https://api.openweathermap.org/data/2.5/forecast?appid=b2d64a2fbedaa12f1f48ebd117b31e74&zip=77761,de")
        #if response.status_code != 200:
        #    print(response.status_code)

        #weather = response.json()
        #city_name = weather["city"]["name"]
        city_name ="Schiltach"
        current_temperature = 0
        todays_low = 0
        todays_high = 10
        maximum_rain_probability = 30
        sun_low = 10

        return "In " + city_name + " sind es gerade "\
               + str(current_temperature) + " Kelvin. Die Minimltemperatur wird heute "+ str(todays_low) + \
               " Kelvin und die Maximaltemperatur " + str(todays_high)  + " Kelvin betragen. Die maximale Regenwahrscheinlichkeit beträgt "\
               + str(maximum_rain_probability) + "%. Die Sonne wird heute um " + str(sun_low) + " untergehen."
