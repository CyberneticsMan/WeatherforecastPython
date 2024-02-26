# import the module
import python_weather

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/forecast/<city>/temperature")
async def get_weather_temp(city):
    data = await get_weather_forecast_current(city)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/forecast/<city>/temperature/hourly")
async def get_weather_forecast(city):
    data = await get_weather_forecast_hourly(city)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  
@app.route("/forecast/<city>/ultraviolet")
async def get_weather_ultraviolet(city):
    data = await get_weather_forecast_ultraviolet(city)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


async def get_weather_forecast_current(city):
  async with python_weather.Client() as client:
  
    weather = await client.get(city)
    
    return weather.current.temperature


async def get_weather_forecast_hourly(city):
  async with python_weather.Client() as client:
    weather = await client.get(city)
    temps = []
        
    for forecast in weather.forecasts:
        temps.extend(hourly.temperature for hourly in forecast.hourly)
    return temps


async def get_weather_forecast_ultraviolet(city):
  async with python_weather.Client() as client:
    weather = await client.get(city)
    
    ultraviolet_list = []
    print(weather.current.ultraviolet)
    
    return weather.current.ultraviolet.value
  