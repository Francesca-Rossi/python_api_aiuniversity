from .apiClass import  *

@app.get("/getDifficultAspectList/{university}/{course}", tags=["Other"])
async def get_difficult_aspect(university: str, course: str):
    '''Return the list of difficulty aspects given the degree course'''
    try:
       
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        list = await getDifficultAspectList(input_course, input_uni,  DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getCountRedoChoice/{university}/{course}", tags=["Other"])
async def get_count_redo_choice(university: str, course: str):
    '''Return the students who would redo this degree course'''
    try:
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getCountRedoChoice(input_course, input_uni,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfStudentsGoToErasmusByCourse/{university}/{course}", tags=["Other"])
async def get_number_of_students_go_to_erasmus_by_course(university: str, course: str):
    '''Return the  number of students went to erasmus,  given the degree course'''
    try:
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getNumberOfStudentsGoToErasmusByCourse(input_course, input_uni,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfStudentsGoToErasmusByUni/{university}", tags=["Other"])
async def get_number_of_students_go_to_erasmus_by_uni(university: str):
    '''Return the  number of students went to erasmus,  given the course and the year attended'''
    try: 
        input_uni = university.lower()
        input_uni = input_uni.strip()
        number = await getNumberOfStudentsGoToErasmusByUni(input_uni,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfStudentsChangedThisDegree/{university}/{course}", tags=["Other"])
async def get_number_of_students_changed_this_degree(university: str, course: str):
    '''Return the number of students changed degree course, given the degree course and the year attended'''
    try:
       
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course = course.lower()
        input_course = input_course.strip()
        number = await getNumberOfStudentsChangeThisDegree(input_course, input_uni,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/restartCalucatedModel", tags=["Other"])
async def restart_calucated_model():
    '''Restart mechanism of AI Model. Thi api should  be used when registraation a new subscriptions'''
    try:
        number = await restartCalucatedModule(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")




