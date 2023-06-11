from django.shortcuts import render
from . import fake_model
from . import ml_predict


def home(request):
	return render(request, 'index.html')

def result(request):
	person_age = "0"
	if request.method == 'POST':
		pclass = request.POST['pclass']
		sex = request.POST['sex']
		age = request.POST['age']
		sibsp = request.POST['sibsp']
		parch = request.POST['parch']
		fare = request.POST['fare']
		embarked = request.POST['embarked']
		title = request.POST['title']
		
		#prediction = fake_model.fake_predict(int(person_age))
		prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)


	return render(request, 'result.html', { 'prediction': prediction})
