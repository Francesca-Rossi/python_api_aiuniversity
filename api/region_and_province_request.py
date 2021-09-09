from .apiClass import  *

@app.get("/getAllRegions", tags=["Regions & Provinces"])
async def get_all_region():
    '''Get all the regions from the db'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        list =  await getAllRegion(db)
        dbCloseConnection(client)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")


@app.get("/getRegionByUni/{university}", tags=["Regions & Provinces"])
async def get_region_by_uni(university: str):
    '''Get the region by the university'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input = university.lower()
        input = input.strip()
        list =  await getRegionByUni(input, db)
        dbCloseConnection(client)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getAllProvinces", tags=["Regions & Provinces"])
async def get_all_province():
    '''Get all the provinces from the db'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        list =  await getAllProvince(db)
        dbCloseConnection(client)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getProvinceByUni/{university}", tags=["Regions & Provinces"])
async def get_province_by_uni(university: str):
    '''Get the province of a university'''
    try:
        client = dbOpenConnection()
        db = client.get_database("ai_university_db")
        input = university.lower()
        input = input.strip()
        list =  await getProvinceByUni(input, db)
        dbCloseConnection(client)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
