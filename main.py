# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI,  HTTPException
from api.apiClass import  *
from api.man_request import  *
from api.woman_request import  *
from api.subscription_request import  *
from api.uni_request import *
from api.course_request import  *
from api.region_and_province_request import  *
from api.subject_request import *
from api.average_request import *
from api.review_request import  *
from api.evalutation_request import  *
from api.other_request import *
from api.post_api import *
from ai_model.recovery_data import *
from datetime import date
from commons_func.logging_config import *




















if __name__ == '__main__':

    #logging.warning('prova')
    '''# inserisco di nuovo tutto nel dataset
    today=date.today()
    date_today =  today.strftime("%d-%m-%Y")
    df_graduate = get_graduate_original_data()
    df_graduate_first_degree = df_graduate.query(query_first_degree)
    df_graduate_lower = df_graduate_first_degree.applymap(lambda s: s.lower() if type(s) == str else s)
    df_graduate_lower = df_graduate_first_degree.applymap(lambda s: s.strip() if type(s) == str else s)
    df_graduate_lower = df_graduate_lower.reset_index()
    df_graduate_lower = df_graduate_lower.iloc[:, 1:]
    df_graduate_lower['subscription_date'] = date_today
    for i in df_graduate_lower.index:
        df = df_graduate_lower.iloc[i]
        addNewGraduate(df.to_dict(), db)
        df['subscription_type'] = 'graduate'
        addNewSubscriptions(df.to_dict(), db)
        print(df.to_dict())
    df_students = get_students_original_data()
    df_students_first_degree = df_students.query(query_first_degree)
    df_students_lower = df_students_first_degree.applymap(lambda s: s.lower() if type(s) == str else s)
    df_students_lower = df_students_first_degree.applymap(lambda s: s.strip() if type(s) == str else s)
    df_students_lower = df_students_lower.reset_index()
    df_students_lower = df_students_lower.iloc[:, 1:]
    df_students_lower['subscription_date'] = date_today
    for i in df_students_lower.index:
        df = df_students_lower.iloc[i]
        addNewStudent(df.to_dict(), db)
        df['subscription_type'] = 'student'
        addNewSubscriptions(df.to_dict(), db)
        print(df.to_dict())'''