from django.http import HttpResponse

def index(request):
    return HttpResponse("<p><img src='/static/image1.jpg'>Text</p>")
