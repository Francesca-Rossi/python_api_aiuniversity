from .apiClass import  *

@app.get("/getNumberOfWomanByCourseAndUni", tags=["Number of women"])
async def get_woman_by_uni_and_course(university: str, course: str):
    '''How womany woman there are in a course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfWomanByCourseAndUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanByCourse", tags=["Number of women"])
async def get_woman_by_course( course: str):
    '''How womany woman there study this course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfWomanByCourse(course_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanByUni", tags=["Number of women"])
async def get_woman_by_uni(university: str):
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfWomanByUNi(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanWhitSameProvinceOfUni", tags=["Number of women"])
async def get_woman_whit_same_province_of_uni(university: str):
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfWomanWhitSameProvinceOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanWhitSameRegionOfUni", tags=["Number of women"])
async def get_woman_whit_same_region_of_uni(university: str):
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfWomanWhitSameRegionOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanByRegion", tags=["Number of women"])
async def get_woman_by_region(region: str):
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    number =  await getNumberOfWomanByRegion(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanGroupbyRegion", tags=["Number of women"])
async def get_woman_groupby_region():
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanGroupbyRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanStudyatHomeRegion", tags=["Number of women"])
async def get_woman_study_at_home_region():
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanStudyatHomeRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanStudyOutsideRegion", tags=["Number of women"])
async def get_woman_study_outside_region():
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanStudyOutsideRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanByProvince", tags=["Number of women"])
async def get_woman_by_province(province: str):
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfWomanByProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanGroupbyProvince", tags=["Number of women"])
async def get_woman_groupby_province(province: str):
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfWomanGroupbyProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanStudyatHomeProvince", tags=["Number of women"])
async def get_woman_study_at_home_province():
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanStudyatHomeProvince(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomanStudyOutsideProvince", tags=["Number of women"])
async def get_woman_study_outside_province():
    '''How womany woman there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number = await getNumberOfWomanStudyOutsideProvince(db)
    dbCloseConnection(client)
    return number
