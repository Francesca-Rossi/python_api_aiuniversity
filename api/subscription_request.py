from .apiClass import  *

@app.get("/getNumberOfPeopleByCourseAndUni/{university}/{course}", tags=["Number of subscriptions"])
async def get_people_by_uni_and_course(university: str, course: str):
    '''Return the number of people that attend a specific degree course of an university'''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        course_input = course.lower()
        course_input = course_input.strip()
        number =  await getNumberOfPeopleByCourseAndUni(course_input, uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleByCourse/{course}", tags=["Number of subscriptions"])
async def get_people_by_course( course: str):
    try:
        '''Return the number of people that attend a specific degree course '''

        course_input = course.lower()
        course_input = course_input.strip()
        number =  await getNumberOfPeopleByCourse(course_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleByUni/{university}", tags=["Number of subscriptions"])
async def get_people_by_uni(university: str):
    '''Return the number of people that attend a specific university '''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfPeopleByUNi(uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleWithSameProvinceOfUni/{university}", tags=["Number of subscriptions"])
async def get_people_whit_same_province_of_uni(university: str):
    '''Return the number of students that have the same province of the university'''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfPeopleWhitSameProvinceOfUni(uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleWithSameRegionOfUni/{university}", tags=["Number of subscriptions"])
async def get_people_whit_same_region_of_uni(university: str):
    '''Return the number of students that have the same region of the university '''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfPeopleWhitSameRegionOfUni(uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleByRegion/{region}", tags=["Number of subscriptions"])
async def get_people_by_region(region: str):
    '''Return the number of students living  in a specific region '''
    try:
        
        input = region.lower()
        input = input.strip()
        number =  await getNumberOfPeopleByRegion(input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleGroupbyRegion", tags=["Number of subscriptions"])
async def get_people_groupby_region():
    '''Return the number of students group by their living region '''
    try:
        
        number =  await getNumberOfPeopleGroupbyRegion(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleStudyatHomeRegion", tags=["Number of subscriptions"])
async def get_people_study_at_home_region():
    '''Return the number of students that study in their living region '''
    try:
        
        number =  await getNumberOfPeopleStudyatHomeRegion(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleStudyOutsideRegion", tags=["Number of subscriptions"])
async def get_people_study_outside_region():
    '''Return the number that study outside their living region  '''
    try:
        
        number =  await getNumberOfPeopleStudyOutsideRegion(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleByProvince/{province}", tags=["Number of subscriptions"])
async def get_people_by_province(province: str):
    '''Return the number of students living  in a specific province'''
    try:
        
        input = province.lower()
        input = input.strip()
        number =  await getNumberOfPeopleByProvince(input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleGroupbyProvince", tags=["Number of subscriptions"])
async def get_people_groupby_province():
    '''Return the number of students by their living province'''
    try:
        
        list =  await getNumberOfPeopleGroupbyProvince( DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleStudyatHomeProvince", tags=["Number of subscriptions"])
async def get_people_study_at_home_province():
    '''Return the number of students that study in their living province  '''
    try:
        
        number =  await getNumberOfPeopleStudyatHomeProvince(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfPeopleStudyOutsideProvince", tags=["Number of subscriptions"])
async def get_people_study_outside_province():
    '''Return the number of students that study outside their living region '''
    try:
        
        number = await getNumberOfPeopleStudyOutsideProvince(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getDateOfLastSubscription", tags=["Subscriptions"])
async def get_date_of_last_subscription():
    '''Return date of  the last students exeperience registered '''
    try:
        
        date = await getDateOfLastSubscription(DB)
        
        return {'result': date}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getSubscriptionsByDate", tags=["Subscriptions"])
async def get_subscriptions_by_date():
    '''Return a students exeperience by date '''
    try:
        
        date = await getSubscriptionsByDate(DB)
        
        return {'result': date}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

