from pydantic import BaseModel
class UserInfo(BaseModel):
    high_school: str
    main_subject: str
    prefered_subject: str
    hobby: str
    dream_work: str
    uni_aspectations: str
    uni_decision_choice: str
    continuous_previous_study: str


class DegreeResult(UserInfo):
    degree_predict: dict