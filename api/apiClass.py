from pydantic import BaseModel
from typing import Optional
from commons_func.generic_func import *
from fastapi import Depends, FastAPI,  HTTPException
from db.db_operations import  *
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer


app = FastAPI(debug=True, title="AIuniversity-API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

class BoolResult(BaseModel):
    result: bool

class UniInfo(BaseModel):
    uni: str
    course: str

class UserInfo(BaseModel):
    region: str
    province: str
    high_school: str
    main_subject: str
    prefered_subject: str
    hobby: str
    dream_work: str
    uni_aspectations: str
    uni_decision_choice: str
    continuous_previous_study: str


class SubscriptionInfo(BaseModel):
    age: int
    gender: str
    hometown: str
    home_province: str
    home_region: str
    outpost: str
    study_town: str
    study_province: str
    study_region: str
    difficulties_transferring:  Optional[str] = "" #TODO: si può togliere
    difficulties_list:  Optional[str] = "" #TODO: si può togliere
    study_type: str
    university: str
    other_uni: str
    uni_type:  str
    department: str
    degree_course: str
    subject_area: str
    enrolment_year: int
    end_year: int
    enrolment_type: str
    graduation_grade:  Optional[int] = 0 #TODO: solo per laureati
    degree_year: Optional[int] = 0  #TODO: solo per studenti
    average_grade: Optional[int] = 0 #TODO: solo per studenti
    exams_not_done: Optional[str] = "" #TODO: solo per studenti
    numb_exams_not_done: Optional[int] = 0 #TODO: solo per studenti
    difficult_aspect: str
    easy_exams: str
    hard_exams: str
    redo_choice: str
    reason_redo_choice: Optional[str] = "" #TODO: si può togliere
    decision_choice: Optional[str] = "" #TODO: si può togliere
    expectations: str
    expectations_met: Optional[str] = "" #TODO: si può togliere
    expectations_no: Optional[str] = "" #TODO: si può togliere
    advice: Optional[str] = "" #TODO: si può togliere
    advice_why: Optional[str] = "" #TODO: si può togliere
    advice_who: Optional[str] = "" #TODO: si può togliere
    abroad_experience: str
    erasmus_type: str
    foreign_country: Optional[str] = "" #TODO: si può togliere
    foreign_city: Optional[str] = "" #TODO: si può togliere
    change_degree: str
    change_year: Optional[str] = "" #TODO: si può togliere
    prev_change_uni: Optional[str] = "" #TODO: si può togliere
    prev_change_other_uni: Optional[str] = "" #TODO: si può togliere
    prev_change_department: Optional[str] = "" #TODO: si può togliere
    prev_change_degree_course: Optional[str] = "" #TODO: si può togliere
    change_why: Optional[str] = "" #TODO: si può togliere
    triennial_university: Optional[str] = "" #TODO: si può togliere
    triennial_university_other: Optional[str] = "" #TODO: si può togliere
    triennial_department: Optional[str] = "" #TODO: si può togliere
    triennial_course_degree: Optional[str] = "" #TODO: si può togliere
    triennial_subject_area: Optional[str] = "" #TODO: si può togliere
    triennial_enrolment_year: Optional[str] = "" #TODO: si può togliere
    triennial_end_year: Optional[str] = "" #TODO: si può togliere
    triennial_type: Optional[str] = "" #TODO: si può togliere
    triennial_grade: Optional[str] = "" #TODO: si può togliere
    master_choice_related_studies: Optional[str] = "" #TODO: si può togliere
    high_school: str
    other_high_school: str
    main_subject: str
    favorite_subject: str
    baccalaureate: int
    choice_related_studies: str
    work_experience: Optional[str] = "" #TODO: si può togliere
    work_experience_type: Optional[str] = "" #TODO: si può togliere
    work_related_studies: Optional[str] = "" #TODO: si può togliere
    distance_work_graduation: Optional[str] = "" #TODO: solo per laureato
    didactic_quality: int
    teaching_quality: int
    exams_difficulties: int
    subjects_difficulties: int
    environment_quality: int
    students_relationship: int
    laboratories: int
    hobby: str
    dream_job : str
    review : str
    stars: int
    subscription_date: Optional[str] = todayToString()
    subscription_type: str

class PredictResult(BaseModel):
    degree_course_input: str #corso inserito dall'utente
    degree_predict: str #corso che gli abbiamo consigliato
    university_input: str #università inserita
    degree_predict_correct: bool
    difference_between_course: int #quanto è lontano il tuo corso da quello che ti abbiamo consigliato
    choosing_course_if_back: int #se tornassi indietro che scelta faresti
    degree_dream: str #scelta da fare se tornasse indietro
    uni_dream: str
    aiuniversity_is_utils: bool
    start_utilities_aiuniversity: bool
    stars_aiuniversity: int
    review_aiuniversity: str
    subscription_date: Optional[str] = todayToString()

