from django.http import HttpResponse


def input(request):
    return HttpResponse("This is the input page")

def results(request):
    return HttpResponse("This is the results page")
