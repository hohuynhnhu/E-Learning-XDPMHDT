from .report import Report

class SurveyReport(Report):
    def __init__(self, report_title="Survey Report", report_date=None):
        super().__init__(report_title, report_date)
        self.total_participants = 0
        self.average_score = 0.0

    def generate_data(self):
        print("Generating survey report data...")

    def display_report(self):
        print("Displaying survey report...")

    def analyze_survey(self):
        print("Analyzing survey results...")
