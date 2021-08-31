# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI,  HTTPException
from api import apiClass
from request import predict_request
from db.db_operations import  *


app = FastAPI()

# pydantic models



@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.post("/predict", response_model= apiClass.DegreeResult, status_code=200)
async def get_prediction(payload: apiClass.UserInfo):
    '''api per prevedere una laurea dato le informazioni in ingresso ( da usare sia per studenti superiori sia come check per gli studenti universitari)'''
    high_school = payload.high_school
    main_subject = payload.main_subject
    prefered_subject = payload.prefered_subject
    hobby = payload.hobby
    dream_work = payload.dream_work
    uni_aspectations = payload.uni_aspectations
    uni_decision_choice = payload.uni_decision_choice
    continuous_previous_study = payload.continuous_previous_study

    prediction_list= predict_request(high_school, main_subject, prefered_subject, hobby, dream_work, uni_aspectations, uni_decision_choice, continuous_previous_study )

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")
    response_object = {"high_school": high_school,
         "main_subject": main_subject,
         "prefered_subject": prefered_subject,
         "hobby": hobby,
         "dream_work": dream_work,
         "uni_aspectations": uni_aspectations,
         "uni_decision_choice": uni_decision_choice,
         "continuous_previous_study": continuous_previous_study,
         "degree_predict": prediction_list
         }
    return response_object

if __name__ == '__main__':
    client=dbOpenConnection()
    db = client.get_database("ai_university_db")
    getAllStudents(db)
    dbCloseConnection(client)