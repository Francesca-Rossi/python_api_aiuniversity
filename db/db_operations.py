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

def getAllRegion(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    try:
        home = db.subscriptions.distinct('home_region')
        study = db.subscriptions.distinct('study_region')
        region_list=set()
        for item in home:
            region_list.add(item)
        for item in study:
            if item not in region_list:
                region_list.add(item)
        for i in region_list:
            print(i)
        return region_list
    except Exception as e:
        print(e)

def getRegionFromUni(uni, db):
    #recupero la regione di un università
    try:
        study = db.subscriptions.distinct('study_region', {"university": uni})
        home = db.subscriptions.distinct('home_region', {"university": uni})
        if len(study) > 1:
            print(len(study))
            for item in study:
                if (len(home)>0):
                    if item != '':
                        for item1 in home:
                            if (item == item1):
                                print(item)
                                return item
                else:
                    print(item)
                    return item
        else:
            print("NO REGION FOUND")

    except Exception as e:
        print(e)

def getAllProvince(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    try:
        home = db.subscriptions.distinct('home_province')
        study = db.subscriptions.distinct('study_province')
        province_list=set()
        for item in home:
            province_list.add(item.upper())
        for item in study:
            if item not in province_list:
                province_list.add(item.upper())
        for i in province_list:
            print(i)
    except Exception as e:
        print(e)

def getProvinceFromUni(uni, db):
    #recupero la regione di un università
    try:
        study = db.subscriptions.distinct('study_province', {"university": uni})
        home = db.subscriptions.distinct('home_province', {"university": uni})
        if len(study) > 0:
            print(len(study))
            for item in study:
                if (len(home)>0):
                    for item1 in home:
                        if (item == item1):
                            print(item)
                            return item
                else:
                    print(item)
                    return item
        else:
            print('NO PROVINCE FOUND')

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
    try:
        cursor = db.subscriptions.distinct('subject_area',  {'$and': [{"degree_course": course},{"university": uni}]})
        for i in cursor:
            list= i.split(',')
            subject_list=set()
            for item in list:
                if item not in subject_list:
                    subject_list.add(item)
                    print(item)
    except Exception as e:
        print(e)

def getAllEasyExam(course, uni, db):
    #recupero tutte gli esami facili dato un corso di un'università
    try:
        easy_exam = db.subscriptions.distinct('easy_exams',{'$and': [{"university": uni}, {'degree_course': course}]})
        exams_list = set()
        for exams in easy_exam:
            list= exams.split(',')
            for item in list:
                if item.strip() not in exams_list:
                    exams_list.add(item.strip())
                    print(item.strip())
    except Exception as e:
        print(e)

def getAllDifficultExam(course, uni,  db):
    #recupero tutte gli esami difficili dato un corso
    # recupero tutte gli esami facili dato un corso di un'università
    try:
        hard_exams = db.subscriptions.distinct('hard_exams', {'$and': [{"university": uni}, {'degree_course': course}]})
        exams_list = set()
        for exams in hard_exams:
            list = exams.split(',')
            for item in list:
                if item.strip() not in exams_list:
                    exams_list.add(item.strip())
                    print(item.strip())
    except Exception as e:
        print(e)

'''
MAN QUERY
'''
def getNumberOfManByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    man=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}, {'gender':'m'}]})
    print(man)
def getNumberOfManByCourse(course, db):
    #recupero numero maschi in un corso
    man = db.subscriptions.count_documents({'$and': [ {'degree_course': course}, {'gender': 'm'}]})
    print(man)

def getNumberOfManByUNi(uni, db):
    #recupero numero maschi in un università
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'gender': 'm'}]})
    print(man)

def getNumberOfManWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    province=getProvinceFromUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}, {'gender': 'm'}]})
    print(man)

def getNumberOfManWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    region=getRegionFromUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}, {'gender': 'm'}]})
    print(man)

def getNumberOfManByRegion(home_region, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_region': home_region}, {'gender': 'm'}]})
    print(man)

def getNumberOfManGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    region_list=getAllRegion(db)
    region_dict={}
    for region in region_list:
        if region != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_region': region}, {'gender': 'm'}]})
            region_dict[region]=n_man
    print(region_dict)

def getNumberOfManStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_region': ''}, {'gender': 'm'}]})
    print(man)

def getNumberOfManStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione ragruppati per re
    region_list=getAllRegion(db)
    total=0
    for region in region_list:
        if region != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_region': region}, {'gender': 'm'}]})
            total = total + n_man
    print(total)

def getNumberOfManByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_province': home_province}, {'gender': 'm'}]})
    print(man)

def getNumberOfManGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    province_list=getAllProvince(db)
    province_dict={}
    for province in province_list:
        if province != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_province': province}, {'gender': 'm'}]})
            province_dict[province]=n_man
    print(province_dict)

def getNumberOfManStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_province': ''}, {'gender': 'm'}]})
    print(man)

def getNumberOfManStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    province_list=getAllProvince(db)
    total=0
    for province in province_list:
        if province != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_province': province}, {'gender': 'm'}]})
            total = total + n_man
    print(total)



'''
WOMAN QUERY
'''
def getNumberOfWomanByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    man=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}, {'gender':'f'}]})
    print(man)
def getNumberOfWomanByCourse(course, db):
    #recupero numero maschi in un corso
    man = db.subscriptions.count_documents({'$and': [ {'degree_course': course}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanByUNi(uni, db):
    #recupero numero maschi in un università
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    province=getProvinceFromUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    region=getRegionFromUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanByRegion(home_region, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_region': home_region}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    region_list=getAllRegion(db)
    region_dict={}
    for region in region_list:
        if region != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_region': region}, {'gender': 'f'}]})
            region_dict[region]=n_man
    print(region_dict)

def getNumberOfWomanStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_region': ''}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione ragruppati per re
    region_list=getAllRegion(db)
    total=0
    for region in region_list:
        if region != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_region': region}, {'gender': 'f'}]})
            total = total + n_man
    print(total)

def getNumberOfWomanByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_province': home_province}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    province_list=getAllProvince(db)
    province_dict={}
    for province in province_list:
        if province != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_province': province}, {'gender': 'f'}]})
            province_dict[province]=n_man
    print(province_dict)

def getNumberOfWomanStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_province': ''}, {'gender': 'f'}]})
    print(man)

def getNumberOfWomanStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    province_list=getAllProvince(db)
    total=0
    for province in province_list:
        if province != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_province': province}, {'gender': 'f'}]})
            total = total + n_man
    print(total)



'''
SUBSCRIBERS QUERY
'''
def getNumberOfPeopleByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    man=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}]})
    print(man)
def getNumberOfPeopleByCourse(course, db):
    #recupero numero maschi in un corso
    man = db.subscriptions.count_documents({'$and': [ {'degree_course': course}]})
    print(man)

def getNumberOfPeopleByUNi(uni, db):
    #recupero numero maschi in un università
    man = db.subscriptions.count_documents({'$and': [{'university': uni}]})
    print(man)

def getNumberOfPeopleWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    province=getProvinceFromUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}]})
    print(man)

def getNumberOfPeopleWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    region=getRegionFromUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}]})
    print(man)

def getNumberOfPeopleByRegion(home_region, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_region': home_region}]})
    print(man)


def getNumberOfPeopleGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    region_list=getAllRegion(db)
    region_dict={}
    for region in region_list:
        if region != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_region': region}]})
            region_dict[region]=n_man
    print(region_dict)

def getNumberOfPeopleStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_region': ''}]})
    print(man)

def getNumberOfPeopleStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione
    region_list=getAllRegion(db)
    total=0
    for region in region_list:
        if region != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_region': region}]})
            total = total + n_man
    print(total)

def getNumberOfPeopleByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_province': home_province}]})
    print(man)

def getNumberOfPeopleGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    province_list=getAllProvince(db)
    province_dict={}
    for province in province_list:
        if province != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_province': province}]})
            province_dict[province]=n_man
    print(province_dict)

def getNumberOfPeopleStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_province': ''}]})
    print(man)

def getNumberOfPeopleStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    province_list=getAllProvince(db)
    total=0
    for province in province_list:
        if province != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_province': province}]})
            total = total + n_man
    print(total)


