from django.shortcuts import render
import json
import urllib.request 
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+'&appid=d0c0437f4614691d39736868103edb0e').read()
        json_data = json.loads(res)
        temp = float(json_data['main']['temp'])
        cent = int(temp - 273.15)
        data = {'city':city,
                'country_code':str(json_data['sys']['country']),
                'coordinate': str(json_data['coord']['lon'])+' long'+ " - " +str( json_data['coord']['lat'])+' lat',
                'temp': str(cent)+u"\u2103",
                'pressure': str(json_data['main']['pressure']) + " bar",
                'humidity': str(json_data['main']['humidity'])+ " mi"
        }
        
    else:
        city =''
        data = { }
    return render(request,'index.html', data,)