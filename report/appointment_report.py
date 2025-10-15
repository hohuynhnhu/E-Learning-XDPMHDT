from .report import Report

class AppointmentReport(Report):
    def __init__(self, report_title="Appointment Report", report_date=None):
        super().__init__(report_title, report_date)
        self.total_appointments = 0
        self.completed_appointments = 0
        self.cancelled_appointments = 0

    def generate_data(self):
        print("Generating appointment report data...")

    def display_report(self):
        print("Displaying appointment report...")

    def analyze_schedule(self):
        print("Analyzing appointment schedules...")
