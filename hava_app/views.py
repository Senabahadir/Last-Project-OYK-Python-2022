from django.shortcuts import render
from .models import Hava
from .forms import ListForm

# import requests
# import json

def index(request):

    if request.method == "POST":                       #Adminden kaydedilen veriler
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            hava_list = Hava.objects.all()
            print(hava_list)
            return render(request,"index.html",{'hava_list':hava_list})
    else:
        hava_list = Hava.objects.all()
        print(hava_list)
        return render(request,"index.html",{'hava_list':hava_list})


    #---------------- json olarak çektiğimiz veri  -----------------
    # res = requests.get(url='http://192.168.2.193:8000/collector/read/29bc4e8b-2789-4689-918d-99158c6b9ff2/')
    # data = json.loads(json.loads(res.text))
    # print(data)

    # for veriler in data:
    #     json.loads(veriler['data'])
    # veriler = [json.loads(veriler['data']) for veri in data ]
    # print(veriler)
    # return render(request,"index.html",{'veriler':veriler})
    #     print(temp)
    

def about(request):
    return render(request,"about.html")