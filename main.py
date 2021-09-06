# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI,  HTTPException, routing
from api.apiClass import  *
from request import predict_request
from recovery_data import *
from db.db_operations import  *
from datetime import date


app = FastAPI()


# pydantic models



@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.get("/getAllUni")
async def get_all_uni():
    '''Get all the university present in the db'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    list = await getAllUni(db)
    dbCloseConnection(client)
    return list

@app.get("/getAllUniByCourse")
async def get_all_uni_by_course(course: str):
    '''Get all the university by course'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input= course.lower()
    input = input.strip()
    list = await getAllUnByCourse(input, db)
    dbCloseConnection(client)
    return list

@app.get("/getAllUniByRegion")
async def get_all_uni_by_region(region: str):
    '''Get all the university by region'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    list = await getAllUniByRegion(input, db)
    dbCloseConnection(client)
    return list

@app.get("/getAllUniByProvince")
async def get_all_uni_by_province(province: str):
    '''Get all the university by region'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    list = await getAllUniByProvince(input, db)
    dbCloseConnection(client)
    return list

@app.get("/getAllCourse")
async def get_all_course():
    '''Get all italian course in the DB'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    list = await getAllCourse(db)
    dbCloseConnection(client)
    return list

@app.get("/getAllCourseByUni")
async def get_all_course_by_uni(university: str):
    '''Get all the course given a university'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = university.lower()
    input = input.strip()
    list =  await getAllCourseByUni(input, db)
    dbCloseConnection(client)
    return list

@app.get("/getAllRegion")
async def get_all_region():
    '''Get all the region from the db'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    list =  await getAllRegion(db)
    dbCloseConnection(client)
    return list

@app.get("/getRegionByUni")
async def get_region_by_uni(university: str):
    '''Get all the region from the db'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = university.lower()
    input = input.strip()
    list =  await getRegionByUni(input, db)
    dbCloseConnection(client)
    return list


@app.get("/predict", response_model= DegreeResult, status_code=200)
async def prediction_degree(payload: UserInfo):
    '''api per prevedere una laurea dato le informazioni in ingresso ( da usare sia per studenti superiori sia come check per gli studenti universitari)'''
    #TODO: Questo codice si può migliorare
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

@app.post("/addNewSubscriptions", response_model= BoolResult, status_code=200)
async def add_new_subscription(payload: SubscriptionInfo):
    '''Aggiunta di una compilazione al database'''
    user_info_dict=SubscriptionInfo(** payload.dict())
    print(user_info_dict.dict())

    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    result= addNewSubscriptions(user_info_dict.dict(), db)
    dbCloseConnection(client)

    response_object = {"result": result}
    return response_object

@app.post("/addNewStudent", response_model= BoolResult, status_code=200)
async def add_new_students(payload: SubscriptionInfo):
    '''Aggiunta di uno studente al database'''
    user_info_dict=SubscriptionInfo(** payload.dict())
    print(user_info_dict.dict())

    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    result= addNewStudent(user_info_dict.dict(), db)
    dbCloseConnection(client)

    response_object = {"result": result}
    return response_object

@app.post("/AddNewGraduate", response_model= BoolResult, status_code=200)
async def add_new_graduate(payload: SubscriptionInfo):
    '''Aggiunta di un laureato al database'''
    user_info_dict=SubscriptionInfo(** payload.dict())
    print(user_info_dict.dict())

    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    result= addNewGraduate(user_info_dict.dict(), db)
    dbCloseConnection(client)

    response_object = {"result": result}
    return response_object




if __name__ == '__main__':
    #TODO: INSERIRE EMAIL/ CODICE IDENTIFICATIVO UUID PER NUOVE SOTTOSCRIZIONI DI UTENTI REGISTRATI
    client=dbOpenConnection()
    db = client.get_database("ai_university_db")
    #getSubscriptionByDate('05-09-2021', db)
    dbCloseConnection(client)

    '''# inserisco di nuovo tutto nel dataset
    today=date.today()
    date_today =  today.strftime("%d-%m-%Y")
    df_graduate = get_graduate_original_data()
    df_graduate_first_degree = df_graduate.query(query_first_degree)
    df_graduate_lower = df_graduate_first_degree.applymap(lambda s: s.lower() if type(s) == str else s)
    df_graduate_lower = df_graduate_first_degree.applymap(lambda s: s.strip() if type(s) == str else s)
    df_graduate_lower = df_graduate_lower.reset_index()
    df_graduate_lower = df_graduate_lower.iloc[:, 1:]
    df_graduate_lower['subscription_date'] = date_today
    for i in df_graduate_lower.index:
        df = df_graduate_lower.iloc[i]
        addNewGraduate(df.to_dict(), db)
        df['subscription_type'] = 'graduate'
        addNewSubscriptions(df.to_dict(), db)
        print(df.to_dict())
    df_students = get_students_original_data()
    df_students_first_degree = df_students.query(query_first_degree)
    df_students_lower = df_students_first_degree.applymap(lambda s: s.lower() if type(s) == str else s)
    df_students_lower = df_students_first_degree.applymap(lambda s: s.strip() if type(s) == str else s)
    df_students_lower = df_students_lower.reset_index()
    df_students_lower = df_students_lower.iloc[:, 1:]
    df_students_lower['subscription_date'] = date_today
    for i in df_students_lower.index:
        df = df_students_lower.iloc[i]
        addNewStudent(df.to_dict(), db)
        df['subscription_type'] = 'student'
        addNewSubscriptions(df.to_dict(), db)
        print(df.to_dict())'''