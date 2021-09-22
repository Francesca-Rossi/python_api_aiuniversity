from .apiClass import  *

@app.get("/getAllStudents", tags=["Resources"])
async def get_all_students():
    '''Return all students in the database'''
    try:
        json = await getAllStudents(DB)
        return json
    except:
        raise HTTPException(status_code=400, detail="Model not found.")
@app.get("/getAllGraduates", tags=["Resources"])
async def get_all_graduates():
    '''Return all graduates in the database'''
    try:
        json = await getAllGraduates(DB)
        return json
    except:
        raise HTTPException(status_code=400, detail="Model not found.")

@app.get("/getAllSubscriptions", tags=["Resources"])
async def get_all_subscriptions():
    '''Return all subscriptions in the database'''
    try:
        json = await getAllSubscription(DB)
        return json
    except:
        raise HTTPException(status_code=400, detail="Model not found.")