from abc import ABC, abstractmethod
from datetime import date

class Survey(ABC):
    def __init__(self, report_title: str, report_date: date, data=None):
        self.report_title = report_title
        self.report_date = report_date
        self.data = data or []

    @abstractmethod
    def show_questions(self):
        pass

    @abstractmethod
    def calculate_score(self):
        pass

    @abstractmethod
    def suggest_action(self):
        pass
