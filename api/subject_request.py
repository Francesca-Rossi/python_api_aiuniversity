from .apiClass import  *

@app.get("/getAllSubject", tags=["Subjects & Exams"])
async def get_all_subject(course: str):
    '''Get all subjects study in a course'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = course.lower()
    input = input.strip()
    list = await getAllSubject(input, db=db)
    dbCloseConnection(client)
    return list

@app.get("/getAllSubjectByUni", tags=["Subjects & Exams"])
async def get_all_subject_by_uni(university: str, course: str):
    '''Get all the province given a uni'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    list =  await getAllSubjectByUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return list

@app.get("/getAllEasyExam", tags=["Subjects & Exams"])
async def get_all_easy_exam(university: str, course: str):
    '''Get all easy exam in a course '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    list =  await getAllEasyExam(course_input, uni_input,  db)
    dbCloseConnection(client)
    return list

@app.get("/getAllHardExam", tags=["Subjects & Exams"])
async def get_all_hard_exam(university: str, course: str):
    '''Get all easy exam in a course '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    list =  await getAllDifficultExam(course_input, uni_input,  db)
    dbCloseConnection(client)
    return list