from abc import ABC, abstractmethod
from datetime import date

class Report(ABC):
    def __init__(self, report_title: str, report_date: date, data=None):
        self.report_title = report_title
        self.report_date = report_date
        self.data = data or []

    @abstractmethod
    def generate_data(self):
        pass

    @abstractmethod
    def display_report(self):
        pass

    def export_to_pdf(self):
        print(f"Exporting {self.report_title} to PDF...")

    def export_to_excel(self):
        print(f"Exporting {self.report_title} to Excel...")
