from .apiClass import  *

@app.get("/getNumberOfMenByCourseAndUni/{university}/{course}", tags=["Number of men"])
async def get_men_by_uni_and_course(university: str, course: str):
    '''How many men there are in a course? '''
    try:
        uni_input = university.lower()
        uni_input = uni_input.strip()
        course_input = course.lower()
        course_input = course_input.strip()
        number =  await getNumberOfManByCourseAndUni(course_input, uni_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenByCourse/{course}", tags=["Number of men"])
async def get_men_by_course( course: str):
    '''How many men study in this course? '''
    try:
        course_input = course.lower()
        course_input = course_input.strip()
        number =  await getNumberOfManByCourse(course_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenByUni/{university}", tags=["Number of men"])
async def get_men_by_uni(university: str):
    '''How many men there are in a university? '''
    try:
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfManByUNi(uni_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenWithSameProvinceOfUni/{university}", tags=["Number of men"])
async def get_men_whit_same_province_of_uni(university: str):
    '''How many men there are in a province? '''
    try:
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfManWhitSameProvinceOfUni(uni_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenWithSameRegionOfUni/{university}", tags=["Number of men"])
async def get_men_whit_same_region_of_uni(university: str):
    '''How many men there are in a region? '''
    try:
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfManWhitSameRegionOfUni(uni_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenByRegion/{region}", tags=["Number of men"])
async def get_men_by_region(region: str):
    '''How many men there are in a region? '''
    try:
        input = region.lower()
        input = input.strip()
        number =  await getNumberOfManByRegion(input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenGroupbyRegion", tags=["Number of men"])
async def get_men_groupby_region():
    '''How many men there are in all regions? '''
    try:
        number =  await getNumberOfManGroupbyRegion(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyatHomeRegion", tags=["Number of men"])
async def get_men_study_at_home_region():
    '''How many men study at the home region? '''
    try:
        number =  await getNumberOfManStudyatHomeRegion(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyOutsideRegion", tags=["Number of men"])
async def get_men_study_outside_region():
    '''How many men study outside the region? '''
    try:
        number =  await getNumberOfManStudyOutsideRegion(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenByProvince/{province}", tags=["Number of men"])
async def get_men_by_province(province: str):
    '''How many men there are in a province? '''
    try:
        input = province.lower()
        input = input.strip()
        number =  await getNumberOfManByProvince(input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenGroupbyProvince", tags=["Number of men"])
async def get_men_groupby_province():
    '''How many men there are in all provinces? '''
    try:
        number =  await getNumberOfManGroupbyProvince( DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyatHomeProvince", tags=["Number of men"])
async def get_men_study_at_home_province():
    '''How many men study at the home province? '''
    try:
        number =  await getNumberOfManStudyatHomeProvince(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyOutsideProvince", tags=["Number of men"])
async def get_men_study_outside_province():
    '''How many men study outside the province? '''
    try:
        number = await getNumberOfManStudyOutsideProvince(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
