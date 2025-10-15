from .survey_report import SurveyReport
from .appointment_report import AppointmentReport
from .program_report import ProgramReport

class ReportFactory:
    @staticmethod
    def create_report(report_type: str):
        if report_type.lower() == "survey":
            return SurveyReport()
        elif report_type.lower() == "appointment":
            return AppointmentReport()
        elif report_type.lower() == "program":
            return ProgramReport()
        else:
            raise ValueError("Unknown report type")
