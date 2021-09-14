from .apiClass import  *
from ai_model.request import predict_request

@app.post("/predict", status_code=200, tags=["Add"])
async def prediction_degree(payload: UserInfo):
    '''This api allow to predict a degree course and save the result on the database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info= UserInfo(**dictionary)
        prediction= await predict_request(user_info.high_school, user_info.main_subject, user_info.prefered_subject, user_info.hobby, user_info.dream_work, user_info.uni_aspectations, user_info.uni_decision_choice, user_info.continuous_previous_study )
        if not prediction:
            raise HTTPException(status_code=400, detail="Model not found.")
        dict_info=user_info.dict()
        dict_info['degree_predict']= prediction
        result = await AddNewAdvice(dict_info, DB)
        return {'result': prediction}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.post("/addNewSubscriptions", response_model= BoolResult, status_code=200, tags=["Add"])
async def add_new_subscription(payload: SubscriptionInfo):
    '''Add a form answers to database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info_dict=SubscriptionInfo(** dictionary)
        
        result=await addNewSubscriptions(user_info_dict.dict(), DB)
        

        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.post("/addNewStudent", response_model= BoolResult, status_code=200,  tags=["Add"])
async def add_new_students(payload: SubscriptionInfo):
    '''Add a students answers to database'''
    try:
        dictionary = payload.dict()

        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info_dict=SubscriptionInfo(** dictionary)
        
        result= await addNewStudent(user_info_dict.dict(), DB)
        
        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.post("/addNewGraduate", response_model= BoolResult, status_code=200,  tags=["Add"] )
async def add_new_graduate(payload: SubscriptionInfo):
    '''Add a degree answers to database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        user_info_dict=SubscriptionInfo(** dictionary)
        print(user_info_dict.dict())
        
        result= await addNewGraduate(user_info_dict.dict(), DB)
        
        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")


@app.post("/addPredictReview", response_model= BoolResult, status_code=200,  tags=["Add"])
async def add_predict_review(payload: PredictResult):
    '''Add feedback for a specific predict on database'''
    try:
        dictionary = payload.dict()
        for key in dictionary.keys():
            if type(dictionary[key]) is str:
                dictionary[key] = dictionary[key].lower()
                dictionary[key] = dictionary[key].strip()
        predict_dict=PredictResult(** dictionary)
        
        result= await addReviewOfMachineLearning(predict_dict.dict(), DB)
        
        response_object = {"result": result}
        return response_object
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
