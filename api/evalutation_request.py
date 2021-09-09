from .apiClass import  *

@app.get("/getDidacticQualityAverangebyCourse/{university}/{course}", tags=["Evalutations"])
async def get_didatic_quality_average(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getDidacticQualityAverangebyCourse(input_course, input_uni,  db)
        dbCloseConnection(client)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getTeachingQualityAverangebyCourse/{university}/{course}", tags=["Evalutations"])
async def get_teaching_quality_average(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getTeachingQualityAverangebyCourse(input_course, input_uni,  db)
        dbCloseConnection(client)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getExamsDifficultAverangebyCourse/{university}/{course}", tags=["Evalutations"])
async def get_exams_difficult_average(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getExamDifficultAverangebyCourse(input_course, input_uni,  db)
        dbCloseConnection(client)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getSubjectsDifficultAverangebyCourse/{university}/{course}", tags=["Evalutations"])
async def get_subjects_difficult_average(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getSubjectsDifficultAverangebyCourse(input_course, input_uni,  db)
        dbCloseConnection(client)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getEnviromentalQualityAverangebyCourse/{university}/{course}", tags=["Evalutations"])
async def get_enviromental_quality_average(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getEnviromentalQualityAverangebyCourse(input_course, input_uni,  db)
        dbCloseConnection(client)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getStudentsRelationshipAverangebyCourse/{university}/{course}", tags=["Evalutations"])
async def get_students_relationship_average(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getStudentsRelationshipAverangebyCourse(input_course, input_uni,  db)
        dbCloseConnection(client)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getLaboratoryAverangebyCourse/{university}/{course}", tags=["Evalutations"])
async def get_laboratory_average(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        number = await getLaboratoryAverangebyCourse(input_course, input_uni,  db)
        dbCloseConnection(client)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")