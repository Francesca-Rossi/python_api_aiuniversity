from .apiClass import  *

@app.get("/getNumberOfPeopleByCourseAndUni/{university}/{course}", tags=["Number of subscriptions"])
async def get_people_by_uni_and_course(university: str, course: str):
    '''How many people there are in a course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfPeopleByCourseAndUni(course_input, uni_input,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleByCourse/{course}", tags=["Number of subscriptions"])
async def get_people_by_course( course: str):
    '''How many people study in this course? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    course_input = course.lower()
    course_input = course_input.strip()
    number =  await getNumberOfPeopleByCourse(course_input,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleByUni/{university}", tags=["Number of subscriptions"])
async def get_people_by_uni(university: str):
    '''How many people there are in a university? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfPeopleByUNi(uni_input,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleWithSameProvinceOfUni/{university}", tags=["Number of subscriptions"])
async def get_people_whit_same_province_of_uni(university: str):
    '''How many people there are in a province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfPeopleWhitSameProvinceOfUni(uni_input,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleWithSameRegionOfUni/{university}", tags=["Number of subscriptions"])
async def get_people_whit_same_region_of_uni(university: str):
    '''How many people there are in a region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    uni_input = university.lower()
    uni_input = uni_input.strip()
    number =  await getNumberOfPeopleWhitSameRegionOfUni(uni_input,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleByRegion/{region}", tags=["Number of subscriptions"])
async def get_people_by_region(region: str):
    '''How many people there are in a region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    number =  await getNumberOfPeopleByRegion(input,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleGroupbyRegion", tags=["Number of subscriptions"])
async def get_people_groupby_region():
    '''How many people there are in all regions? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleGroupbyRegion(db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleStudyatHomeRegion", tags=["Number of subscriptions"])
async def get_people_study_at_home_region():
    '''How many people study at the home region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleStudyatHomeRegion(db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleStudyOutsideRegion", tags=["Number of subscriptions"])
async def get_people_study_outside_region():
    '''How many people study outside the region? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleStudyOutsideRegion(db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleByProvince/{province}", tags=["Number of subscriptions"])
async def get_people_by_province(province: str):
    '''How many people there are in a province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    number =  await getNumberOfPeopleByProvince(input,  db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleGroupbyProvince/{province}", tags=["Number of subscriptions"])
async def get_people_groupby_province(province: str):
    '''How many people there are in all provinces? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    list =  await getNumberOfPeopleGroupbyProvince(input,  db)
    dbCloseConnection(client)
    return {'result': list}

@app.get("/getNumberOfPeopleStudyatHomeProvince", tags=["Number of subscriptions"])
async def get_people_study_at_home_province():
    '''How many people study at the home province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number =  await getNumberOfPeopleStudyatHomeProvince(db)
    dbCloseConnection(client)
    return {'result': number}

@app.get("/getNumberOfPeopleStudyOutsideProvince", tags=["Number of subscriptions"])
async def get_people_study_outside_province():
    '''How many people study outside the province? '''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    number = await getNumberOfPeopleStudyOutsideProvince(db)
    dbCloseConnection(client)
    return {'result': number}
