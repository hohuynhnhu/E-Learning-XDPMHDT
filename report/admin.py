from .report_factory import ReportFactory

class Admin:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def view_report(self, report_type: str):
        report = ReportFactory.create_report(report_type)
        report.generate_data()
        report.display_report()

    def export_report(self, report_type: str, format: str):
        report = ReportFactory.create_report(report_type)
        if format.lower() == "pdf":
            report.export_to_pdf()
        elif format.lower() == "excel":
            report.export_to_excel()
        else:
            print("Unsupported format")
