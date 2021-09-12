from .apiClass import  *

@app.get("/getNumberOfWomenByCourseAndUni/{university}/{course}", tags=["Number of women"])
async def get_women_by_uni_and_course(university: str, course: str):
    '''Return the number of women that attend a specific degree course of an university'''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        course_input = course.lower()
        course_input = course_input.strip()
        number =  await getNumberOfWomanByCourseAndUni(course_input, uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenByCourse/{course}", tags=["Number of women"])
async def get_women_by_course( course: str):
    '''Return the number of women that attend a specific degree course '''
    try:
        
        course_input = course.lower()
        course_input = course_input.strip()
        number =  await getNumberOfWomanByCourse(course_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenByUni/{university}", tags=["Number of women"])
async def get_women_by_uni(university: str):
    '''Return the number of women that attend a specific university '''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfWomanByUNi(uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenWithSameProvinceOfUni/{university}", tags=["Number of women"])
async def get_women_whit_same_province_of_uni(university: str):
    '''Return the number of women that have the same province of the university'''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfWomanWhitSameProvinceOfUni(uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenWithSameRegionOfUni/{university}", tags=["Number of women"])
async def get_women_whit_same_region_of_uni(university: str):
    '''Return the number of women that have the same region of the university '''
    try:
        
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfWomanWhitSameRegionOfUni(uni_input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenByRegion/{region}", tags=["Number of women"])
async def get_women_by_region(region: str):
    '''Return the number of women living  in a specific region '''
    try:
        
        input = region.lower()
        input = input.strip()
        number =  await getNumberOfWomanByRegion(input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenGroupbyRegion", tags=["Number of women"])
async def get_women_groupby_region():
    '''Return the number of women group by their living region '''
    try:
        
        number =  await getNumberOfWomanGroupbyRegion(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenStudyatHomeRegion", tags=["Number of women"])
async def get_women_study_at_home_region():
    '''Return the number of women that study in their living region '''
    try:
        
        number =  await getNumberOfWomanStudyatHomeRegion(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenStudyOutsideRegion", tags=["Number of women"])
async def get_women_study_outside_region():
    '''Return the number that study outside their living region  '''
    try:
        
        number =  await getNumberOfWomanStudyOutsideRegion(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenByProvince/{province}", tags=["Number of women"])
async def get_women_by_province(province: str):
    '''Return the number of women living  in a specific province'''
    try:
        
        input = province.lower()
        input = input.strip()
        number =  await getNumberOfWomanByProvince(input,  DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenGroupbyProvince", tags=["Number of women"])
async def get_women_groupby_province():
    '''Return the number of women by their living province'''
    try:
        
        number =  await getNumberOfWomanGroupbyProvince( DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfWomenStudyatHomeProvince", tags=["Number of women"])
async def get_women_study_at_home_province():
    '''Return the number of women that study in their living province  '''
    try:
        
        number =  await getNumberOfWomanStudyatHomeProvince(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")


@app.get("/getNumberOfWomenStudyOutsideProvince", tags=["Number of women"])
async def get_women_study_outside_province():
    '''Return the number of women that study outside their living region '''
    try:
        
        number = await getNumberOfWomanStudyOutsideProvince(DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
