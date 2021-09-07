from .apiClass import  *

@app.get("/getNumberOfPeopleByCourseAndUni", tags=["Number of subscriptions"])
async def get_people_by_uni_and_course(university: str, course: str):
    '''How peopley people there are in a course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfPeopleByCourseAndUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleByCourse", tags=["Number of subscriptions"])
async def get_people_by_course( course: str):
    '''How peopley people there study this course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfPeopleByCourse(course_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleByUni", tags=["Number of subscriptions"])
async def get_people_by_uni(university: str):
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfPeopleByUNi(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleWhitSameProvinceOfUni", tags=["Number of subscriptions"])
async def get_people_whit_same_province_of_uni(university: str):
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfPeopleWhitSameProvinceOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleWhitSameRegionOfUni", tags=["Number of subscriptions"])
async def get_people_whit_same_region_of_uni(university: str):
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfPeopleWhitSameRegionOfUni(uni_input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleByRegion", tags=["Number of subscriptions"])
async def get_people_by_region(region: str):
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    number =  await getNumberOfPeopleByRegion(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleGroupbyRegion", tags=["Number of subscriptions"])
async def get_people_groupby_region():
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleGroupbyRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleStudyatHomeRegion", tags=["Number of subscriptions"])
async def get_people_study_at_home_region():
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleStudyatHomeRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleStudyOutsideRegion", tags=["Number of subscriptions"])
async def get_people_study_outside_region():
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleStudyOutsideRegion(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleByProvince", tags=["Number of subscriptions"])
async def get_people_by_province(province: str):
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfPeopleByProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleGroupbyProvince", tags=["Number of subscriptions"])
async def get_people_groupby_province(province: str):
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfPeopleGroupbyProvince(input,  db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleStudyatHomeProvince", tags=["Number of subscriptions"])
async def get_people_study_at_home_province():
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleStudyatHomeProvince(db)
    dbCloseConnection(client)
    return number

@app.get("/getNumberOfPeopleStudyOutsideProvince", tags=["Number of subscriptions"])
async def get_people_study_outside_province():
    '''How peopley people there are in a uni? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number = await getNumberOfPeopleStudyOutsideProvince(db)
    dbCloseConnection(client)
    return number
