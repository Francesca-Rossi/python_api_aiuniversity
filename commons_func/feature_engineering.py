import pandas as pd
import numpy as np
import joblib


# FEATURE ENGINEERING TEXT
def tf_vector(vectorize, feature):
    tf_matrix = vectorize.fit_transform(feature)
    joblib.dump(vectorize, 'doc/tf_id_model.joblib')
    tf_matrix = tf_matrix.toarray()
    vocab = vectorize.get_feature_names()
    return pd.DataFrame(np.round(tf_matrix, 2), columns=vocab)


def bag_of_words(vectorize, feature):
    vectorize.fit(feature)
    joblib.dump(vectorize, 'doc/bag_of_word_model.joblib')
    bag_array = vectorize.transform(feature).toarray()
    vocab = vectorize.get_feature_names()
    return pd.DataFrame(bag_array, columns=vocab)


# FEATURE ENGINEERING CATEGORICAL DATA

def one_hot_encoding(feature, key, genre_labels, encoder):
    genre_mappings = {index: label for index, label in enumerate(encoder.classes_)}
    feature = genre_labels
    print('encoding', key, ':', genre_mappings)
    return feature
