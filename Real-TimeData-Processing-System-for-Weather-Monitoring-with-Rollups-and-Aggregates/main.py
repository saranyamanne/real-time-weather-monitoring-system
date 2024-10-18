from weather_data_processor import WeatherDataProcessor
from alert_manager import AlertManager
from db_manager import DBManager
from config import TEMP_THRESHOLD

if __name__ == "__main__":
    processor = WeatherDataProcessor()
    db_manager = DBManager('weather.db')
    alert_manager = AlertManager(TEMP_THRESHOLD)

    while True:
        # Get latest weather data
        weather_data = processor.process_data()

        # Store daily summaries
        # db_manager.insert_summary(...)

        # Check for alert conditions
        alert_manager.check_for_alert(weather_data)
