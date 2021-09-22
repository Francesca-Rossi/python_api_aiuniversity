import pymongo
from bson.json_util import *
from datetime import datetime
from ai_model.model import *

#region ---CONNECTION METHOD---
def dbOpenConnection():
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://ai_university_admin:Pippo@dbserveraiuniversity.yfbov.mongodb.net/ai_university_db?retryWrites=true&w=majority")
        logging.warning('---CONNECT DB SUCCESS---')
        return client
    except:
        logging.error('---FAILED TO CONNECT DB---')
        logging.error("Exception occurred", exc_info=True)


def dbCloseConnection(client):
    try:
        client.close()
        logging.warning('---CLOSE CONNECTION DB---')
    except:
        logging.warning('---FAILED TO CLOSE CONNECTION DB---')
        logging.error("Exception occurred", exc_info=True)
#endregion

#region ---INSERT METHOD---
async def addNewStudent(student_info, db):
    try:
        db.students.insert_one(student_info) #student_info is a dict
        logging.warning('-----New student added in db------')
        logging.warning('-----Method finish whit success------')
        return True
    except:
        logging.error("Exception occurred", exc_info=True)
        return False

async def addNewGraduate(graduate_info, db):
    try:
        db.graduates.insert_one(graduate_info) #graduate_info is a dict
        logging.warning('-----New graduate added in db------')
        logging.warning('-----Method finish whit success------')
        return True
    except:
        logging.error("Exception occurred", exc_info=True)
        return False

async def addNewSubscriptions(subscriptions_info, db):
    try:
        db.subscriptions.insert_one(subscriptions_info)
        logging.warning('-----New subscriptions added in db------')
        logging.warning('-----Method finish whit success------')
        return True
    except:
        logging.error("Exception occurred", exc_info=True)
        return False

async def AddNewAdvice(student_info, db):
    try:
        db.advice.insert_one(student_info) #student_info is a dict
        logging.warning('-----New advice added in db------')
        logging.warning('-----Method finish whit success------')
        return True
    except:
        logging.error("Exception occurred", exc_info=True)
        return False
#endregion

#region ---SELECT METHOD ---

def getAllStudents(db):
    try:
        cursor=db.students.find({})
        df = pd.read_json(dumps(cursor))
        df = df.iloc[:, 1:]
        df.to_json('doc/students_original_dataset.json')
        logging.warning('-----Method finish whit success------')
        return dumps(cursor)
    except:
        logging.error("Exception occurred", exc_info=True)

def getAllGraduates(db):
    try:
        cursor=db.graduates.find({})
        df = pd.read_json(dumps(cursor))
        df = df.iloc[:, 1:]
        df.to_json('doc/graduates_original_dataset.json')
        logging.warning('-----Method finish whit success------')
        return dumps(cursor)
    except:
        logging.error("Exception occurred", exc_info=True)


def getAllSubscription(db):
    try:
        cursor=db.subscriptions.find({})
        df = pd.read_json(dumps(cursor))
        df = df.iloc[:, 1:]
        df.to_json('doc/subscriptions_original_dataset.json')
        logging.warning('-----Method finish whit success------')
        return dumps(cursor)
    except:
        logging.error("Exception occurred", exc_info=True)


async def getAllUni(db):
    #recupero tutte le università del database ( sia studenti che laureati)
    uni_list = set()
    try:
        cursor = db.subscriptions.distinct('university')
        for item in cursor:
            if item !="":
                uni_list.add(item)
        logging.warning('-----Method finish whit success------')
        return uni_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllUnByCourse(course, db):
    #recupero tutte le università che hanno quel corso di laurea ( sia studenti che laureati)
    uni_list = set()
    try:
        cursor = db.subscriptions.distinct('university', {"degree_course": course})
        for item in cursor:
            if item != "":
                uni_list.add(item)
        logging.warning('-----Method finish whit success------')
        return uni_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllUniByRegion(region, db):
    # recupero tutte le università che si trovano in quella regione ( sia studenti che laureati)
    uni_list = set()
    try:
        home_region_list = db.subscriptions.distinct('university', { '$or': [{ "study_region": '' ,"home_region": region}]})
        study_region_list= db.subscriptions.distinct('university', {'$or': [{"study_region": region}]})
        for i in home_region_list:
            for j in study_region_list:
                if ( j==i ):
                    if i != "":
                        uni_list.add(i)
        logging.warning('-----Method finish whit success------')
        return uni_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllUniByProvince(province, db):
    #recupero tutte le università che si trovano in quella provincia ( sia studenti che laureati)
    uni_list = set()
    try:
        home_province_list = db.subscriptions.distinct('university', { '$or': [{ "study_province": '' ,"home_province": province}]})
        study_province_list = db.subscriptions.distinct('university', {'$or': [{"study_province": province}]})
        for i in home_province_list:
            for j in study_province_list:
                if ( j==i ):
                    if i != "":
                        uni_list.add(i)
        logging.warning('-----Method finish whit success------')
        return uni_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllCourse(db):
    #recupero tutti i corsi del db ( sia studenti che laureati)
    degree_course_list = set()
    try:
        cursor = db.subscriptions.distinct('degree_course')
        for item in cursor:
            if item not in degree_course_list:
                if item != "":
                    degree_course_list.add(item)
        logging.warning('-----Method finish whit success------')
        return degree_course_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllCourseByUni(uni, db):
    #recupero tutti i corsi di un università ( sia studenti che laureati)
    degree_course_list = set()
    try:
        cursor = db.subscriptions.distinct('degree_course', {"university": uni})
        degree_course_list = set()
        for item in cursor:
            if item not in degree_course_list:
                if item != "":
                    degree_course_list.add(item)
        logging.warning('-----Method finish whit success------')
        return degree_course_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllRegion(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    region_list = set()
    try:
        home = db.subscriptions.distinct('home_region')
        study = db.subscriptions.distinct('study_region')
        for item in home:
            region_list.add(item)
        for item in study:
            if item not in region_list:
                region_list.add(item)
        logging.warning('-----Method finish whit success------')
        return region_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getRegionByUni(uni, db):
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
                                return item
                else:
                    return item
        else:
            item="NO REGION FOUND"
            print(item)
            return item

        logging.warning('-----Method finish whit success------')
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllProvince(db):
    #recupero tutti le regioni del db ( sia studenti che laureati)
    province_list = set()
    try:
        home = db.subscriptions.distinct('home_province')
        study = db.subscriptions.distinct('study_province')
        for item in home:
            province_list.add(item.upper())
        for item in study:
            if item not in province_list:
                province_list.add(item.upper())
        logging.warning('-----Method finish whit success------')
        return province_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getProvinceByUni(uni, db):
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
                            return item.upper()
                else:
                    print(item)
                    return item.upper()
        else:
            item= 'NO PROVINCE FOUND'
            return item.upper()
        logging.warning('-----Method finish whit success------')

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)



async def getAllSubject(course, db):
    #recupero tutte le materie dato un corso generico
    subject_list = set()
    try:
        cursor = db.subscriptions.distinct('subject_area', {'$or':[{"degree_course": course}]})
        for i in cursor:
            list= i.split(',')
            for item in list:
                if item not in subject_list:
                    if item != "":
                        subject_list.add(item.strip())
        logging.warning('-----Method finish whit success------')
        return subject_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllSubjectByUni(course,  uni, db):
    #recupero tutte le materie dato un corso specifico di un università
    subject_list = set()
    try:
        cursor = db.subscriptions.distinct('subject_area',  {'$and': [{"degree_course": course},{"university": uni}]})
        for i in cursor:
            list= i.split(',')
            for item in list:
                item = item.strip()
                if item not in subject_list:
                    if item != "":
                        subject_list.add(item)
        logging.warning('-----Method finish whit success------')
        return subject_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


async def getAllEasyExam(course, uni, db):
    #recupero tutte gli esami facili dato un corso di un'università
    exams_list = set()
    try:
        easy_exam = db.subscriptions.distinct('easy_exams',{'$and': [{"university": uni}, {'degree_course': course}]})
        for exams in easy_exam:
            list= exams.split(',')
            for item in list:
                if item.strip() not in exams_list:
                    if item.strip()  != "":
                        exams_list.add(item.strip())
        logging.warning('-----Method finish whit success------')
        return exams_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

async def getAllDifficultExam(course, uni,  db):
    #recupero tutte gli esami difficili dato un corso
    # recupero tutte gli esami facili dato un corso di un'università
    exams_list = set()
    try:
        hard_exams = db.subscriptions.distinct('hard_exams', {'$and': [{"university": uni}, {'degree_course': course}]})
        for exams in hard_exams:
            list = exams.split(',')
            for item in list:
                if item.strip() not in exams_list:
                    if item.strip() != "":
                        exams_list.add(item.strip())
        logging.warning('-----Method finish whit success------')
        return exams_list
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

#region ---MAN QUERY---
async def getNumberOfManByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    try:
        man=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}, {'gender':'m'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManByCourse(course, db):
    #recupero numero maschi in un corso
    try:
        man = db.subscriptions.count_documents({'$and': [ {'degree_course': course}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManByUNi(uni, db):
    #recupero numero maschi in un università
    try:
        man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    try:
        province=await getProvinceByUni(uni, db)
        man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    try:
        region=await getRegionByUni(uni, db)
        man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)


async def getNumberOfManByRegion(home_region, db):
    try:
        #recupero numero maschi in una regione iscritti all'uni
        man = db.subscriptions.count_documents({'$and': [{'home_region': home_region}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    try:
        region_list=await getAllRegion(db)
        region_dict={}
        for region in region_list:
            if region != "":
                n_man = db.subscriptions.count_documents({'$and': [{'home_region': region}, {'gender': 'm'}]})
                region_dict[region]=n_man
        logging.warning('-----Method finish whit success------')
        return region_dict
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    try:
        man = db.subscriptions.count_documents({'$and': [{'study_region': ''}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione ragruppati per re
    try:
        region_list=await getAllRegion(db)
        total=0
        for region in region_list:
            if region != "":
                n_man =db.subscriptions.count_documents({'$and': [{'study_region': region}, {'gender': 'm'}]})
                total = total + n_man
        logging.warning('-----Method finish whit success------')
        return total
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    try:
        man = db.subscriptions.count_documents({'$and': [{'home_province': home_province}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    try:
        province_list=await getAllProvince(db)

        province_dict={}
        for province in province_list:
            if province != "":
                pr=province.lower()
                n_man = db.subscriptions.count_documents({'$and': [{'home_province': pr}, {'gender': 'm'}]})
                province_dict[province]=n_man
        logging.warning('-----Method finish whit success------')
        return province_dict
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    try:
        man = db.subscriptions.count_documents({'$and': [{'study_province': ''}, {'gender': 'm'}]})
        logging.warning('-----Method finish whit success------')
        return man
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfManStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    try:
        province_list=await getAllProvince(db)
        total=0
        for province in province_list:
            if province != "":
                pr = province.lower()
                n_man =db.subscriptions.count_documents({'$and': [{'study_province': pr}, {'gender': 'm'}]})
                total = total + n_man
        logging.warning('-----Method finish whit success------')
        return total
    except:
        logging.error("Exception occurred", exc_info=True)
#endregion

#region ---WOMAN QUERY---
async def getNumberOfWomanByCourseAndUni(course, uni, db):
    try:
     #recupero numero maschi in un corso
        woman=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}, {'gender':'f'}]})
        logging.warning('-----Method finish whit success------')
        return  woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanByCourse(course, db):
    try:
        #recupero numero maschi in un corso
        woman = db.subscriptions.count_documents({'$and': [ {'degree_course': course}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanByUNi(uni, db):
    try:
        #recupero numero maschi in un università
        woman = db.subscriptions.count_documents({'$and': [{'university': uni}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanWhitSameProvinceOfUni(uni, db):
    try:
        #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
        province=await getProvinceByUni(uni, db)
        woman = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanWhitSameRegionOfUni(uni, db):
    try:
        #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
        region=await getRegionByUni(uni, db)
        woman = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanByRegion(home_region, db):
    try:
        #recupero numero maschi in una regione iscritti all'uni
        woman = db.subscriptions.count_documents({'$and': [{'home_region': home_region}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanGroupbyRegion(db):
    try:
        #da che regione provengono i ragazzi che studiano all'uni
        region_list=await getAllRegion(db)
        region_dict={}
        for region in region_list:
            if region != "":
                n_woman = db.subscriptions.count_documents({'$and': [{'home_region': region}, {'gender': 'f'}]})
                region_dict[region]=n_woman
        logging.warning('-----Method finish whit success------')
        return region_dict
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanStudyatHomeRegion(db):
    try:
        #quanti sono i ragazzi che studiano nella loro regione di provenienza
        woman = db.subscriptions.count_documents({'$and': [{'study_region': ''}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanStudyOutsideRegion(db):
    try:
        #quanti sono i ragazzi che studiano fuori regione ragruppati per re
        region_list=await getAllRegion(db)
        total=0
        for region in region_list:
            if region != "":
                n_woman =db.subscriptions.count_documents({'$and': [{'study_region': region}, {'gender': 'f'}]})
                total = total + n_woman
        logging.warning('-----Method finish whit success------')
        return total
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanByProvince(home_province, db):
    try:
        #recupero numero maschi in una regione iscritti all'uni
        woman = db.subscriptions.count_documents({'$and': [{'home_province': home_province}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanGroupbyProvince(db):
    try:
        #da che regione provengono i ragazzi che studiano all'uni
        province_dict = {}
        province_list=await getAllProvince(db)
        for province in province_list:
            if province != "":
                pr = province.lower()
                n_man = db.subscriptions.count_documents({'$and': [{'home_province': pr}, {'gender': 'f'}]})
                province_dict[province]=n_man
        logging.warning('-----Method finish whit success------')
        return province_dict
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanStudyatHomeProvince(db):
    try:
        #quanti sono i ragazzi che studiano nella loro regione di provenienza
        woman = db.subscriptions.count_documents({'$and': [{'study_province': ''}, {'gender': 'f'}]})
        logging.warning('-----Method finish whit success------')
        return woman
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfWomanStudyOutsideProvince(db):
    try:
        #quanti sono i ragazzi che studiano fuori regione
        province_list=await getAllProvince(db)
        total=0
        for province in province_list:
            pr = province.lower()
            if province != "":
                n_woman =db.subscriptions.count_documents({'$and': [{'study_province': pr}, {'gender': 'f'}]})
                total = total + n_woman
        logging.warning('-----Method finish whit success------')
        return total
    except:
        logging.error("Exception occurred", exc_info=True)

#endregion

#region ---SUBSCRIBERS QUERY---

async def getNumberOfPeopleByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    try:
        people=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)
async def getNumberOfPeopleByCourse(course, db):
    #recupero numero maschi in un corso
    try:
        people = db.subscriptions.count_documents({'$and': [ {'degree_course': course}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleByUNi(uni, db):
    #recupero numero maschi in un università
    try:
        people = db.subscriptions.count_documents({'$and': [{'university': uni}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    try:
        province=await getProvinceByUni(uni, db)
        people = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    try:
        region=await getRegionByUni(uni, db)
        people = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleByRegion(home_region, db):
    #recupero numero maschi in una regione iscritti all'uni
    try:
        people = db.subscriptions.count_documents({'$and': [{'home_region': home_region}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)


async def getNumberOfPeopleGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    try:
        region_dict = {}
        region_list=await getAllRegion(db)
        for region in region_list:
            if region != "":
                n_man = db.subscriptions.count_documents({'$and': [{'home_region': region}]})
                region_dict[region]=n_man
        logging.warning('-----Method finish whit success------')
        return region_dict
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    try:
        people = db.subscriptions.count_documents({'$and': [{'study_region': ''}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione
    try:
        region_list=await getAllRegion(db)
        total=0
        for region in region_list:
            if region != "":
                n_man =db.subscriptions.count_documents({'$and': [{'study_region': region}]})
                total = total + n_man
        logging.warning('-----Method finish whit success------')
        return total
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    try:
        people = db.subscriptions.count_documents({'$and': [{'home_province': home_province}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    try:
        province_list=await getAllProvince(db)
        province_dict={}
        for province in province_list:
            if province != "":
                pr=province.lower()
                n_man = db.subscriptions.count_documents({'$and': [{'home_province': pr}]})
                province_dict[province]=n_man
        logging.warning('-----Method finish whit success------')
        return province_dict
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    try:
        people = db.subscriptions.count_documents({'$and': [{'study_province': ''}]})
        logging.warning('-----Method finish whit success------')
        return people
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfPeopleStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    try:
        province_list= await getAllProvince(db)
        total=0
        for province in province_list:
            if province != "":
                pr = province.lower()
                n_man =db.subscriptions.count_documents({'$and': [{'study_province': pr}]})
                total = total + n_man
        logging.warning('-----Method finish whit success------')
        return total
    except:
        logging.error("Exception occurred", exc_info=True)
#endregion

#region --AVERAGE QUERY--
async def getMarkAveragebyCourse(course, uni, db):
    try:
        dictionary=db.subscriptions.find({'$and':
           [{'university': uni },
            {'degree_course': course}]})
        avg=average_dict(dictionary, 'average_grade', 18)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

async def getMarkAveragebyCourseAndYear(course, uni, year,  db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                          [{'university': uni},
                                           {'degree_course': course},
                                           {'degree_year': year}
                                           ]})
        avg = average_dict(dictionary, 'average_grade', 18)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

async def getGradeAveragebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                          [{'university': uni},
                                           {'degree_course': course}
                                           ]})
        avg = average_dict(dictionary, 'graduation_grade', 60)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)


async def getDurationAveragebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                          [{'university': uni},
                                           {'degree_course': course}
                                           ]})
        duration = set()
        avg=0
        for i in dictionary:
            if int(i['end_year']) & int(i['enrolment_year']):
                if len(str(i['end_year']))==4 & len(str(i['enrolment_year']))==4:
                    difference=int(i['end_year'])-int(i['enrolment_year'])
                    if difference > 0:
                        duration.add(difference)
        if len(duration)>0:
            avg = average_list(duration)
            return fromFloatToYearAndMonth(avg)

        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)
        return "undefined"

async def getExamNotDoneAveragebyCourse(course, uni, db):
     try:
         dictionary = db.subscriptions.find({'$and':
                                                 [{'university': uni},
                                                  {'degree_course': course}
                                                  ]})
         avg = average_dict(dictionary, 'numb_exams_not_done', 1)
         logging.warning('-----Method finish whit success------')
         return avg
     except:
         logging.error("Exception occurred", exc_info=True)

async def getExamNotDoneAveragebyCourseAndYear(course, uni,  year, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course},
                                                 {'degree_year': year}
                                                 ]})
        avg = average_dict(dictionary, 'numb_exams_not_done', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)
#endregion

#region ---REVIEW QUERY---
async def getReviewListbyCourse(course, uni, db):
    try:
        review_list=[]
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        for i in dictionary:
            if i['review'] !="":
                review_dict={}
                review_dict['review']=i['review']
                review_dict['stars'] = i['stars']
                review_list.append(review_dict)
        logging.warning('-----Method finish whit success------')
        return review_list
    except:
        logging.error("Exception occurred", exc_info=True)

async def getReviewListbyCourseAndYear(course, uni, year,  db):
    try:
        review_list = set()
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course},
                                                 {'degree_year': year}
                                                 ]})
        for i in dictionary:
            if i['review'] != "":
                review_list.add(i['review'])
        logging.warning('-----Method finish whit success------')
        return review_list
    except:
        logging.error("Exception occurred", exc_info=True)

async def getReviewAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'stars', 0)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

async def getReviewAverangebyCourseAndYear(course, uni, year,  db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course},
                                                 {'degree_year': year}
                                                 ]})
        avg = average_dict(dictionary, 'stars', 0)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

async def getReviewAverangebyUni(uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni}
                                                 ]})
        avg = average_dict(dictionary, 'stars', 0)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

#endregion

#region ---EVALUTATIONS---
async def getDidacticQualityAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'didactic_quality', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)


async def getTeachingQualityAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'teaching_quality', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)


async def getExamDifficultAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'exams_difficulties', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

async def getSubjectsDifficultAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'subjects_difficulties', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

async def getEnviromentalQualityAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'environment_quality', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)

async def getStudentsRelationshipAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'students_relationship', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)
#endregion

async def getDateOfLastSubscription(db):
    try:
        dictionary = db.subscriptions.find({})
        df=pd.DataFrame()
        date_list=set()
        for dict in dictionary:
            date_str= dict['subscription_date']
            dto = datetime.strptime(date_str, '%d-%m-%Y').date()
            date_list.add(dto)
        most_recent=max(date_list)
        logging.warning('-----Method finish whit success------')
        return most_recent
    except:
        logging.error("Exception occurred", exc_info=True)



async def getSubscriptionsByDate(date, db):
    try:
        dictionary = db.subscriptions.find({'subscription_date': date})
        logging.warning('-----Method finish whit success------')
        return dictionary
    except:
        logging.error("Exception occurred", exc_info=True)


async def getLaboratoryAverangebyCourse(course, uni, db):
    try:
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        avg = average_dict(dictionary, 'laboratories', 1)
        logging.warning('-----Method finish whit success------')
        return avg
    except:
        logging.error("Exception occurred", exc_info=True)


#TODO: da testare in python
async def getDifficultAspectList(course, uni, db):
    try:
        difficult_list=set()
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        for item in dictionary:
            value=item['difficult_aspect']
            if value != "":
                difficult_list.add(value)
        logging.warning('-----Method finish whit success------')
        return difficult_list
    except:
        logging.error("Exception occurred", exc_info=True)


async def getCountRedoChoice(course, uni, db):
    #Quanti studenti rifarebbero la scelta
    try:

        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        sum = 0
        for item in dictionary:
            value = item['redo_choice']
            if value == "si":
                sum = sum +1
        logging.warning('-----Method finish whit success------')
        return sum
    except:
        logging.error("Exception occurred", exc_info=True)

async def getNumberOfStudentsGoToErasmusByCourse(course, uni, db):
    #Contare quanti hanno fatto un esperienza all'estero
    try:
        sum = 0
        dictionary = db.subscriptions.find({'$and':
                                                [{'university': uni},
                                                 {'degree_course': course}
                                                 ]})
        for item in dictionary:
            value = item['abroad_experience']
            if value == "si":
                sum =sum +1
        logging.warning('-----Method finish whit success------')
        return sum
    except:
        logging.error("Exception occurred", exc_info=True)


async def getNumberOfStudentsGoToErasmusByUni(uni, db):
    try:
        sum = 0
        dictionary = db.subscriptions.find({'university': uni})
        for item in dictionary:
            value = item['abroad_experience']
            if value == "si":
                sum = sum +1
        logging.warning('-----Method finish whit success------')
        return sum
    except:
        logging.error("Exception occurred", exc_info=True)

#TODO: da testare in python

async def getNumberOfStudentsChangeThisDegree(course, uni, db):
    #Quanti studenti avevano già fatto una precedente carriera incompleta
    try:
        count= db.subscriptions.count_documents({'$and':
                                                [{'prev_change_uni': uni},
                                                 {'prev_change_degree_course': course}
                                                 ]})
        logging.warning('-----Method finish whit success------')
        return count
    except:
        logging.error("Exception occurred", exc_info=True)


async def addReviewOfMachineLearning(predict_review, db):
    #aggiungo la recesione sull'algoritmo
    try:
        db.predict_review.insert_one(predict_review)  # student_info is a dict
        logging.warning('-----Method finish whit success------')
        return True
    except:
        logging.error("Exception occurred", exc_info=True)
        return False

async def restartCalucatedModule(db):
    #ricalcolo il modulo python
    try:
        getAllStudents(db)
        getAllGraduates(db)
        save_best_model()
        logging.warning('-----Method finish whit success------')
        return True
    except:
        logging.error("Exception occurred", exc_info=True)
        return False

#endregion