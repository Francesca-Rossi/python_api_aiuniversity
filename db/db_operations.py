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
        print('exception to insert graduate')

def addNewSubscriptions(subscriptions_info, db):
    try:
        db.subscriptions.insert_one(subscriptions_info)
    except Exception as e:
        print( e)


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


def getAllGraduates(db):
    try:
        cursor=db.graduates.find({})
    except:
        print('Error to get graduates from db')
    df=pd.read_json(dumps(cursor))
    df.to_json('doc/graduates_original_dataset.json')

def getAllSubscription(db):
    try:
        cursor=db.subscriptions.find({})
    except:
        print('Error to get graduates from db')
    df=pd.read_json(dumps(cursor))
    df.to_json('doc/subscriptions_original_dataset.json')

#TODO: def countAllSubscription(db)

def getAllUni(db):
    #recupero tutte le università del database ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('university')
        for i in cursor:
            print(i)
    except Exception as e:
        print(e)

def getAllUni(course, db):
    #recupero tutte le università che hanno quel corso di laurea ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('university', {"degree_course": course})
        for i in cursor:
            print(i)
    except Exception as e:
        print(e)

def getAllUni(region, db):
    # recupero tutte le università che si trovano in quella regione ( sia studenti che laureati)
    try:
        home_region_list = db.subscriptions.distinct('university', { '$or': [{ "study_region": '' ,"home_region": region}]})
        study_region_list= db.subscriptions.distinct('university', {'$or': [{"study_region": region}]})
        for i in home_region_list:
            for j in study_region_list:
                if ( j==i ):
                    print(j)
    except Exception as e:
        print(e)

def getAllUni(province, db):
    #recupero tutte le università che si trovano in quella provincia ( sia studenti che laureati)
    try:
        home_province_list = db.subscriptions.distinct('university', { '$or': [{ "study_province": '' ,"home_province": province}]})
        study_province_list = db.subscriptions.distinct('university', {'$or': [{"study_province": province}]})
        for i in home_province_list:
            for j in study_province_list:
                if ( j==i ):
                    print(j)
    except Exception as e:
        print(e)

def getAllCourse(db):
    #recupero tutti i corsi del db ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('degree_course')
        degree_course_list=set()
        for item in cursor:
            if item not in degree_course_list:
                degree_course_list.add(item)
                print(item)

    except Exception as e:
        print(e)

def getAllCourse(uni, db):
    #recupero tutti i corsi di un università ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('degree_course', {"university": uni})
        degree_course_list = set()
        for item in cursor:
            if item not in degree_course_list:
                degree_course_list.add(item)
                print(item)
    except Exception as e:
        print(e)

def getAllHomeRegion(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('home_region')
        for i in cursor:
            print(i)
    except Exception as e:
        print(e)

def getAllStudyRegion(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('study_region')
        for i in cursor:
            print(i)
    except Exception as e:
        print(e)

def getAllHomeProvince(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('home_province')
        for i in cursor:
            print(i)
    except Exception as e:
        print(e)

def getAllStudyProvince(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    try:
        cursor = db.subscriptions.distinct('study_province')
        for i in cursor:
            print(i)
    except Exception as e:
        print(e)

def getAllSubject(course, db):
    #recupero tutte le materie dato un corso generico
    capital_course= course.capitalize()
    try:
        cursor = db.subscriptions.distinct('subject_area', {'$or':[{"degree_course": course},{"degree_course": capital_course}]})
        for i in cursor:
            list= i.split(',')
            subject_list=set()
            for item in list:
                if item not in subject_list:
                    subject_list.add(item.strip())
                    print(item.strip())
    except Exception as e:
        print(e)

def getAllSubjectWhitUni(course, db, uni):
    #recupero tutte le materie dato un corso specifico di un università
    capital_course= course.capitalize()
    try:
        cursor = db.subscriptions.distinct('subject_area',  {'$and': [
               {
                 '$or': [
                         {"degree_course" : course},
                         {"degree_course" : capital_course}
                       ]
               },
               {
                 "university": uni
               }
             ]})
        for i in cursor:
            list= i.split(',')
            subject_list=set()
            for item in list:
                if item not in subject_list:
                    subject_list.add(item)
                    print(item)
    except Exception as e:
        print(e)

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