import string
from nltk.corpus import stopwords
from nltk.stem.snowball import ItalianStemmer

# CLEANING DATA
def lang_stop_words(feature, lang):
    stop_ita = stopwords.words('italian')
    stop_en = stopwords.words('english')
    if (lang == "IT"):
        feature = feature.apply(lambda x: [item for item in x if item not in stop_ita])
    elif (lang == "EN"):
        feature = feature.apply(lambda x: [item for item in x if item not in stop_en])
    else:
        feature = feature.apply(lambda x: [item for item in x if item not in stop_ita])
        feature = feature.apply(lambda x: [item for item in x if item not in stop_en])
    return feature


def data_cleaning(feature, regex_list):
    feature = feature.apply(lambda x: x.lower())  # lowercase
    feature = feature.str.strip()  # elimination of white spaces at the beginning and at the end
    for regex in regex_list:
        feature = feature.str.replace(regex, ' ')
    for char in string.punctuation:
        feature = feature.str.replace(char, ' ')
    return feature