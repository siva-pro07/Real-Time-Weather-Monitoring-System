import matplotlib.pyplot as plt
import sqlite3

def visualize_data():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT date, AVG(avg_temp) as avg_temp, MAX(max_temp) as max_temp, MIN(min_temp) as min_temp
        FROM daily_summary
        GROUP BY date
    ''')
    data = c.fetchall()
    conn.close()

    if not data:
        print("No data found in the database.")
        return

    dates, avg_temps, max_temps, min_temps = zip(*data)

    plt.figure(figsize=(10, 6))
    plt.plot(dates, avg_temps, label='Average Temperature', marker='o')
    plt.plot(dates, max_temps, label='Maximum Temperature', marker='o')
    plt.plot(dates, min_temps, label='Minimum Temperature', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Temperature Trends')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('temperature_trends.png')
    plt.show()
