from .assist_survey import ASSISTSurvey
from .crafft_survey import CRAFFTSurvey

class SurveyFactory:
    @staticmethod
    def create_survey(survey_type: str):
        if survey_type.lower() == "assist":
            return ASSISTSurvey("ASSIST Survey", None)
        elif survey_type.lower() == "crafft":
            return CRAFFTSurvey("CRAFFT Survey", None)
        else:
            raise ValueError("Unknown survey type")
