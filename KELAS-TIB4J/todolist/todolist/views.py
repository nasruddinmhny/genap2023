from django.http import HttpResponse 

def dashboard(request):
    return HttpResponse('<H1>Selamat Datang</H1>')
