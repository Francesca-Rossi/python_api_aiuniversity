from .apiClass import  *

@app.get("/getAllRegions", tags=["Regions & Provinces"])
async def get_all_region():
    '''Get all the regions from the DB'''
    try:
        list =  await getAllRegion(DB)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")


@app.get("/getRegionByUni/{university}", tags=["Regions & Provinces"])
async def get_region_by_uni(university: str):
    '''Get the region by the university'''
    try:
        input = university.lower()
        input = input.strip()
        list =  await getRegionByUni(input, DB)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getAllProvinces", tags=["Regions & Provinces"])
async def get_all_province():
    '''Get all the provinces from the DB'''
    try:
        list =  await getAllProvince(DB)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getProvinceByUni/{university}", tags=["Regions & Provinces"])
async def get_province_by_uni(university: str):
    '''Get the province of a university'''
    try:
        input = university.lower()
        input = input.strip()
        list =  await getProvinceByUni(input, DB)
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
