
# Real-Time Weather Monitoring System

## Overview

This project is a real-time data processing system designed to monitor weather conditions using the OpenWeatherMap API. It retrieves weather data, processes it to generate daily summaries, triggers alerts based on predefined thresholds, and provides visualizations of temperature trends.

## Features

- **Real-Time Data Retrieval**: Fetch weather data from the OpenWeatherMap API at configurable intervals.
- **Data Processing**: Calculate daily weather summaries including average, maximum, and minimum temperatures, as well as the dominant weather condition.
- **Alerting System**: Trigger alerts if temperature exceeds specified thresholds.
- **Data Visualization**: Generate plots showing daily temperature trends.
- **Database Storage**: Store daily summaries in a SQLite database.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `matplotlib`, `sqlite3`
- An API key from OpenWeatherMap

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/siva-pro07/Real-Time-Weather-Monitoring-System.git
   cd weather-monitoring-system
   ```

2. **Install Dependencies**

   Ensure you have Python 3.x installed. Install the required libraries using pip:

   ```bash
   pip install requests matplotlib
   ```

3. **Set Up the Database**

   Initialize the SQLite database:

   ```python
   from database import init_db
   init_db()
   ```

4. **Configure API Key**

   Update the `API_KEY` variable in `main.py` with your OpenWeatherMap API key.

   ```python
   API_KEY = 'cbebc392610c2fb05e60e28609166f53'
   ```

### Usage

1. **Run the Main Script**

   Start the weather monitoring system by running:

   ```bash
   python main.py
   ```

   The script will continuously fetch weather data, process it, save daily summaries, check for alerts, and visualize data.

2. **View Alerts**

   Alerts will be printed to the console if temperature thresholds are exceeded.

3. **Check Visualizations**

   The generated plots will be saved as `temperature_trends.png` in the project directory.

### Files and Directories

- `main.py`: Main script to start the system.
- `weather.py`: Functions to fetch and process weather data.
- `database.py`: Functions to initialize the database and save daily summaries.
- `alert.py`: Functions to check for alerts based on weather data.
- `visualize.py`: Functions to visualize temperature trends.
- `weather.db`: SQLite database for storing daily weather summaries.
- `temperature_trends.png`: Output image of temperature trends.

### Example Data

Sample data output:

```json
{'2024-08-13': {'temperatures': [27.05], 'conditions': ['Mist']}}
{'2024-08-13': {'temperatures': [27.05, 25.99], 'conditions': ['Mist', 'Mist']}}
...
```

### Testing

1. **System Setup**

   Verify the system starts successfully and connects to the OpenWeatherMap API.

2. **Data Retrieval**

   Ensure the system retrieves and parses weather data correctly.

3. **Temperature Conversion**

   Test the conversion of temperature values from Kelvin to Celsius.

4. **Daily Weather Summary**

   Simulate weather updates and verify that daily summaries are accurate.

5. **Alerting Thresholds**

   Configure thresholds and verify that alerts are triggered correctly.
