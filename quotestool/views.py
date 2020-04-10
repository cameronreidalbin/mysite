from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Parameter
from .prediction import predict

Parameter.objects.all().delete()
smc = Parameter(name="SMC")
eau = Parameter(name="EAU")
smc.save()
eau.save()

def input(request):
    parameterList = Parameter.objects.all()
    context = {'parameterList': parameterList}
    return render(request, 'quotestool/input.html', context)

def results(request):
    parameterList = Parameter.objects.all()
    smc = Parameter.objects.get(name="SMC")
    eau = Parameter.objects.get(name="EAU")
    smc.quantity = int(request.GET['SMC'])
    eau.quantity = int(request.GET['EAU'])
    password = request.GET['pwd']
    smc.save()
    eau.save()
    if password == 'alphaplan':
        prediction = predict(smc.quantity,eau.quantity)
        context = {'parameterList': parameterList, 'prediction':prediction}
        return render(request, 'quotestool/results.html', context)
    return HttpResponse('wrong password')