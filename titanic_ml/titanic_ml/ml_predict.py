# Correct order in the dataframe
import os

def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    print ("test=", os.getcwd())
    randomforest = pickle.load(open("titanic_ml/titanic_model.sav", "rb"))
    prediction = randomforest.predict(x)

    if prediction == 0:
        resultat = 'Not survived'
    elif prediction == 1:
        resultat = 'Survived'
    else:
        resultat = 'Error'

    return resultat
