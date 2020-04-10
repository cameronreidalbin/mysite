from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Parameter
#from .prediction import predict

def input(request):
    parameterList = Parameter.objects.all()
    context = {'parameterList': parameterList}
    return HttpResponse('input page')
#    return render(request, 'quotesTool/input.html', context)

def results(request):
    parameterList = Parameter.objects.all()
#    smc = Parameter.objects.get(name="SMC")
#    eau = Parameter.objects.get(name="EAU")
#    smc.quantity = int(request.GET['SMC'])
#    eau.quantity = int(request.GET['EAU'])
#    password = request.GET['pwd']
#    smc.save()
#    eau.save()
#    if password == 'alphaplan':
#        prediction = predict(smc.quantity,eau.quantity)
#        context = {'parameterList': parameterList, 'prediction':prediction}
#        return render(request, 'quotesTool/results.html', context)
#    return HttpResponse('wrong password')
    return HttpResponse('results page')