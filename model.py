from feature_engineering import *
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from commons_func.training_data import *
import joblib
import multiprocessing as mp

model_1 = MultinomialNB()
model_2 = DecisionTreeClassifier()
model_3 = SVC()
estimators_list = [('NB', model_1), ('DT', model_2), ('SVM', model_3)]

def create_model():
    df_clean_features = tf_id_text_features()
    X = df_clean_features.iloc[:, 1:]
    y = df_clean_features['degree_course']
    """##<h5><b>7.1) Bilanciamento delle classi</b></h5>
    <p> Poichè le nostre classi (i corsi di laurea) non sono rappresentate in modo approssimativamente uguale, è stato necessario bilanciare le classi. In questa fase l'obiettivo principale è stato perdere meno dati possibili, il che ha portato a escludere un <code>algoritmo di undersampling</code>, cui risultato sarebbe stata la riduzione del numero dei campioni nelle classi più numerose.  Abbiamo invece optato per un' <code>algoritmo di oversampling</code>, cui scopo è di aumentare il numero dei campioni delle classi meno numerose.</p>
    <p> In particolare abbiamo usato l'algoritmo<code> RandomOverSampler</code> della libreria <i>imblearn</i></p>
    """
    print('number of sample before:', Counter(y))  # DEBUG: see the number of sample before oversampling
    oversample = RandomOverSampler(sampling_strategy='auto')
    X1, y1 = oversample.fit_resample(X.values, y)
    print('number of sample after:', Counter(y1))  # DEBUG: see the number of sample after oversampling

    """###<h5><b>7.2) Suddivisione nel set di test e di addestramento</b></h5>
    <p>In questa fase abbiamo testato gli algoritmi con 4 test set e train set differenti,con lo scopo di verificare in quale caso la predizione fosse migliore e più accurata</p>
    """

    X_train_20, X_test_20, y_train_20, y_test_20 = train_test_split(X1, y1, test_size=0.20, random_state=42)
    X_train_33, X_test_33, y_train_33, y_test_33 = train_test_split(X1, y1, test_size=0.33, random_state=42)
    X_train_50, X_test_50, y_train_50, y_test_50 = train_test_split(X1, y1, test_size=0.50, random_state=42)
    X_train_66, X_test_66, y_train_66, y_test_66 = train_test_split(X1, y1, test_size=0.66, random_state=42)
    X_train_list = [X_train_20, X_train_33, X_train_50, X_train_66]
    y_train_list = [y_train_20, y_train_33, y_train_50, y_train_66]
    X_test_list = [X_test_20, X_test_33, X_test_50, X_test_66]
    y_test_list = [y_test_20, y_test_33, y_test_50, y_test_66]
    keys_list = ['test_20%', 'test_33%', 'test_50%', 'test_66%']
    return X_train_list,y_train_list, X_test_list, y_test_list, keys_list

def voting_alghoritm(X_train_list, y_train_list, X_test_list, y_test_list, keys_list):
    voting_predict = {}
    voting_score = {}
    voting_report = {}
    for i in range(0, 4):
        voting_model = VotingClassifier(estimators=estimators_list, voting='hard')
        voting_model = fit_dataset(voting_model, X_train_list[i], y_train_list[i])
        voting_predict[keys_list[i]] = predict_dataset(voting_model, X_test_list[i])
        voting_score[keys_list[i]] = score_dataset(voting_model, X_train_list[i], y_train_list[i], X_test_list[i],y_test_list[i])
        #voting_score[keys_list[i]]['wrong_class'] = wrong_classification(X_test_list[i], voting_predict[keys_list[i]],y_test_list[i])
        voting_report[keys_list[i]] = classification_report(y_test_list[i], voting_predict[keys_list[i]],output_dict=True)
        voting_score[keys_list[i]]['accuracy'] = voting_report[keys_list[i]]['accuracy']
    return voting_score, voting_model , voting_predict, voting_report


def bagging_algorithm(X_train_list, y_train_list, X_test_list, y_test_list, keys_list):
    bagging_predict = {}
    bagging_score = {}
    bagging_report = {}
    for i in range(0, 4):
        bagging_model = BaggingClassifier(base_estimator=None, n_estimators=10, random_state=0)
        bagging_model= fit_dataset(bagging_model, X_train_list[i], y_train_list[i])
        bagging_predict[keys_list[i]] = predict_dataset(bagging_model, X_test_list[i])
        bagging_score[keys_list[i]] = score_dataset(bagging_model, X_train_list[i], y_train_list[i], X_test_list[i],y_test_list[i])
        #bagging_score[keys_list[i]]['wrong_class'] = wrong_classification(X_test_list[i], bagging_predict[keys_list[i]],y_test_list[i])
        bagging_report[keys_list[i]] = classification_report(y_test_list[i], bagging_predict[keys_list[i]],output_dict=True)
        bagging_score[keys_list[i]]['accuracy'] = bagging_report[keys_list[i]]['accuracy']
    return  bagging_score, bagging_model, bagging_predict, bagging_report


def boosting_alghoritm(X_train_list, y_train_list, X_test_list, y_test_list, keys_list):
    boosting_predict = {}
    boosting_score = {}
    boosting_report = {}
    for i in range(0, 4):
        boosting_model = GradientBoostingClassifier(n_estimators=10, learning_rate=1.0, max_depth=1, random_state=0)
        boosting_model = fit_dataset(boosting_model, X_train_list[i], y_train_list[i])
        boosting_predict[keys_list[i]] = predict_dataset(boosting_model, X_test_list[i])
        boosting_score[keys_list[i]] = score_dataset(boosting_model, X_train_list[i], y_train_list[i], X_test_list[i],y_test_list[i])
        #boosting_score[keys_list[i]]['wrong_class'] = wrong_classification(X_test_list[i],boosting_predict[keys_list[i]], y_test_list[i])
        boosting_report[keys_list[i]] = classification_report(y_test_list[i], boosting_predict[keys_list[i]], output_dict=True)
        boosting_score[keys_list[i]]['accuracy'] = boosting_report[keys_list[i]]['accuracy']
    return boosting_score, boosting_model, boosting_predict, boosting_report


def stacking_alghortim(X_train_list, y_train_list, X_test_list, y_test_list, keys_list):
    stacking_predict = {}
    stacking_score = {}
    stacking_report = {}
    for i in range(0, 4):
        stacking_model = StackingClassifier(estimators=estimators_list, final_estimator=LogisticRegression())
        stacking_model =fit_dataset(stacking_model, X_train_list[i], y_train_list[i])
        stacking_predict[keys_list[i]] = predict_dataset(stacking_model, X_test_list[i])
        stacking_score[keys_list[i]] = score_dataset(stacking_model, X_train_list[i], y_train_list[i], X_test_list[i], y_test_list[i])
        #stacking_score[keys_list[i]]['wrong_class'] = wrong_classification(X_test_list[i],stacking_predict[keys_list[i]],y_test_list[i])
        stacking_report[keys_list[i]] = classification_report(y_test_list[i], stacking_predict[keys_list[i]],output_dict=True)
        stacking_score[keys_list[i]]['accuracy'] = stacking_report[keys_list[i]]['accuracy']
    return stacking_score, stacking_model, stacking_predict, stacking_report



def generate_model():
    X_train_list, y_train_list, X_test_list, y_test_list, keys_list = create_model()
    voting_score, voting_model , voting_predict, voting_report = voting_alghoritm(X_train_list, y_train_list, X_test_list, y_test_list, keys_list)
    bagging_score, bagging_model, bagging_predict, bagging_report = bagging_algorithm(X_train_list, y_train_list, X_test_list, y_test_list, keys_list)
    boosting_score, boosting_model, boosting_predict, boosting_report = boosting_alghoritm(X_train_list, y_train_list, X_test_list, y_test_list, keys_list)
    stacking_score, stacking_model, stacking_predict, stacking_report = stacking_alghortim(X_train_list, y_train_list, X_test_list, y_test_list, keys_list)
    voting_score_df = pd.DataFrame(voting_score)
    bagging_score_df = pd.DataFrame(bagging_score)
    boosting_score_df = pd.DataFrame(boosting_score)
    stacking_score_df = pd.DataFrame(stacking_score)
    list_score = [voting_score_df, bagging_score_df, boosting_score_df, stacking_score_df]
    name_list = ['voting', 'bagging', 'boosting', 'stacking']
    voting_list = [voting_score, voting_model, voting_predict, voting_report]
    bagging_list = [bagging_score, bagging_model, bagging_predict, bagging_report]
    boosting_list = [boosting_score, boosting_model, boosting_predict, boosting_report]
    stacking_list = [stacking_score, stacking_model, stacking_predict, stacking_report]
    return  list_score, name_list, voting_list, bagging_list, boosting_list, stacking_list

def best_model():
    list_score, name_list, voting_list, bagging_list, boosting_list, stacking_list= generate_model()
    keys_list = ['test_20%', 'test_33%', 'test_50%', 'test_66%']
    accurancy_df = pd.DataFrame()
    for i in range(0, 4):
        df = list_score[i].transpose()
        label = name_list[i]
        accurancy_df.insert(0, label, df['accuracy'])
    print(accurancy_df) #DEBUG
    df2 = accurancy_df.transpose()
    dict2 = {}
    l = []
    for key in keys_list:
        dict2[key] = df2[df2[key] == df2[key].max()][
            key].to_dict()  # dictionary containing for each test set the algorithm with the highest accuracy
        l.append(list(dict2[key].values()))  # support list
    # find the test set with the best accuracy
    max_model = max(l)
    for test, sub_dict in dict2.items():
        if (list(sub_dict.values()) == max_model):  # get the best algorithm and test set back
            for model, value in sub_dict.items():
                model_name = model
                test_name = test
    print('Il miglior modello è', model_name, ', utilizzando un', test_name)
    return model_name, test_name, voting_list, bagging_list, boosting_list, stacking_list


def save_best_model():
    error = 0
    model_name, test_name, voting_list, bagging_list, boosting_list, stacking_list = best_model()
    if model_name == 'voting':
        clf = voting_list[1] #modello
        report = voting_list[3][test_name] #report
        predictions = voting_list[2][test_name] #prediction
        print('voting')  # debug output
    elif model_name == 'bagging':
        clf = bagging_list[1]
        report = bagging_list[3][test_name]
        predictions = bagging_list[2][test_name]
        print('bagging')
    elif model_name == 'boosting':
        clf = boosting_list[1]
        report = boosting_list[3][test_name]
        predictions = boosting_list[2][test_name]
        print('boosting')
    elif model_name == 'stacking':
        clf = stacking_list[1]
        report = stacking_list[3][test_name]
        predictions = stacking_list[2][test_name]
        print('stacking')
    else:
        print('Errore nella scelta del modello')
        error = 1
    filename = 'doc/model'
    joblib.dump(clf, filename)
