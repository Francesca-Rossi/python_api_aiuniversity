from .apiClass import  *

@app.get("/getNumberOfWomenByCourseAndUni", tags=["Number of women"])
async def get_women_by_uni_and_course(university: str, course: str):
    '''How many women there are in a course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfWomanByCourseAndUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenByCourse", tags=["Number of women"])
async def get_women_by_course( course: str):
    '''How many women study in this course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfWomanByCourse(course_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenByUni", tags=["Number of women"])
async def get_women_by_uni(university: str):
    '''How many women there are in a university? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfWomanByUNi(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenWithSameProvinceOfUni", tags=["Number of women"])
async def get_women_whit_same_province_of_uni(university: str):
    '''How many women study in the same province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfWomanWhitSameProvinceOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenWithSameRegionOfUni", tags=["Number of women"])
async def get_women_whit_same_region_of_uni(university: str):
    '''How many women study at the same region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfWomanWhitSameRegionOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenByRegion", tags=["Number of women"])
async def get_women_by_region(region: str):
    '''How many women are in a region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    number =  await getNumberOfWomanByRegion(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenGroupbyRegion", tags=["Number of women"])
async def get_women_groupby_region():
    '''How many women are in all regions? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanGroupbyRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenStudyatHomeRegion", tags=["Number of women"])
async def get_women_study_at_home_region():
    '''How many women study at the home region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanStudyatHomeRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenStudyOutsideRegion", tags=["Number of women"])
async def get_women_study_outside_region():
    '''How many women study outside the region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanStudyOutsideRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenByProvince", tags=["Number of women"])
async def get_women_by_province(province: str):
    '''How many women study in a province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfWomanByProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenGroupbyProvince", tags=["Number of women"])
async def get_women_groupby_province(province: str):
    '''How many women study in all provinces? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfWomanGroupbyProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenStudyatHomeProvince", tags=["Number of women"])
async def get_women_study_at_home_province():
    '''How many women study at the home province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfWomanStudyatHomeProvince(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfWomenStudyOutsideProvince", tags=["Number of women"])
async def get_women_study_outside_province():
    '''How many women study outside the province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number = await getNumberOfWomanStudyOutsideProvince(db)
    dbCloseConnection(client)
    return number
