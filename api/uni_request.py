from .apiClass import  *

@app.get("/getAllUni", tags=["Universities"])
async def get_all_uni():
    '''Get all the universities present in the DB'''
    try:
        
        list = await getAllUni(DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getAllUniByCourse/{course}", tags=["Universities"])
async def get_all_uni_by_course(course: str):
    '''Return all the universities by course'''
    try:
        
        input= course.lower()
        input = input.strip()
        list = await getAllUnByCourse(input, DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getAllUniByRegion/{region}", tags=["Universities"])
async def get_all_uni_by_region(region: str):
    '''Return all the universities by region'''
    try:
        
        input = region.lower()
        input = input.strip()
        list = await getAllUniByRegion(input, DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getAllUniByProvince/{province}", tags=["Universities"])
async def get_all_uni_by_province(province: str):
    '''Return all the universities by province'''
    try:
        
        input = province.lower()
        input = input.strip()
        list = await getAllUniByProvince(input, DB)
        
        return {'result': list}
    except:
        raise HTTPException(status_code=400, detail="Model not found.")