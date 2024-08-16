import requests
from datetime import datetime
from statistics import mean

# Dictionary to hold daily weather data
daily_data = {}

def fetch_weather_data(api_key, location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_weather_data(data):
    temp = data['main']['temp']
    condition = data['weather'][0]['main']
    timestamp = data['dt']
    
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    if date not in daily_data:
        daily_data[date] = {
            'temperatures': [],
            'conditions': []
        }
    
    daily_data[date]['temperatures'].append(temp)
    daily_data[date]['conditions'].append(condition)
    
    avg_temp = mean(daily_data[date]['temperatures'])
    max_temp = max(daily_data[date]['temperatures'])
    min_temp = min(daily_data[date]['temperatures'])
    dominant_condition = max(set(daily_data[date]['conditions']), key=daily_data[date]['conditions'].count)


    print(daily_data)    

    return {
        'date': date,
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }
def calculate_daily_summary(daily_data):
    temperatures = daily_data['temperatures']
    conditions = daily_data['conditions']
    
    avg_temp = mean(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    dominant_condition = Counter(conditions).most_common(1)[0][0]
    
    return {
        'date': date,
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }
