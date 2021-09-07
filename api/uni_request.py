from .apiClass import  *

@app.get("/getAllUni", tags=["Universities"])
async def get_all_uni():
    '''Get all the university present in the db'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    list = await getAllUni(db)
    dbCloseConnection(client)
    return list

@app.get("/getAllUniByCourse", tags=["Universities"])
async def get_all_uni_by_course(course: str):
    '''Get all the university by course'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input= course.lower()
    input = input.strip()
    list = await getAllUnByCourse(input, db)
    dbCloseConnection(client)
    return list

@app.get("/getAllUniByRegion", tags=["Universities"])
async def get_all_uni_by_region(region: str):
    '''Get all the university by region'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = region.lower()
    input = input.strip()
    list = await getAllUniByRegion(input, db)
    dbCloseConnection(client)
    return list

@app.get("/getAllUniByProvince", tags=["Universities"])
async def get_all_uni_by_province(province: str):
    '''Get all the university by region'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = province.lower()
    input = input.strip()
    list = await getAllUniByProvince(input, db)
    dbCloseConnection(client)
    return list