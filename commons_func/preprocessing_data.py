from nltk.stem.snowball import ItalianStemmer
from ai_model.cleaning_data import lang_stop_words
import nltk

def preprocessing_text(dataframe, feature, key, lang):
    stemmer = ItalianStemmer()
    feature = feature.str.strip()  # elimination of white spaces at the beginning and at the end
    feature = dataframe.apply(lambda row: nltk.word_tokenize(row[key]), axis=1)
    feature = lang_stop_words(feature, lang)
    feature = feature.apply(lambda x: [stemmer.stem(y) for y in x])  # stem every word
    feature = feature.apply(' '.join)
    return feature