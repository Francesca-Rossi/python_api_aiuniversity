from .apiClass import  *

@app.get("/getNumberOfMenByCourseAndUni/{university}/{course}", tags=["Number of men"])
async def get_men_by_uni_and_course(university: str, course: str):
    '''Return the number of men that attend a specific degree course of an university'''
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
    '''Return the number of men that attend a specific degree course '''
    try:
        course_input = course.lower()
        course_input = course_input.strip()
        number =  await getNumberOfManByCourse(course_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenByUni/{university}", tags=["Number of men"])
async def get_men_by_uni(university: str):
    '''Return the number of men that attend a specific university '''
    try:
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfManByUNi(uni_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenWithSameProvinceOfUni/{university}", tags=["Number of men"])
async def get_men_whit_same_province_of_uni(university: str):
    '''Return the number of men that have the same province of the university'''
    try:
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfManWhitSameProvinceOfUni(uni_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenWithSameRegionOfUni/{university}", tags=["Number of men"])
async def get_men_whit_same_region_of_uni(university: str):
    '''Return the number of men that have the same region of the university '''
    try:
        uni_input = university.lower()
        uni_input = uni_input.strip()
        number =  await getNumberOfManWhitSameRegionOfUni(uni_input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenByRegion/{region}", tags=["Number of men"])
async def get_men_by_region(region: str):
    '''Return the number of men living  in a specific region '''
    try:
        input = region.lower()
        input = input.strip()
        number =  await getNumberOfManByRegion(input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenGroupbyRegion", tags=["Number of men"])
async def get_men_groupby_region():
    '''Return the number of men group by their living region '''
    try:
        number =  await getNumberOfManGroupbyRegion(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyatHomeRegion", tags=["Number of men"])
async def get_men_study_at_home_region():
    '''Return the number of men that study in their living region '''
    try:
        number =  await getNumberOfManStudyatHomeRegion(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyOutsideRegion", tags=["Number of men"])
async def get_men_study_outside_region():
    '''Return the number that study outside their living region  '''
    try:
        number =  await getNumberOfManStudyOutsideRegion(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenByProvince/{province}", tags=["Number of men"])
async def get_men_by_province(province: str):
    '''Return the number of men living  in a specific province'''
    try:
        input = province.lower()
        input = input.strip()
        number =  await getNumberOfManByProvince(input,  DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenGroupbyProvince", tags=["Number of men"])
async def get_men_groupby_province():
    '''Return the number of men by their living province'''
    try:
        number =  await getNumberOfManGroupbyProvince( DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyatHomeProvince", tags=["Number of men"])
async def get_men_study_at_home_province():
    '''Return the number of men that study in their living province  '''
    try:
        number =  await getNumberOfManStudyatHomeProvince(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getNumberOfMenStudyOutsideProvince", tags=["Number of men"])
async def get_men_study_outside_province():
    '''Return the number of men that study outside their living region '''
    try:
        number = await getNumberOfManStudyOutsideProvince(DB)
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
