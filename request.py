import pandas as pd
from cleaning_data import *
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from feature_engineering import *
from commons_func.logging_config import *
import joblib

def set_request(high_school, subject, prefered_subject, hobby, work_dream, aspectations_uni, decision_choice_uni, continuos_study):
    try:
        df_answer = pd.DataFrame([high_school, subject, prefered_subject, hobby, work_dream, aspectations_uni, decision_choice_uni, continuos_study]).transpose()
        df_answer.columns = ['high_school', 'subject', 'prefered_subject', 'hobby', 'work_dream', 'aspectations_uni', 'decision_choice_uni', 'continuos_study']
        logging.warning('-----Method finish whit success------')
        return df_answer
    except:
        logging.error("Exception occurred", exc_info=True)

def clean_request(df_answer):
    #TODO SE UNO LASCIA UN CAMPO VUOTO COSA SUCCEDE? NON PUO' LASCIARLO!
    try:
        df_answer_clean = df_answer.copy()
        categorical_features_answer = ['high_school', 'continuos_study']
        regex_features = [r'\s\s+']  # delete black space
        for feature in df_answer_clean.columns:
            df_answer_clean[feature] = data_cleaning(df_answer_clean[feature], regex_features)
            if feature not in categorical_features_answer:
                df_answer_clean[feature] = preprocessing_text(df_answer_clean, df_answer_clean[feature], feature,  'IT')
        logging.warning('-----Method finish whit success------')
        return df_answer_clean
    except:
        logging.error("Exception occurred", exc_info=True)

def hot_encoding(encoder, df, label):
    try:
        number= 0
        for class_ in encoder.classes_:
            for value in df[label]:
                if class_ == value:
                    df[label] = number
                else:
                    number += 1
        logging.warning('-----Method finish whit success------')
        return df
    except:
        logging.error("Exception occurred", exc_info=True)

def reverse_bag_of_word(df):
    try:
        vectorizer_train = joblib.load('doc/bag_of_word_model')
        df['bag_of_words'] = df[['subject', 'hobby', 'prefered_subject', 'work_dream']].values.tolist()
        for index in df['bag_of_words'].index:
            item = df['bag_of_words'].iloc[index]
            listToStr = ' '.join([str(i) for i in item])
            df['bag_of_words'].iloc[index] = listToStr
        msg_array = vectorizer_train.transform(df['bag_of_words']).toarray()
        vocab = vectorizer_train.get_feature_names()
        df_bow_answer = pd.DataFrame(msg_array, columns=vocab)
        df = df.drop(['subject', 'hobby', 'prefered_subject', 'work_dream', 'bag_of_words'], axis=1)
        # add the new columns
        df = df.set_index(df_bow_answer.index)
        df = pd.concat([df, df_bow_answer], axis=1)
        logging.warning('-----Method finish whit success------')
        return df
    except:
        logging.error("Exception occurred", exc_info=True)


def reverse_td_if(df):
    try:
        tv = joblib.load('doc/tf_id_model')
        df['tf_if'] = df[['aspectations_uni', 'decision_choice_uni']].values.tolist()
        for index in df['tf_if'].index:
            item = df['tf_if'].iloc[index]
            listToStr = ' '.join([str(i) for i in item])
            df['tf_if'].iloc[index] = listToStr
        msg_array_tf = tv.transform(df['tf_if']).toarray()
        vocab = tv.get_feature_names()
        df_tf_answer = pd.DataFrame(msg_array_tf, columns=vocab)
        # delete the old columns
        df = df.drop(['aspectations_uni', 'decision_choice_uni', 'tf_if'], axis=1)
        df = df.set_index(df_tf_answer.index)
        df = pd.concat([df, df_tf_answer], axis=1)
        logging.warning('-----Method finish whit success------')
        return df
    except:
        logging.error("Exception occurred", exc_info=True)

def feature_engireering_request(high_school, subject, prefered_subject, hobby, work_dream, aspectations_uni, decision_choice_uni, continuos_study):
    try:
        encoder_choice= joblib.load('doc/encoder_choice_model')
        encoder_school = joblib.load('doc/encoder_school_model')
        df_request = set_request(high_school, subject, prefered_subject, hobby, work_dream, aspectations_uni, decision_choice_uni, continuos_study)
        logging.warning(f'REQUEST VALUE: {df_request.values}')
        df_request_clean = clean_request(df_request)
        logging.warning(f'REQUEST VALUE CLEANS: {df_request_clean.values}')
        df_request_clean = hot_encoding(encoder_choice, df_request_clean, 'continuos_study')
        df_request_clean= hot_encoding(encoder_school, df_request_clean, 'high_school')
        logging.warning(f'REQUEST VALUE ENCODING CATEGORICAL: {df_request_clean.values}')
        df_after_bof = reverse_bag_of_word(df_request_clean)
        print(df_after_bof.values)
        df_after_tfid = reverse_td_if(df_after_bof)
        logging.warning(f'REQUEST VALUE AFTER FEAURES ENGIN: {df_after_tfid.values}')
        logging.warning(f'REQUEST VALUE AFTER FEAURES ENGIN=>shape: {df_after_tfid.shape}')
        logging.warning('-----Method finish whit success------')
        return df_after_tfid
    except:
        logging.error("Exception occurred", exc_info=True)


async def predict_request(high_school, subject, prefered_subject, hobby, work_dream, aspectations_uni, decision_choice_uni, continuos_study):
    try:
        logging.warning('****START PREDICT****')
        df_request = feature_engireering_request(high_school, subject, prefered_subject, hobby, work_dream, aspectations_uni, decision_choice_uni, continuos_study)
        model = joblib.load('doc/model')
        prediction_uni = model.predict(df_request.values)
        for i in prediction_uni:
            uni = i
        print(uni)
        #RECUPERO LAUREE DATO CLUSTER
        cluster_labels_degree_course = pd.read_json('doc/cluster_labels_degree_course.json')
        df2 = cluster_labels_degree_course[cluster_labels_degree_course['ClusterLabel'] == uni]['full_degree_course']
        print(df2)
        logging.warning('-----Method finish whit success------')
        return  df2.to_dict()
    except:
        logging.error("Exception occurred", exc_info=True)