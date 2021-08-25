from recovery_data import *
from commons_func.generic_func import *
from commons_func.cleaning_data import *
from commons_func.preprocessing_data import *


categorical_features=['high_school', 'choice_related_studies']
def main_subject_replace_missing_value():
    """Get complete dataframe after replace missing value of main subject features"""
    df_all_features_first_degree=get_first_degree_complete_dataset_after_delete_missing_value()
    school_whitout_subject = df_all_features_first_degree['high_school'].loc[df_all_features_first_degree['main_subject'].isnull()]

    full_subject = df_all_features_first_degree['main_subject']
    high_school = np.array(df_all_features_first_degree['high_school'])
    for x in school_whitout_subject:
        subject = np.array(df_all_features_first_degree['main_subject'].loc[df_all_features_first_degree['high_school'].str.contains(x, na=False)][0:1])
        for i in range(0, len(high_school)):
            if (high_school[i] == x):
                full_subject[i] = np.array2string(subject)
    df_all_features_first_degree['full_subject'] = full_subject

    # replace missing value in main subject whit the new value in full subject
    df_all_features_first_degree['main_subject'] = df_all_features_first_degree['main_subject'].combine_first(
        df_all_features_first_degree['full_subject'])
    print(df_all_features_first_degree[['main_subject', 'full_subject']].head(50))

    df_all_features_first_degree = df_all_features_first_degree.drop(['full_subject'],axis=1)  # eliminate the support column

    """Eliminazione eventuali valori nulli rimasti ed aggiunta al dizionario con il resto delle colonne pulite"""

    df_all_features_first_degree = df_all_features_first_degree[df_all_features_first_degree['main_subject'].notna()]  # delete null values
    print('sample first degree after delete null value:', df_all_features_first_degree.shape[0])
    return df_all_features_first_degree

def get_originl_df_after_managing_all_missing_value():
    '''Using during clustering for labeling deree course'''
    df_all_features_first_degree = main_subject_replace_missing_value()
    original_df_whitout_nan_value = df_all_features_first_degree.copy()
    return original_df_whitout_nan_value

def clean_degree_course():
    # acronimi
    slug_degree_course = get_slug_degree_course()

    regex_degree_course = [r'\sl.*[0-9]+', r'\scurriculum\s.*', r'indirizzo.*', r'[(].*[)]*', r'&', r'\s\s+',
                           r'corso di laurea', r'ciclo unico', r'’']
    df_all_features_first_degree = main_subject_replace_missing_value()
    # delete null value
    df_all_features_first_degree = df_all_features_first_degree[df_all_features_first_degree['degree_course'].notna()]
    df_all_features_first_degree['degree_course'] = data_cleaning(df_all_features_first_degree['degree_course'],
                                                                  regex_degree_course)
    # replace slang
    for key in slug_degree_course.keys():
        df_all_features_first_degree.loc[
            df_all_features_first_degree['degree_course'].str.contains(key), 'degree_course'] = slug_degree_course[key]

    # another cleaning
    df_all_features_first_degree.loc[
        df_all_features_first_degree['degree_course'].str.contains('medicina') & ~df_all_features_first_degree[
            'degree_course'].str.contains('veterinaria'), 'degree_course'] = 'medicina e chirurgia'
    df_all_features_first_degree.loc[
        df_all_features_first_degree['degree_course'].str.contains('informatica') & df_all_features_first_degree[
            'degree_course'].str.contains('elettronica') & df_all_features_first_degree['degree_course'].str.contains(
            'telecomunicazioni'), 'degree_course'] = 'ingegneria informatica elettronica e telecomunicazioni'
    df_all_features_first_degree.loc[df_all_features_first_degree['degree_course'].str.contains(
        'comunicazione e media per le industrie creative'), 'degree_course'] = 'comunicazione e media contemporanei per le industrie creative'
    df_all_features_first_degree.loc[
        df_all_features_first_degree['degree_course'].str.contains('elettronica') & ~df_all_features_first_degree[
            'degree_course'].str.contains('ingegneria') & ~df_all_features_first_degree['degree_course'].str.contains(
            'ing'), 'degree_course'] = 'ingegneria elettronica'
    df_all_features_first_degree.loc[df_all_features_first_degree['degree_course'].str.contains(
        'interfacce e tecnologie della comunicazion'), 'degree_course'] = 'interfacce uomo macchina e tecnologie della comunicazione'
    df_all_features_first_degree.loc[df_all_features_first_degree['degree_course'].str.contains(
        'letteratura musica e spettacolo'), 'degree_course'] = 'letteratura musica e spettacolo'
    df_all_features_first_degree['degree_course'] = df_all_features_first_degree['degree_course'].str.replace(
        r'(^ingegneria\s*)|(^ingegneria)', 'ing ')
    df_all_features_first_degree['degree_course'] = df_all_features_first_degree['degree_course'].str.replace(
        'ingeneria ', 'ing ')
    df_all_features_first_degree['degree_course']

    df_all_features_first_degree['degree_course'] = preprocessing_text(df_all_features_first_degree,
                                                                       df_all_features_first_degree['degree_course'],
                                                                       'degree_course', 'IT-EN')

    # DEBUG: print the unique degree_course after the cleaning
    unique_degree_course = np.unique(df_all_features_first_degree['degree_course'])
    print(len(unique_degree_course))
    print(unique_degree_course)
    return df_all_features_first_degree

def merge_school_whit_other_school_features():
    df_all_features_first_degree = clean_degree_course()
    #need to merge 2 columns
    df_all_features_first_degree['high_school']=df_all_features_first_degree['high_school'].replace('altro', np.NaN )

    #merge columns
    df_all_features_first_degree['high_school']=df_all_features_first_degree['high_school'].combine_first(df_all_features_first_degree['other_high_school'])

    df_all_features_first_degree['high_school']=df_all_features_first_degree['high_school'].replace(np.NaN,'altro')

    #delete support column
    df_all_features_first_degree=df_all_features_first_degree.drop(['other_high_school'], axis=1)
    print(df_all_features_first_degree.head())

    """  ### <h5>5.5.6) Controllo finale che non ci siano più valori nulli</h5>"""

    print(df_all_features_first_degree.isnull().sum())
    return df_all_features_first_degree

def cleaning_character_features():
    df_all_features_first_degree=merge_school_whit_other_school_features()
    df_clean_features = df_all_features_first_degree.copy()

    regex_features = [r'\s\s+']  # delete black space
    for feature in df_clean_features.columns:
        if feature != 'degree_course':
            df_clean_features[feature] = data_cleaning(df_clean_features[feature], regex_features)
            if feature not in categorical_features:
                df_clean_features[feature] = preprocessing_text(df_clean_features, df_clean_features[feature], feature,
                                                                'IT')

    # DEBUG: comparison between dirty data and clean data
    for feature in df_clean_features.columns:
        print(pd.merge(df_all_features_first_degree[feature], df_clean_features[feature], right_index=True,
                         left_index=True))
    #TODO: index_clean_features serve nella parte finale
    index_clean_features = df_clean_features.index  # need to the final
    return df_clean_features