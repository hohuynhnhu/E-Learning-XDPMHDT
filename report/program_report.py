from .report import Report

class ProgramReport(Report):
    def __init__(self, report_title="Program Report", report_date=None):
        super().__init__(report_title, report_date)
        self.total_programs = 0
        self.participants = 0
        self.success_rate = 0.0

    def generate_data(self):
        print("Generating program report data...")

    def display_report(self):
        print("Displaying program report...")

    def evaluate_effectiveness(self):
        print("Evaluating program effectiveness...")
