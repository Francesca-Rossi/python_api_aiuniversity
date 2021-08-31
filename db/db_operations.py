import pandas as pd
import pymongo
from bson.json_util import *

'''
--------------------------
DB CONNECTION
--------------------------
'''
def dbOpenConnection():
    client = pymongo.MongoClient(
        "mongodb+srv://ai_university_admin:Pippo@dbserveraiuniversity.yfbov.mongodb.net/ai_university_db?retryWrites=true&w=majority")
    return client


def dbCloseConnection(client):
    client.close()

'''
--------------------------
INSERT METHOD
--------------------------
'''
def addNewStudent(student_info, db):
    try:
        db.students.insert_one(student_info) #student_info is a dict
    except:
        print('exception to insert students')

def addNewGraduate(graduate_info, db):
    try:
        db.graduates.insert_one(graduate_info) #graduate_info is a dict
    except:
        print('exception to insert students')


'''
--------------------------
SELECT METHOD
--------------------------
'''
def getAllStudents(db):
    try:
        cursor=db.students.find({})
    except:
        print('Error to get students from db')
    df=pd.read_json(dumps(cursor))
    df.to_json('doc/students_original_dataset.json')

#TODO: CREARE UN UNICA COLLEZIONE CON SIA STUDENTI CHE LAUREATI

#TODO: def getAllGraduates(db)

#TODO: def getAllUni(db)
#recupero tutte le università del database ( sia studenti che laureati)
#TODO: def getAllUni(course, db)
#recupero tutte le università che hanno quel corso di laurea ( sia studenti che laureati)
#TODO: def getAllUni(region, db)
#recupero tutte le università che si trovano in quella regione ( sia studenti che laureati)
#TODO: def getAllUni(province, db)
#recupero tutte le università che si trovano in quella provincia ( sia studenti che laureati)
#TODO: def getAllUni(city, db)
#recupero tutte le università che si trovano in quella citta ( sia studenti che laureati)

#TODO: def getAllCourse(db)
#recupero tutti i corsi del db ( sia studenti che laureati)
#TODO: def getAllCourse(uni, db)
#recupero tutti i corsi di un università ( sia studenti che laureati)

#TODO: def getAllRegion(db)
#TODO: def getAllProvince(db)

#TODO: def getAllSubject(course, db)
#recupero tutte le materie dato un corso

#TODO: def getAllEasyExam(course, db)
#recupero tutte gli esami facili dato un corso

#TODO: def getAllDifficultExam(course, db)
#recupero tutte gli esami difficili dato un corso

#TODO: def getNumberOfMan(course, db)
#recupero numero maschi in un corso
#TODO: def getNumberOfMan(uni, db)
#recupero numero maschi in un università
#TODO: def getNumberOfMan(region, db)
#recupero numero maschi in una regione iscritti all'uni
#TODO: def getNumberOfWoman(course, db)
#recupero numero femmine in un corso
#TODO: def getNumberOfWoman(uni, db)
#recupero numero femmine in un università
#TODO: def getNumberOfWoman(region, db)
#recupero numero maschi in una regione iscritti all'uni
#TODO: def getNumberOfSubscrives(course, db)
#recupero numero totali sottoscrizioni ( studenti + laureati) per quel corso
#TODO: def getNumberOfSubscrives(uni, db)
#recupero numero totali sottoscrizioni ( studenti + laureati) in un università
#TODO: def totalNumberOfSubscriver(db)
#recupero numero totali sottoscrizioni ( studenti + laureati) ricevute al questionario