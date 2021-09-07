from .apiClass import  *

@app.get("/getAllCourse", tags=["Degree courses"])
async def get_all_course():
    '''Get all italian course in the DB'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    list = await getAllCourse(db)
    dbCloseConnection(client)
    return list

@app.get("/getAllCourseByUni", tags=["Degree courses"])
async def get_all_course_by_uni(university: str):
    '''Get all the course given a university'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = university.lower()
    input = input.strip()
    list =  await getAllCourseByUni(input, db)
    dbCloseConnection(client)
    return list