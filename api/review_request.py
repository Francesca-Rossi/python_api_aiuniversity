from .apiClass import  *

@app.get("/getReviewListbyCourse/{university}/{course}", tags=["Reviews"])
async def get_review_list_by_course(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        list = await getReviewListbyCourse(input_course, input_uni,  DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getReviewListbyCourseAndYear/{university}/{course}/{year_of_course}", tags=["Reviews"])
async def get_review_list_by_course_and_year(university: str, course: str, year_of_course: int):
    '''Get the average of exame not done given the course and the year'''
    try:
        
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        list = await getReviewListbyCourseAndYear(input_course, input_uni, year_of_course, DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getReviewAverangebyCourse/{university}/{course}", tags=["Reviews"])
async def get_review_average_by_course(university: str, course: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course= course.lower()
        input_course = input_course.strip()
        number = await getReviewAverangebyCourse(input_course, input_uni, DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getReviewAverangebyCourseAndYear/{university}/{course}/{year_of_course}", tags=["Reviews"])
async def get_review_average_by_course_and_year(university: str, course: str, year_of_course: int):
    '''Get the average of exame not done given the course and the year'''
    try:
        
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course= course.lower()
        input_course = input_course.strip()
        number = await getReviewAverangebyCourseAndYear(input_course, input_uni,year_of_course, DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getReviewAverangebyUni/{university}", tags=["Reviews"])
async def get_review_average_by_uni(university: str):
    '''Get the average of exame not done given the course and the year'''
    try:
        
        input_uni = university.lower()
        input_uni = input_uni.strip()
        number = await getReviewAverangebyUni(input_uni, DB)
        
        return {'result': number}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")