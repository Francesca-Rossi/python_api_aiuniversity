from cleaning_data import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from commons_func.feature_engineering import *
from commons_func.logging_config import  *
import joblib

def create_clustering_degree_course():
    try:
        df_clean_features = cleaning_character_features()
        original_df_whitout_nan_value= get_originl_df_after_managing_all_missing_value()
        # text analysis
        tv = TfidfVectorizer(min_df=0., max_df=1., use_idf=True)
        vectorize_matrix = tf_vector(tv, df_clean_features['degree_course'])

        # cosine similarity
        similarity_matrix = cosine_similarity(vectorize_matrix)
        similarity_df = pd.DataFrame(similarity_matrix)
        logging.warning('Finish create SIMILARITY MATRIX')

        # clustering
        km = KMeans(n_clusters=120, random_state=0)
        km.fit_transform(similarity_df)
        filename = 'doc/degree_cluster_model'
        joblib.dump(km, filename)
        cluster_labels = km.labels_
        cluster_labels_degree_course = pd.DataFrame(cluster_labels, columns=['ClusterLabel'])
        df_clean_features = df_clean_features.set_index(
            cluster_labels_degree_course.index)  # avoids NAN values ​​coming out due to different indexes
        cluster_labels_degree_course.insert(0, 'degree_course', df_clean_features['degree_course'], True)
        original_df_whitout_nan_value = original_df_whitout_nan_value.set_index(
            cluster_labels_degree_course.index)  # avoids NAN values ​​coming out due to different indexes
        cluster_labels_degree_course.insert(0, 'full_degree_course', original_df_whitout_nan_value['degree_course'], True)
        byCluster = cluster_labels_degree_course.groupby(['ClusterLabel'])
        cluster_labels_degree_course.to_json('doc/cluster_labels_degree_course.json')  # salvo nel documento json

        # DEBUG: print all the cluster
        labels = []
        for cluster, degree in byCluster:
            logging.warning(f"All entries for {cluster!r}")
            logging.warning("------------------------")
            logging.warning(f"All entries for {degree}")  # display(degree)

            labels.append(degree['full_degree_course'].iloc[0])
        logging.warning(labels)

        # put the cluster result inside the dataset

        df_clean_features = df_clean_features.set_index(cluster_labels_degree_course.index)
        df_clean_features['degree_course'] = cluster_labels_degree_course['ClusterLabel']
        # DEBUG
        logging.warning('check if add missing values: %s', df_clean_features['degree_course'].isnull().sum())
        logging.warning('-----Method finish whit success------')
        return df_clean_features
    except:
        logging.error("Exception occurred", exc_info=True)


def encoding_categorical_features():
    try:
        df_clean_features = create_clustering_degree_course()
        encoder_school = LabelEncoder()
        encoder_choice = LabelEncoder()
        for feature in CATEGORICAL_FEATURES:
            print(feature)
            if feature == 'high_school':
              school_labels = encoder_school.fit_transform( df_clean_features[feature])
              df_clean_features[feature]=one_hot_encoding( df_clean_features[feature], feature, school_labels, encoder_school )
            if feature == 'choice_related_studies':
              choice_labels = encoder_choice.fit_transform(df_clean_features[feature])
              df_clean_features[feature]=one_hot_encoding( df_clean_features[feature], feature, choice_labels,encoder_choice )

        joblib.dump(encoder_choice, 'doc/encoder_choice_model')
        joblib.dump(encoder_school, 'doc/encoder_school_model')
        logging.warning('-----Method finish whit success------')
        return df_clean_features
    except:
        logging.error("Exception occurred", exc_info=True)


def bag_of_words_text_features():
    try:
        df_clean_features = encoding_categorical_features()
        # group all the columns in one columns using a list, the we convert the list in string
        df_clean_features['bag_of_words'] = df_clean_features[
            ['main_subject', 'hobby', 'favorite_subject', 'dream_job']].values.tolist()
        for index in df_clean_features['bag_of_words'].index:
            item = df_clean_features['bag_of_words'].iloc[index]
            listToStr = ' '.join([str(i) for i in item])
            df_clean_features['bag_of_words'].iloc[index] = listToStr
        # fit the model
        vectorizer_train = CountVectorizer(min_df=0, binary=True)
        df_bow_dict = bag_of_words(vectorizer_train, df_clean_features['bag_of_words'])
        # delete the old columns
        df_clean_features = df_clean_features.drop(
            ['main_subject', 'hobby', 'favorite_subject', 'dream_job', 'bag_of_words'], axis=1)
        print(df_clean_features.head()) # DEBUG
        # add the new columns
        df_clean_features = df_clean_features.set_index(df_bow_dict.index)
        df_clean_features = pd.concat([df_clean_features, df_bow_dict], axis=1)
        # DEBUG
        logging.warning('bag of words DF %s', df_clean_features.head())
        logging.warning('bag of words SHAPE %s', df_clean_features.shape)
        logging.warning('-----Method finish whit success------')
        return df_clean_features
    except:
        logging.error("Exception occurred", exc_info=True)

def tf_id_text_features():
    try:
        df_clean_features = bag_of_words_text_features()
        df_clean_features['tf_if'] = df_clean_features[['expectations', 'decision_choice']].values.tolist()
        for index in df_clean_features['tf_if'].index:
            item = df_clean_features['tf_if'].iloc[index]
            listToStr = ' '.join([str(i) for i in item])
            df_clean_features['tf_if'].iloc[index] = listToStr
        tv = TfidfVectorizer(min_df=0., max_df=1., use_idf=True)
        df_tf_id = tf_vector(tv, df_clean_features['tf_if'])
        print(df_tf_id)
        df_clean_features = df_clean_features.drop(['expectations', 'decision_choice', 'tf_if'], axis=1)
        df_clean_features = df_clean_features.set_index(df_tf_id.index)
        df_clean_features = pd.concat([df_clean_features, df_tf_id], axis=1)
        logging.warning('tf-id DF %s', df_clean_features.head())
        logging.warning('tf-id SHAPE %s', df_clean_features.shape)
        print(df_clean_features.isnull().sum())
        logging.warning('-----Method finish whit success------')
        return  df_clean_features
    except:
        logging.error("Exception occurred", exc_info=True)