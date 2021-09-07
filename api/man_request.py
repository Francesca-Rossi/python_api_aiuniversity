from .apiClass import  *

@app.get("/getNumberOfMenByCourseAndUni", tags=["Number of men"])
async def get_men_by_uni_and_course(university: str, course: str):
    '''How many men there are in a course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfManByCourseAndUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenByCourse", tags=["Number of men"])
async def get_men_by_course( course: str):
    '''How many men study in this course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfManByCourse(course_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenByUni", tags=["Number of men"])
async def get_men_by_uni(university: str):
    '''How many men there are in a university? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfManByUNi(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenWithSameProvinceOfUni", tags=["Number of men"])
async def get_men_whit_same_province_of_uni(university: str):
    '''How many men there are in a province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfManWhitSameProvinceOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenWithSameRegionOfUni", tags=["Number of men"])
async def get_men_whit_same_region_of_uni(university: str):
    '''How many men there are in a region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfManWhitSameRegionOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenByRegion", tags=["Number of men"])
async def get_men_by_region(region: str):
    '''How many men there are in a region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    number =  await getNumberOfManByRegion(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenGroupbyRegion", tags=["Number of men"])
async def get_men_groupby_region():
    '''How many men there are in all regions? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManGroupbyRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenStudyatHomeRegion", tags=["Number of men"])
async def get_men_study_at_home_region():
    '''How many men study at the home region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManStudyatHomeRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenStudyOutsideRegion", tags=["Number of men"])
async def get_men_study_outside_region():
    '''How many men study outside the region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManStudyOutsideRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenByProvince", tags=["Number of men"])
async def get_men_by_province(province: str):
    '''How many men there are in a province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfManByProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenGroupbyProvince", tags=["Number of men"])
async def get_men_groupby_province(province: str):
    '''How many men there are in all provinces? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfManGroupbyProvince(input, db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenStudyatHomeProvince", tags=["Number of men"])
async def get_men_study_at_home_province():
    '''How many men study at the home province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfManStudyatHomeProvince(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfMenStudyOutsideProvince", tags=["Number of men"])
async def get_men_study_outside_province():
    '''How many men study outside the province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number = await getNumberOfManStudyOutsideProvince(db)
    dbCloseConnection(client)
    return number
