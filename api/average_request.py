from .apiClass import  *

@app.get("/getMarkAveragebyCourse/{university}/{course}", tags=["Mark"])
async def get_mark_average_by_course(university: str, course: str):
    '''Returns the average of the marks given the bachelor’s degree'''
    try:
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        avg = await getMarkAveragebyCourse(input_course, input_uni, DB)
        return {'result': round(avg, 2)}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getMarkAveragebyCourseAndYear/{university}/{course}/{year_of_course}", tags=["Mark"])
async def get_mark_average_by_course_and_year(university: str, course: str, year_of_course: int):
    '''Returns the average of the marks given the bachelor’s degree and the year of course'''
    try:
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        avg = await getMarkAveragebyCourseAndYear(input_course, input_uni, year_of_course,  DB)
        return {'result': round(avg, 2)}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")



@app.get("/getGradeAveragebyCourse/{university}/{course}", tags=["Grade"])
async def get_grade_average_by_course(university: str, course: str):
    '''Returns the average of the grades given the bachelor’s degree'''
    try:
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        avg = await getGradeAveragebyCourse(input_course, input_uni, DB)
        return {'result': round(avg, 2)}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getDurationAveragebyCourse/{university}/{course}", tags=["Duration"])
async def get_duratiion_average_by_course(university: str, course: str):
    '''Returns the average of the duration given the bachelor’s degree'''
    try:
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        duration = await getDurationAveragebyCourse(input_course, input_uni, DB)
        return {'result': duration}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getExamNotDoneAveragebyCourseAndYear/{university}/{course}/{year_of_course}", tags=["Subjects & Exams"])
async def get_exam_not_done_by_course_and_year(university: str, course: str, year_of_course:int ):
    '''Returns the average of the exams not done given the bachelor’s degree and years'''
    try:
        input_uni = university.lower()
        input_uni = input_uni.strip()
        input_course=course.lower()
        input_course = input_course.strip()
        avg = await getExamNotDoneAveragebyCourseAndYear(input_course, input_uni, year_of_course, DB)
        return {'result': round(avg, 2)}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")



