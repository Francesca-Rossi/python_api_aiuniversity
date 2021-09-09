from .apiClass import  *
from request import predict_request

@app.post("/predict", response_model= DegreeResult, status_code=200)
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

    prediction_list= await predict_request(high_school, main_subject, prefered_subject, hobby, dream_work, uni_aspectations, uni_decision_choice, continuous_previous_study )

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
    result=await addNewSubscriptions(user_info_dict.dict(), db)
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
    result= await addNewStudent(user_info_dict.dict(), db)
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
    result= await addNewGraduate(user_info_dict.dict(), db)
    dbCloseConnection(client)
    response_object = {"result": result}
    return response_object


@app.post("/AddPredictReview", response_model= BoolResult, status_code=200)
async def add_predict_review(payload: PredictResult):
    '''Aggiunta di un laureato al database'''
    predict_dict=PredictResult(** payload.dict())

    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    result= await addReviewOfMachineLearning(predict_dict.dict(), db)
    dbCloseConnection(client)

    response_object = {"result": result}
    return response_object
