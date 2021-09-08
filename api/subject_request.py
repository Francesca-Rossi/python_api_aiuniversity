from .apiClass import  *

@app.get("/getAllSubjects/{course}", tags=["Subjects & Exams"])
async def get_all_subject(course: str):
    '''Get all subjects studied in a course'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = course.lower()
    input = input.strip()
    list = await getAllSubject(input, db=db)
    dbCloseConnection(client)
    return {'result': list}

@app.get("/getAllSubjectsByUni/{university}/{course}", tags=["Subjects & Exams"])
async def get_all_subject_by_uni(university: str, course: str):
    '''Get all the subjects of a university'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    list =  await getAllSubjectByUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return {'result': list}

@app.get("/getAllEasyExams/{university}/{course}", tags=["Subjects & Exams"])
async def get_all_easy_exam(university: str, course: str):
    '''Get all easy exams in a course '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    list =  await getAllEasyExam(course_input, uni_input,  db)
    dbCloseConnection(client)
    return {'result': list}

@app.get("/getAllHardExams/{university}/{course}", tags=["Subjects & Exams"])
async def get_all_hard_exam(university: str, course: str):
    '''Get all hard exams in a course '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    list =  await getAllDifficultExam(course_input, uni_input,  db)
    dbCloseConnection(client)
    return {'result': list}