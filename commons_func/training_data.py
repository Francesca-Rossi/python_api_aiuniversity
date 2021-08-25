# TRAINING DATASET
def fit_dataset(model, X_train, y_train):
    model.fit(X_train, y_train)  # training the model on the train dataset
    return model

def predict_dataset(model, X_test):
    predictions = model.predict(X_test)  # predicting the output on the test dataset
    return predictions

def score_dataset(model, X_train, y_train, X_test, y_test):
    score_dict = {}
    score_dict['score_train_set'] = model.score(X_train, y_train)
    score_dict['score_test_set'] = model.score(X_test, y_test)
    score_dict['lengh_train_set'] = round(len(X_train))
    score_dict['lengh_test_set'] = round(len(X_test))
    return score_dict


def wrong_classification(X_test, predictions, y_test):
    wrong_class = 0
    for i in range(len(X_test)):
        elem = X_test[i]
        prediction = predictions[i]
        label = y_test[i]
        if prediction != label:  # output for debug
            wrong_class += 1
            print(i, 'has been classified as ', prediction, 'and should be ', label)
    print("-----------------------------------")
    return wrong_class