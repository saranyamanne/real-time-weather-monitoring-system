# Real-Time Weather Monitoring System

This project implements a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system utilizes data from the OpenWeatherMap API.

## Features

- Continuous retrieval of weather data for major Indian metros
- Daily weather summaries with aggregates
- Configurable alerting thresholds
- Temperature conversion (Kelvin to Celsius)
- Visualizations for weather trends and alerts

## Installation

1. Clone the repository:git clone https://github.com/saranyamanne/real-time-weather-monitoring-system.git
2. cd real-time-weather-monitoring-system
3. Install dependencies:pip install -r requirements.txt
4. Set up environment variables:
Create a `.env` file in the root directory and add your OpenWeatherMap API key:
OPENWEATHERMAP_API_KEY=your_api_key_here

## Usage

1. Start the application: python main.py
2. Access the web interface at `http://localhost:8000`

## Configuration

Edit `config.py` to modify:
- Data retrieval interval
- Cities to monitor
- Alerting thresholds
- Temperature unit preference

## API Documentation

The system doesn't expose a public API, but internal functions
