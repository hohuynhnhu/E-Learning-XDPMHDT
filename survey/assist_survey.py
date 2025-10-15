from datetime import date
from .survey import Survey

class ASSISTSurvey(Survey):
    def show_questions(self):
        print("Displaying ASSIST survey questions...")

    def calculate_score(self):
        print("Calculating ASSIST survey score...")
        return 75

    def suggest_action(self):
        print("Suggesting action based on ASSIST results...")
