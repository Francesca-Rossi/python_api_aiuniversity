# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''from request import *
from model import  *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    scuola_superiore = "Liceo Artistico"  # @param ["Liceo Scientifico", "Istituto tecnico Industriale", "Liceo Classico", "Istituto tecnico economico", "Liceo delle scienze umane"]
    materie_studiate = "Storia, Itaiano, Filosofia, Storia dell'arte, Disegno"  # @param {type:"string"}
    materie_preferite = "Disegno, Storia dell'arte"  # @param {type:"string"}
    hobby = "sport, musica, guardare film, disegnare, leggere fumetti, teatro"  # @param {type:"string"}
    lavoro_sognato = "attore"  # @param {type:"string"}
    aspettative_universita = "Mi piacerebbe migliorare le mie conoscenze artistiche e teatrali, approfondendo in particolare il lato storico"  # @param {type:"string"}
    motivo_scelta_universita = "spero mi possa aiutare per intraprendere una carriera artistica e culturale"  # @param {type:"string"}
    continuare_studi_precedenti = "SI"  # @param ["SI", "NO"]
    predict_request(scuola_superiore,materie_studiate,materie_preferite,hobby,lavoro_sognato,aspettative_universita,motivo_scelta_universita,continuare_studi_precedenti)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/'''
from fastapi import FastAPI,  HTTPException
from pydantic import BaseModel
from request import predict_request


app = FastAPI()

# pydantic models


class StockIn(BaseModel):
    high_school: str
    main_subject: str
    prefered_subject: str
    hobby: str
    dream_work: str
    uni_aspectations: str
    uni_decision_choice: str
    continuous_previous_study: str




class StockOut(StockIn):
    degree_predict: dict

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
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
    response_object =\
        {"high_school": high_school,
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