from .apiClass import  *

@app.get("/getMarkAveragebyCourse/{university}/{course}", tags=["Mark"])
async def get_mark_average_by_course(university: str, course: str):
    '''Get the average of the marks given the course'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    avg = await getMarkAveragebyCourse(input_course, input_uni, db)
    dbCloseConnection(client)
    return avg

@app.get("/getMarkAveragebyCourseAndYear/{university}/{course}/{year_of_course}", tags=["Mark"])
async def get_mark_average_by_course_and_year(university: str, course: str, year_of_course: int):
    '''Get the average of the marks given the course and the year'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    avg = await getMarkAveragebyCourseAndYear(input_course, input_uni, year_of_course,  db)
    dbCloseConnection(client)
    return {'result': avg}

@app.get("/getGradeAveragebyCourse/{university}/{course}", tags=["Grade"])
async def get_grade_average_by_course(university: str, course: str):
    '''Get the average of the grade given the course'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    avg = await getGradeAveragebyCourse(input_course, input_uni, db)
    dbCloseConnection(client)
    return {'result': avg}

@app.get("/getDurationAveragebyCourse/{university}/{course}", tags=["Duration"])
async def get_duratiion_average_by_course(university: str, course: str):
    '''Get the average of the duration given the course'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    avg = await getDurationAveragebyCourse(input_course, input_uni, db)
    dbCloseConnection(client)
    return {'result': avg}

@app.get("/getExamNotDoneAveragebyCourseAndYear/{university}/{course}/{year_of_course}", tags=["Subjects & Exams"])
async def get_exam_not_done_by_course_and_year(university: str, course: str, year_of_course:int ):
    '''Get the average of exame not done given the course and the year'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input_uni = university.lower()
    input_uni = input_uni.strip()
    input_course=course.lower()
    input_course = input_course.strip()
    avg = await getExamNotDoneAveragebyCourseAndYear(input_course, input_uni, year_of_course, db)
    dbCloseConnection(client)
    return {'result': avg}



