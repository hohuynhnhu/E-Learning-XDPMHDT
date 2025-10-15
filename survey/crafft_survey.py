from datetime import date
from .survey import Survey

class CRAFFTSurvey(Survey):
    def show_questions(self):
        print("Displaying CRAFFT survey questions...")

    def calculate_score(self):
        print("Calculating CRAFFT survey score...")
        return 60

    def suggest_action(self):
        print("Suggesting action based on CRAFFT results...")
