from .apiClass import  *

@app.get("/getDifficultAspectList/{university}/{course}", tags=["Other"])
async def get_difficult_aspect(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    list = await getDifficultAspectList(input_course, input_uni,  db)
    dbCloseConnection(client)
    return {'result': list}

@app.get("/getCountRedoChoice/{university}/{course}", tags=["Other"])
async def get_count_redo_choice(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    number = await getCountRedoChoice(input_course, input_uni,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfStudentsGoToErasmusByCourse/{university}/{course}", tags=["Other"])
async def get_number_of_students_go_to_erasmus_by_course(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    number = await getNumberOfStudentsGoToErasmusByCourse(input_course, input_uni,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfStudentsGoToErasmusByCourse/{university}", tags=["Other"])
async def get_number_of_students_go_to_erasmus_by_uni(university: str):
    '''Get the average of exame not done given the course and the year'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    number = await getNumberOfStudentsGoToErasmusByCourse(input_uni,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfStudentsChangedThisDegree/{university}/{course}", tags=["Other"])
async def get_number_of_students_changed_this_degree(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course = course.lower()
    input_course = input_course.strip()
    number = await getNumberOfStudentsChangeThisDegree(input_course, input_uni,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/restartCalucatedModel", tags=["Other"])
async def restart_calucated_model():
    '''Recalculated AI Model. Thi api must be used when registraation a new subscriptions'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number = await restartCalucatedModule(db)
    dbCloseConnection(client)
    return {'result': number}




