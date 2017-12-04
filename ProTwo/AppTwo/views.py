from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_data = {"data": "This is data from the index view"}
    return render(request, "apptwo/index.html", context=my_data)

def help(request):
    my_data = {'data': "This is the help page data!!!!"}
    return render(request, "apptwo/help.html", context=my_data)
