import time
from weather import fetch_weather_data, process_weather_data
from database import init_db, save_daily_summary
from alert import check_alerts
from visualize import visualize_data

API_KEY = '866877ea295010fd832e45f991746ac6'
LOCATIONS = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # 5 minutes

def main():
    init_db()

    while True:
        for location in LOCATIONS:
            weather_data = fetch_weather_data(API_KEY, location)
            daily_summary = process_weather_data(weather_data)
            save_daily_summary(location, daily_summary)
            check_alerts(weather_data)
        
        visualize_data()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
