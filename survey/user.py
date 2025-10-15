from .survey_factory import SurveyFactory

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def start_survey(self, survey_type: str):
        print(f"{self.name} is starting a {survey_type} survey.")
        survey = SurveyFactory.create_survey(survey_type)
        survey.show_questions()
        score = survey.calculate_score()
        survey.suggest_action()
        print(f"Survey completed with score: {score}\n")
