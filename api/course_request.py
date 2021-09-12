from .apiClass import  *

@app.get("/getAllCourses", tags=["Degree courses"])
async def get_all_course():
    '''Return all Italian bachelor's degree registered in the database'''
    try:
        list = await getAllCourse(DB)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getAllCoursesByUni/{university}", tags=["Degree courses"])
async def get_all_course_by_uni(university: str):
    '''Return all Italian bachelor's degree given by an university'''
    try:
        input = university.lower()
        input = input.strip()
        list =  await getAllCourseByUni(input, DB)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")