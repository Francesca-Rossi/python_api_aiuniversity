from .apiClass import  *
from request import predict_request

@app.post("/predict", response_model= DegreeResult, status_code=200)
async def prediction_degree(payload: UserInfo):
    '''api per prevedere una laurea dato le informazioni in ingresso ( da usare sia per studenti superiori sia come check per gli studenti universitari)'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info= UserInfo(**dictionary)
        prediction_list= await predict_request(user_info.high_school, user_info.main_subject, user_info.prefered_subject, user_info.hobby, user_info.dream_work, user_info.uni_aspectations, user_info.uni_decision_choice, user_info.continuous_previous_study )
        if not prediction_list:
            raise HTTPException(status_code=400, detail="Model not found.")
        response_object = {"high_school": user_info.high_school,
             "main_subject": user_info.main_subject,
             "prefered_subject": user_info.prefered_subject,
             "hobby": user_info.hobby,
             "dream_work": user_info.dream_work,
             "uni_aspectations": user_info.uni_aspectations,
             "uni_decision_choice": user_info.uni_decision_choice,
             "continuous_previous_study": user_info.continuous_previous_study,
             "degree_predict": prediction_list
             }
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.post("/addNewSubscriptions", response_model= BoolResult, status_code=200)
async def add_new_subscription(payload: SubscriptionInfo):
    '''Aggiunta di una compilazione al database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info_dict=SubscriptionInfo(** dictionary)
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        result=await addNewSubscriptions(user_info_dict.dict(), db)
        dbCloseConnection(client)

        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.post("/addNewStudent", response_model= BoolResult, status_code=200)
async def add_new_students(payload: SubscriptionInfo):
    '''Aggiunta di uno studente al database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info_dict=SubscriptionInfo(** dictionary)
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        result= await addNewStudent(user_info_dict.dict(), db)
        dbCloseConnection(client)
        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.post("/AddNewGraduate", response_model= BoolResult, status_code=200)
async def add_new_graduate(payload: SubscriptionInfo):
    '''Aggiunta di un laureato al database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info_dict=SubscriptionInfo(** dictionary)
        print(user_info_dict.dict())
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        result= await addNewGraduate(user_info_dict.dict(), db)
        dbCloseConnection(client)
        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")


@app.post("/AddPredictReview", response_model= BoolResult, status_code=200)
async def add_predict_review(payload: PredictResult):
    '''Aggiunta di un laureato al database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        predict_dict=PredictResult(** dictionary)
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        result= await addReviewOfMachineLearning(predict_dict.dict(), db)
        dbCloseConnection(client)
        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
