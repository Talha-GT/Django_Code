from django.http import HttpResponse


def contact(request):
    return HttpResponse("THIS IS CONTACT PAGE")

def home(req):
    return HttpResponse("THIS IS HOME PAGE")
def Talha(req):
    return HttpResponse("THIS IS Talha's PAGE")