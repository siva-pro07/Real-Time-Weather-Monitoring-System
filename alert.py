import smtplib
from email.mime.text import MIMEText

THRESHOLD_TEMP = 35

def check_alerts(weather_data):
    temp = weather_data['main']['temp']
    if temp > THRESHOLD_TEMP:
        send_alert(weather_data)

def send_alert(weather_data):
    msg = MIMEText(f"Alert! Current weather conditions:\n\nTemperature: {weather_data['main']['temp']}°C\nCondition: {weather_data['weather'][0]['main']}")
    msg['Subject'] = 'Weather Alert'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient@example.com'
    
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
