import gspread
import json as js
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
from commons_func.graphs import *
from commons_func.logging_config import  *

QUERY_FIRST_DEGREE= 'study_type == "Triennale" | study_type == "Magistrale_unico"'
FEATURES_FIRST_DEGREE=['degree_course', 'other_high_school', 'high_school', 'main_subject', 'favorite_subject', 'dream_job', 'hobby', 'decision_choice' , 'expectations', 'choice_related_studies']

#region  #CREATE DATASET
def get_sheet_from_google_cred():
    """#<h4>4) RECUPERO DEI DATI E COSTRUZIONE DATASET INIZIALE</h4>
      <p>I dati per la ricerca sono stati raccolti utilizzando un <b>form autoprodotto</b>, successivamente memorizzati all'interno di un <b>file google sheets</b>.</p>

      ## <h5><b>4.1) Connessione con il foglio di google</b></h5>
      """
    try:
        SCOPES = ["https://spreadsheets.google.com/feeds",
                  "https://www.googleapis.com/auth/spreadsheets",
                  "https://www.googleapis.com/auth/drive",
                  "https://www.googleapis.com/auth/drive"]
        cred = ServiceAccountCredentials.from_json_keyfile_name(
            "doc/GoogleSheetCredentials.json", SCOPES)
        gclient = gspread.authorize(cred)
        sheet = gclient.open_by_url(
            "https://docs.google.com/spreadsheets/d/1scMc0UlNC1pdZNow5k3pLhofcW6j4ekXyxYlNiBcueI/edit?usp=sharing")
        return sheet
    except:
        logging.error("Exception occurred", exc_info=True)

def get_students_original_data():
    try:
        sheet = get_sheet_from_google_cred()
        students_data = sheet.worksheet('Laureando').get_all_records()
        df_students = pd.DataFrame(students_data)
        print("students shape:", df_students.shape)
        df=df_students.apply(lambda col: col.str.lower())
        df.to_json('doc/students_original_dataset.json')  #salvo nel documento json //mi serve per node.js
        return df_students
    except:
        logging.error("Exception occurred", exc_info=True)

def get_graduate_original_data():
    try:
        sheet = get_sheet_from_google_cred()
        graduate_data = sheet.worksheet('Laureato').get_all_records()
        df_graduate = pd.DataFrame(graduate_data)
        print("graduates shape:", df_graduate.shape)
        df = df_graduate.apply(lambda col: col.str.lower())
        df_graduate.to_json('doc/graduates_original_dataset.json')  #salvo nel documento json
        return df_graduate
    except:
        logging.error("Exception occurred", exc_info=True)


def get_students_first_degree_dataset():
    '''Get the students first degree after managing missing value of original dataset'''
    try:
        df_students=get_students_data_after_manage_missing_values(False)
        df_students_first_degree = df_students.query(QUERY_FIRST_DEGREE)
        print('students first degree:', df_students_first_degree.shape)
        logging.warning('-----Method finish whit success------')
        return df_students_first_degree
    except:
        logging.error("Exception occurred", exc_info=True)

def get_graduate_first_degree_dataset():
    try:
        '''Get the students first degree after managing missing value of original dataset'''
        df_graduate = get_graduated_data_after_manage_missing_values(False)
        df_graduate_first_degree = df_graduate.query(QUERY_FIRST_DEGREE)
        print('graduates first degree:', df_graduate_first_degree.shape)
        logging.warning('-----Method finish whit success------')
        return df_graduate_first_degree
    except:
        logging.error("Exception occurred", exc_info=True)

def get_first_degree_complete_dataframe():
    '''Get the dataset after merge from students first degree dataset and graduate first degree dataset
    and select only our interested features'''
    try:
        df_all_features_first_degree = pd.DataFrame(get_first_degree_complete_dictionary())
        print('original sample first degree:', df_all_features_first_degree.shape[0])
        logging.warning('-----Method finish whit success------')
        return df_all_features_first_degree
    except:
        logging.error("Exception occurred", exc_info=True)

def get_first_degree_complete_dictionary():
    try:
        all_features_dict = {}
        df_students_first_degree = get_students_first_degree_dataset()
        df_graduate_first_degree = get_graduate_first_degree_dataset()
        for feature in FEATURES_FIRST_DEGREE:
            all_features = df_students_first_degree[feature]
            all_features = all_features.append(df_graduate_first_degree[feature], ignore_index=True, verify_integrity=True)
            all_features_dict[feature] = all_features
        logging.warning('-----Method finish whit success------')
        return  all_features_dict
    except:
        logging.error("Exception occurred", exc_info=True)
#endregion



#region #MANAGE_MISSING_VALUE
def get_students_data_after_manage_missing_values(show_graphs):
    try:
        df_students = pd.read_json("doc/students_original_dataset.json")
        df_students = df_students.replace('', np.NaN)
        df_missing_value_students = df_students.isnull().sum()
        print("Original students dataset missing value: \n", df_missing_value_students)
        if(show_graphs):
            missing_value_graphs(df_missing_value_students, df_students, 'Studenti')
        logging.warning('-----Method finish whit success------')
        return df_students #ritorno il vecchio dataset con le modifiche fatte
    except:
        logging.error("Exception occurred", exc_info=True)

def get_graduated_data_after_manage_missing_values(show_graphs):
    try:
        df_graduate = pd.read_json('doc/graduates_original_dataset.json')
        df_graduate = df_graduate.replace('', np.NaN)
        df_missing_value_graduate = df_graduate.isnull().sum()
        print("Original graduate dataset missing value: \n", df_missing_value_graduate)
        if(show_graphs):
            missing_value_graphs(df_missing_value_graduate, df_graduate, 'Laureati')
        logging.warning('-----Method finish whit success------')
        return df_graduate
    except:
        logging.error("Exception occurred", exc_info=True)


def get_first_degree_complete_dataset_after_delete_missing_value():
    try:
        all_features_dict = get_first_degree_complete_dictionary()
        df_all_features_first_degree = get_first_degree_complete_dataframe();
        for key in all_features_dict:
            if key != 'main_subject' and key != 'other_high_school':
                df_all_features_first_degree = df_all_features_first_degree[df_all_features_first_degree[key].notna()]
        print('sample first degree after delete null value:', df_all_features_first_degree.shape[0])
        logging.warning('-----Method finish whit success------')
        return df_all_features_first_degree
    except:
        logging.error("Exception occurred", exc_info=True)



def show_graphs_missing_value_first_degree_students():
    try:
        df_students_first_degree = get_students_first_degree_dataset()
        df_missing_value_first_degree_students = df_students_first_degree.isnull().sum()
        missing_value_graphs(df_missing_value_first_degree_students, df_students_first_degree,
                             'Studenti laurea primo livello')
        logging.warning('-----Method finish whit success------')
    except:
        logging.error("Exception occurred", exc_info=True)

def show_graphs_missing_value_first_degree_graduated():
    try:
        df_graduate_first_degree = get_graduate_first_degree_dataset()
        df_missing_value_first_degree_graduate = df_graduate_first_degree.isnull().sum()
        missing_value_graphs(df_missing_value_first_degree_graduate, df_graduate_first_degree,
                             'Laureati laurea primo livello')
        logging.warning('-----Method finish whit success------')
    except:
        logging.error("Exception occurred", exc_info=True)

#endregion




