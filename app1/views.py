
from django.shortcuts import render
import requests
import json


def index(request):
    if request.method=='POST':
        city=request.POST.get('inpt')
        
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=b05ee3965f06b8f069c4b8c740a7fe69'
        res=requests.get(url=url)
        data=res.text
        r=json.loads(data)
        d={
            'temp':r['main']['temp'],
            'tempmin':r['main']['temp_min'],
            'tempmax':r['main']['temp_max'],
            'dec':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            'sys':r['sys']['country'],
            

        }
        print(d)
    return render(request,'index.html')

# 'temp':r['main']['temp'],
#             'temp-min':r['main']['temp_min'],
#             'temp-max':r['main']['temp_max'],
#             'dec':r['weather'][0]['description'],
#             'icon':r['weather'][0]['icon'],
#             'sys':r['sys']['country'],