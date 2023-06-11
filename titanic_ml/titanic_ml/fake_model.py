def fake_predict(person_age):
    if person_age > 10:
        prediction = "survived"
    else:
        prediction = "super survived"

    return prediction
