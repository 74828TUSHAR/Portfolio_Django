from django.shortcuts import render

# Create your views here.
def services(request):
    context = {'project': 'active'}
    return render(request,'serv/services.html',context)
