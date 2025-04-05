from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime

def index(request):
    
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='barisal'
    
    appid='d04743c24458adb8233616c7762290c5'
    URL='https://api.openweathermap.org/data/2.5/weather'
    PARAMS={'q':'city','appid':appid,'units':'metric','city':city}
    
    r=requests.get(url=URL,params=PARAMS)
    res=r.json()
    
    description=res['weather'][0]['description']
    icon=res['weather'][0]['icon']
    temp=res['main']['temp']
    day=datetime.date.today()
    
    return render(request, 'weather/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})