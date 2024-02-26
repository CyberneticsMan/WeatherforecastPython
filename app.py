# import the module
import python_weather

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/forecast/<city>/temperature")
async def get_weather_temp(city):
    data = await get_weather_forecast_current(city)
    return jsonify(data)

@app.route("/forecast/<city>/temperature/hourly")
async def get_weather_forecast(city):
    data = await get_weather_forecast_hourly(city)
    return jsonify(data)
  
@app.route("/forecast/<city>/ultraviolet")
async def get_weather_ultraviolet(city):
    data = await get_weather_forecast_ultraviolet(city)
    return jsonify(data)


async def get_weather_forecast_current(city):
  
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client() as client:
    # fetch a weather forecast from a city
    weather = await client.get(city)
    
    # returns the current day's forecast temperature (int)
    return weather.current.temperature


async def get_weather_forecast_hourly(city):
  
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client() as client:
    # fetch a weather forecast from a city
    weather = await client.get(city)
    temps = []
    # returns the current day's forecast temperature (int)
    for forecast in weather.forecasts:
        for hourly in forecast.hourly:
          temps.append(hourly.temperature)
    return temps


async def get_weather_forecast_ultraviolet(city):
  async with python_weather.Client() as client:
    # fetch a weather forecast from a city
    weather = await client.get(city)
    
    ultraviolet_list = []
    print(weather.current.ultraviolet)
    
    return weather.current.ultraviolet.value
    
    
    # return weather.current.ultraviolet