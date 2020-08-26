from ReportGenerators.ReportGeneratorBase import ReportGeneratorBase
import requests


class CovidReportGenerator(ReportGeneratorBase):
    __last_case_count__: int = None
    __last_death_count__: int = None

    def generate_report(self) -> str:
        response = requests.get(
            "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Coronaf%C3%A4lle_in_den_Bundesl%C3"
            "%A4ndern/FeatureServer/0/query?where=1%3D1&outFields=LAN_ew_GEN,Fallzahl,"
            "Death&returnGeometry=false&outSR=4326&f=json")

        if response.status_code != 200:
            print(response.status_code)

        cases_today = sum(state["attributes"]["Fallzahl"] for state in response.json()["features"])
        deaths_today = sum(state["attributes"]["Death"] for state in response.json()["features"])

        report = "Bis heute wurden dem RKI {} Fälle des neuartigen Coronavirus gemeldet. "\
            .format(cases_today)
        if self.__last_case_count__ is not None:
            report += "Seit der letzten Abfrage sind das {} neue Fälle. "\
                .format(cases_today-self.__last_case_count__)
        report += "Außerdem werden deutschlandweit {} Todesfälle mit der Krankheit in Verbindung gebracht. "\
            .format(deaths_today)
        if self.__last_death_count__ is not None:
            report += "{} mehr als bei der letzten Meldung"\
                .format(deaths_today-self.__last_death_count__)

        self.__last_case_count__ = cases_today
        self.__last_death_count__ = deaths_today
        return report
