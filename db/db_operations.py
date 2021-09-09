import pandas as pd
import pymongo
from bson.json_util import *
from commons_func.generic_func import  *
from datetime import datetime
from model import *

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
async def addNewStudent(student_info, db):
    try:
        db.students.insert_one(student_info) #student_info is a dict
        return True
    except:
        print(e)
        return False

async def addNewGraduate(graduate_info, db):
    try:
        db.graduates.insert_one(graduate_info) #graduate_info is a dict
        return True
    except:
        print(e)
        return False

async def addNewSubscriptions(subscriptions_info, db):
    try:
        db.subscriptions.insert_one(subscriptions_info)
        return True
    except Exception as e:
        print(e)
        return False


'''
--------------------------
SELECT METHOD
--------------------------
'''
#todo: fai le api di questa parte, ci servono per fare l'aggiornamento automatico quando inseriamo un nuovo utente dei file
def getAllStudents(db):
    try:
        cursor=db.students.find({})
    except:
        print('Error to get students from db')
    df=pd.read_json(dumps(cursor))
    df = df.iloc[:, 1:]
    df.to_json('doc/students_original_dataset.json')


def getAllGraduates(db):
    try:
        cursor=db.graduates.find({})
    except:
        print('Error to get graduates from db')
    df=pd.read_json(dumps(cursor))
    df = df.iloc[:, 1:]
    df.to_json('doc/graduates_original_dataset.json')

def getAllSubscription(db):
    try:
        cursor=db.subscriptions.find({})
    except:
        print('Error to get graduates from db')
    df=pd.read_json(dumps(cursor))
    df = df.iloc[:, 1:]
    df.to_json('doc/subscriptions_original_dataset.json')



async def getAllUni(db):
    #recupero tutte le università del database ( sia studenti che laureati)
    uni_list = set()
    try:
        cursor = db.subscriptions.distinct('university')
        for item in cursor:
            if item !="":
                uni_list.add(item)
        return uni_list
    except Exception as e:
        print(e)

async def getAllUnByCourse(course, db):
    #recupero tutte le università che hanno quel corso di laurea ( sia studenti che laureati)
    uni_list = set()
    try:
        cursor = db.subscriptions.distinct('university', {"degree_course": course})
        for item in cursor:
            if item != "":
                uni_list.add(item)
        return uni_list
    except Exception as e:
        print(e)

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
        return uni_list
    except Exception as e:
        print(e)

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
        return uni_list
    except Exception as e:
        print(e)

async def getAllCourse(db):
    #recupero tutti i corsi del db ( sia studenti che laureati)
    degree_course_list = set()
    try:
        cursor = db.subscriptions.distinct('degree_course')
        for item in cursor:
            if item not in degree_course_list:
                if item != "":
                    degree_course_list.add(item)
        return degree_course_list

    except Exception as e:
        print(e)

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
        return degree_course_list
    except Exception as e:
        print(e)

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
        return region_list
    except Exception as e:
        print(e)

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

    except Exception as e:
        print(e)

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
        return province_list
    except Exception as e:
        print(e)
        return province_list

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
                            return item
                else:
                    print(item)
                    return item
        else:
            item= 'NO PROVINCE FOUND'
            return item

    except Exception as e:
        print(e)



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
        return subject_list
    except Exception as e:
        print(e)
        return subject_list

async def getAllSubjectByUni(course,  uni, db):
    #recupero tutte le materie dato un corso specifico di un università
    subject_list = set()
    try:
        cursor = db.subscriptions.distinct('subject_area',  {'$and': [{"degree_course": course},{"university": uni}]})
        for i in cursor:
            list= i.split(',')
            for item in list:
                if item not in subject_list:
                    if item != "":
                        subject_list.add(item)
        return subject_list
    except Exception as e:
        print(e)
        return subject_list


async def getAllEasyExam(course, uni, db):
    #recupero tutte gli esami facili dato un corso di un'università
    exams_list = set()
    try:
        easy_exam = db.subscriptions.distinct('easy_exams',{'$and': [{"university": uni}, {'degree_course': course}]})
        for exams in easy_exam:
            list= exams.split(',')
            for item in list:
                if item.strip() not in exams_list:
                    if item.strip != "":
                        exams_list.add(item.strip())
        return exams_list
    except Exception as e:
        print(e)
        return exams_list

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
                    if item.strip != "":
                        exams_list.add(item.strip())
        return exams_list
    except Exception as e:
        print(e)
        return exams_list

'''
MAN QUERY
'''
async def getNumberOfManByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    man=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}, {'gender':'m'}]})
    return man

async def getNumberOfManByCourse(course, db):
    #recupero numero maschi in un corso
    man = db.subscriptions.count_documents({'$and': [ {'degree_course': course}, {'gender': 'm'}]})
    return man

async def getNumberOfManByUNi(uni, db):
    #recupero numero maschi in un università
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'gender': 'm'}]})
    return man

async def getNumberOfManWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    province=await getRegionByUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}, {'gender': 'm'}]})
    return man

async def getNumberOfManWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    region=await getRegionByUni(uni, db)
    man = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}, {'gender': 'm'}]})
    return man

async def getNumberOfManByRegion(home_region, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_region': home_region}, {'gender': 'm'}]})
    return man

async def getNumberOfManGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    region_list=await getAllRegion(db)
    region_dict={}
    for region in region_list:
        if region != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_region': region}, {'gender': 'm'}]})
            region_dict[region]=n_man
    return region_dict

async def getNumberOfManStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_region': ''}, {'gender': 'm'}]})
    return man

async def getNumberOfManStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione ragruppati per re
    region_list=await getAllRegion(db)
    total=0
    for region in region_list:
        if region != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_region': region}, {'gender': 'm'}]})
            total = total + n_man
    return total

async def getNumberOfManByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    man = db.subscriptions.count_documents({'$and': [{'home_province': home_province}, {'gender': 'm'}]})
    return man

async def getNumberOfManGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    province_list=await getAllProvince(db)
    province_dict={}
    for province in province_list:
        if province != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_province': province}, {'gender': 'm'}]})
            province_dict[province]=n_man
    return province_dict

async def getNumberOfManStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    man = db.subscriptions.count_documents({'$and': [{'study_province': ''}, {'gender': 'm'}]})
    return man

async def getNumberOfManStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    province_list=await getAllProvince(db)
    total=0
    for province in province_list:
        if province != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_province': province}, {'gender': 'm'}]})
            total = total + n_man
    return total



'''
WOMAN QUERY
'''
async def getNumberOfWomanByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    woman=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}, {'gender':'f'}]})
    return  woman
async def getNumberOfWomanByCourse(course, db):
    #recupero numero maschi in un corso
    woman = db.subscriptions.count_documents({'$and': [ {'degree_course': course}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanByUNi(uni, db):
    #recupero numero maschi in un università
    woman = db.subscriptions.count_documents({'$and': [{'university': uni}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    province=await getProvinceByUni(uni, db)
    woman = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    region=await getRegionByUni(uni, db)
    woman = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanByRegion(home_region, db):
    #recupero numero maschi in una regione iscritti all'uni
    woman = db.subscriptions.count_documents({'$and': [{'home_region': home_region}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    region_list=await getAllRegion(db)
    region_dict={}
    for region in region_list:
        if region != "":
            n_woman = db.subscriptions.count_documents({'$and': [{'home_region': region}, {'gender': 'f'}]})
            region_dict[region]=n_woman
    return region_dict

async def getNumberOfWomanStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    woman = db.subscriptions.count_documents({'$and': [{'study_region': ''}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione ragruppati per re
    region_list=await getAllRegion(db)
    total=0
    for region in region_list:
        if region != "":
            n_woman =db.subscriptions.count_documents({'$and': [{'study_region': region}, {'gender': 'f'}]})
            total = total + n_woman
    return total

async def getNumberOfWomanByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    woman = db.subscriptions.count_documents({'$and': [{'home_province': home_province}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    province_dict = {}
    province_list=await getAllProvince(db)
    for province in province_list:
        if province != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_province': province}, {'gender': 'f'}]})
            province_dict[province]=n_man
    return province_dict

async def getNumberOfWomanStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    woman = db.subscriptions.count_documents({'$and': [{'study_province': ''}, {'gender': 'f'}]})
    return woman

async def getNumberOfWomanStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    province_list=await getAllProvince(db)
    total=0
    for province in province_list:
        if province != "":
            n_woman =db.subscriptions.count_documents({'$and': [{'study_province': province}, {'gender': 'f'}]})
            total = total + n_woman
    return total



'''
SUBSCRIBERS QUERY
'''
async def getNumberOfPeopleByCourseAndUni(course, uni, db):
    #recupero numero maschi in un corso
    people=db.subscriptions.count_documents({'$and': [{"university": uni}, {'degree_course': course}]})
    return people
async def getNumberOfPeopleByCourse(course, db):
    #recupero numero maschi in un corso
    people = db.subscriptions.count_documents({'$and': [ {'degree_course': course}]})
    return people

async def getNumberOfPeopleByUNi(uni, db):
    #recupero numero maschi in un università
    people = db.subscriptions.count_documents({'$and': [{'university': uni}]})
    return people

async def getNumberOfPeopleWhitSameProvinceOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA PROVINCIA DELL'UNI)
    province=await getProvinceByUni(uni, db)
    people = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_province': province}]})
    return people

async def getNumberOfPeopleWhitSameRegionOfUni(uni, db):
    #recupero numero maschi in un università che NON SONO FUORISEDE (STESSA REGIONE DELL'UNI)
    region=await getRegionByUni(uni, db)
    people = db.subscriptions.count_documents({'$and': [{'university': uni}, {'home_region': region}]})
    return people

async def getNumberOfPeopleByRegion(home_region, db):
    #recupero numero maschi in una regione iscritti all'uni
    people = db.subscriptions.count_documents({'$and': [{'home_region': home_region}]})
    return people


async def getNumberOfPeopleGroupbyRegion(db):
    #da che regione provengono i ragazzi che studiano all'uni
    region_dict = {}
    region_list=await getAllRegion(db)
    for region in region_list:
        if region != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_region': region}]})
            region_dict[region]=n_man
    return region_dict

async def getNumberOfPeopleStudyatHomeRegion(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    people = db.subscriptions.count_documents({'$and': [{'study_region': ''}]})
    return people

async def getNumberOfPeopleStudyOutsideRegion(db):
    #quanti sono i ragazzi che studiano fuori regione
    region_list=await getAllRegion(db)
    total=0
    for region in region_list:
        if region != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_region': region}]})
            total = total + n_man
    return total

async def getNumberOfPeopleByProvince(home_province, db):
    #recupero numero maschi in una regione iscritti all'uni
    people = db.subscriptions.count_documents({'$and': [{'home_province': home_province}]})
    return people

async def getNumberOfPeopleGroupbyProvince(db):
    #da che regione provengono i ragazzi che studiano all'uni
    province_list=await getAllProvince(db)
    province_dict={}
    for province in province_list:
        if province != "":
            n_man = db.subscriptions.count_documents({'$and': [{'home_province': province}]})
            province_dict[province]=n_man
    return province_dict

async def getNumberOfPeopleStudyatHomeProvince(db):
    #quanti sono i ragazzi che studiano nella loro regione di provenienza
    people = db.subscriptions.count_documents({'$and': [{'study_province': ''}]})
    return people

async def getNumberOfPeopleStudyOutsideProvince(db):
    #quanti sono i ragazzi che studiano fuori regione
    province_list= await getAllProvince(db)
    total=0
    for province in province_list:
        if province != "":
            n_man =db.subscriptions.count_documents({'$and': [{'study_province': province}]})
            total = total + n_man
    return total


async def getMarkAveragebyCourse(course, uni, db):
    dictionary=db.subscriptions.find({'$and':
       [{'university': uni },
        {'degree_course': course}]})
    avg=average_dict(dictionary, 'average_grade')
    return avg

async def getMarkAveragebyCourseAndYear(course, uni, year,  db):
    dictionary = db.subscriptions.find({'$and':
                                      [{'university': uni},
                                       {'degree_course': course},
                                       {'degree_year': year}
                                       ]})
    avg = average_dict(dictionary, 'average_grade')
    return avg

async def getGradeAveragebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                      [{'university': uni},
                                       {'degree_course': course}
                                       ]})
    avg = average_dict(dictionary, 'graduation_grade')
    return avg


async def getDurationAveragebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                      [{'university': uni},
                                       {'degree_course': course}
                                       ]})
    duration = set()
    avg=0
    for i in dictionary:
        if int(i['end_year']) & int(i['enrolment_year']):
            if len(str(i['end_year']))==4 & len(str(i['enrolment_year']))==4:
                difference=i['end_year']-i['enrolment_year']
                duration.add(difference)
    if len(duration)>0:
        avg = average_list(duration)
        return fromFloatToYearAndMonth(avg)
    return avg

async def getExamNotDoneAveragebyCourse(course, uni, db):
     dictionary = db.subscriptions.find({'$and':
                                             [{'university': uni},
                                              {'degree_course': course}
                                              ]})
     avg = average_dict(dictionary, 'numb_exams_not_done')
     return avg

async def getExamNotDoneAveragebyCourseAndYear(course, uni,  year, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course},
                                             {'degree_year': year}
                                             ]})
    avg = average_dict(dictionary, 'numb_exams_not_done')
    return avg


async def getReviewListbyCourse(course, uni, db):
    review_list=set()
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    for i in dictionary:
        if i['review'] !="":
            review_list.add(i['review'])
    return review_list

async def getReviewListbyCourseAndYear(course, uni, year,  db):
    review_list = set()
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course},
                                             {'degree_year': year}
                                             ]})
    for i in dictionary:
        if i['review'] != "":
            review_list.add(i['review'])
    return review_list

async def getReviewAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'stars')
    return avg

async def getReviewAverangebyCourseAndYear(course, uni, year,  db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course},
                                             {'degree_year': year}
                                             ]})
    avg = average_dict(dictionary, 'stars')
    return avg

async def getReviewAverangebyUni(uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni}
                                             ]})
    avg = average_dict(dictionary, 'stars')
    return avg

async def getDidacticQualityAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'didactic_quality')
    return avg

async def getTeachingQualityAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'teaching_quality')
    return avg

async def getExamDifficultAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'exams_difficulties')
    return avg

async def getSubjectsDifficultAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'subjects_difficulties')
    return avg

async def getEnviromentalQualityAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'environment_quality')
    return avg

async def getStudentsRelationshipAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'students_relationship')
    return avg


async def getDateOfLastSubscription(db):
    dictionary = db.subscriptions.find({})
    df=pd.DataFrame()
    date_list=set()
    for dict in dictionary:
        date_str= dict['subscription_date']
        dto = datetime.strptime(date_str, '%d-%m-%Y').date()
        date_list.add(dto)
    most_recent=max(date_list)
    return most_recent


async def getSubscriptionsByDate(date, db):
    dictionary = db.subscriptions.find({'subscription_date': date})
    return dictionary


async def getLaboratoryAverangebyCourse(course, uni, db):
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    avg = average_dict(dictionary, 'laboratory')
    return avg


#TODO: da testare in python
async def getDifficultAspectList(course, uni, db):
    difficult_list=set()
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    for item in dictionary:
        value=item['difficult_aspect']
        if value != "":
            difficult_list.add(value)
    return difficult_list


async def getCountRedoChoice(course, uni, db):
    #Quanti studenti rifarebbero la scelta
    sum=0
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    for item in dictionary:
        value = item['redo_choice']
        if value == "si":
            sum =+1
    return sum

async def getNumberOfStudentsGoToErasmusByCourse(course, uni, db):
    #Contare quanti hanno fatto un esperienza all'estero
    sum = 0
    dictionary = db.subscriptions.find({'$and':
                                            [{'university': uni},
                                             {'degree_course': course}
                                             ]})
    for item in dictionary:
        value = item['abroad_experience']
        if value == "si":
            sum = +1
    return sum


async def getNumberOfStudentsGoToErasmusByUni(uni, db):
    sum = 0
    dictionary = db.subscriptions.find({'university': uni})
    for item in dictionary:
        value = item['abroad_experience']
        if value == "si":
            sum = +1
    return sum

#TODO: da testare in python

async def getNumberOfStudentsChangeThisDegree(course, uni, db):
    #Quanti studenti avevano già fatto una precedente carriera incompleta
    count= db.subscriptions.count_documents({'$and':
                                            [{'prev_change_uni': uni},
                                             {'prev_change_degree_course': course}
                                             ]})
    return count


async def addReviewOfMachineLearning(predict_review, db):
    #aggiungo la recesione sull'algoritmo
    try:
        db.predict_review.insert_one(predict_review)  # student_info is a dict
        return True
    except:
        print(e)
        return False

async def restartCalucatedModule(db):
    #ricalcolo il modulo python
    try:
        getAllStudents(db)
        getAllGraduates(db)
        save_best_model()
        return True
    except:
        print(e)
        return False