class ReportGeneratorBase:
    """Acts as an interface for classes that generate a report about a certain topic"""

    def generate_report(self) -> str:
        """Returns a text containing the generated information"""
        pass
