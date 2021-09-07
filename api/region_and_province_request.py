from .apiClass import  *

@app.get("/getAllRegion", tags=["Regions & Provinces"])
async def get_all_region():
    '''Get all the region from the db'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    list =  await getAllRegion(db)
    dbCloseConnection(client)
    return list

@app.get("/getRegionByUni", tags=["Regions & Provinces"])
async def get_region_by_uni(university: str):
    '''Get all the region from the db'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = university.lower()
    input = input.strip()
    list =  await getRegionByUni(input, db)
    dbCloseConnection(client)
    return list

@app.get("/getAllProvince", tags=["Regions & Provinces"])
async def get_all_province():
    '''Get all the province from the db'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    list =  await getAllProvince(db)
    dbCloseConnection(client)
    return list

@app.get("/getProvinceByUni", tags=["Regions & Provinces"])
async def get_province_by_uni(university: str):
    '''Get all the province given a uni'''
    client = dbOpenConnection()
    db = client.get_database("ai_university_db")
    input = university.lower()
    input = input.strip()
    list =  await getProvinceByUni(input, db)
    dbCloseConnection(client)
    return list
