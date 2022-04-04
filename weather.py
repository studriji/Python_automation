import requests

# Create your views here.

# api key = 23098c7fb74cc117919923648ca47833
# url for api = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}




city = input('Enter the city : ')
#city = "kolkata"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=23098c7fb74cc117919923648ca47833'
data = requests.get(url).json()

data_dict = {
            'city' : data['name'],
            'weather' : data['weather'][0]['main'],
            'temp_K' : data['main']['temp'],
            'temp_C' : int(data['main']['temp'] - 273),
            'pressure' : data['main']['pressure']
                }
result = {'data' : data_dict}
#print(result)
#print(data_dict['city'])
for i in data_dict:
    print(f'{i} : {data_dict[i]}')
    