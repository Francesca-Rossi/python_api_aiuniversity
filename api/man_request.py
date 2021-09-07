from .apiClass import  *

@app.get("/getNumberOfManByCourseAndUni", tags=["Number of men"])
async def get_man_by_uni_and_course(university: str, course: str):
    '''How many man there are in a course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfManByCourseAndUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManByCourse", tags=["Number of men"])
async def get_man_by_course( course: str):
    '''How many man there study this course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfManByCourse(course_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManByUni", tags=["Number of men"])
async def get_man_by_uni(university: str):
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfManByUNi(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManWhitSameProvinceOfUni", tags=["Number of men"])
async def get_man_whit_same_province_of_uni(university: str):
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfManWhitSameProvinceOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManWhitSameRegionOfUni", tags=["Number of men"])
async def get_man_whit_same_region_of_uni(university: str):
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfManWhitSameRegionOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManByRegion", tags=["Number of men"])
async def get_man_by_region(region: str):
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    number =  await getNumberOfManByRegion(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManGroupbyRegion", tags=["Number of men"])
async def get_man_groupby_region():
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManGroupbyRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManStudyatHomeRegion", tags=["Number of men"])
async def get_man_study_at_home_region():
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManStudyatHomeRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManStudyOutsideRegion", tags=["Number of men"])
async def get_man_study_outside_region():
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManStudyOutsideRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManByProvince", tags=["Number of men"])
async def get_man_by_province(province: str):
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfManByProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManGroupbyProvince", tags=["Number of men"])
async def get_man_groupby_province(province: str):
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfManGroupbyProvince(input, db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManStudyatHomeProvince", tags=["Number of men"])
async def get_man_study_at_home_province():
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManStudyatHomeProvince(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfManStudyOutsideProvince", tags=["Number of men"])
async def get_man_study_outside_province():
    '''How many man there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number = await getNumberOfManStudyOutsideProvince(db)
    dbCloseConnection(client)
    return number
