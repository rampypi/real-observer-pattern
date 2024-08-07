# Requirement is you will receive weather data on every change of this data you have to update in the diaplys
# There will be three disply which wil consume this data and show it the respective screen
# Weather station will send you theupdated weather every time
# Wether dayas shuould be consumed whatever weatherstation send and send it to the display
# The display are observer which will get notified whenever new data comes
# The weather data is the subject which is responsible for publishing the messages

import unittest

from app.weather_data import Humidityescreen, WeatherData, Tempreaturescreen, Weatherscreen
from app.exceptions import EmptyObserverException

# Temperature; humididty; Weather
class TestWeatherData(unittest.TestCase):

    def test_data_in_weather_data(self):
        weatherdata = WeatherData(100, 9, 10)       
        self.assertEqual(weatherdata.tempreature, 100)
    
    def test_set_data_in_weather_data(self):
        weatherdata = WeatherData(100, 9, 10)       
        self.assertEqual(weatherdata.tempreature, 100)
        weatherdata.set_weather_data(1,2,3)
        self.assertEqual(weatherdata.humidity, 2)

    def test_register_observers(self):
         weatherdata = WeatherData(100, 9, 10)
         temp_screen = Tempreaturescreen
         weatherdata.register_observers(Tempreaturescreen)
         self.assertEqual(len(weatherdata.observers), 1)
    
    def test_unregister_observers(self):
         weatherdata = WeatherData(100, 9, 10)
         temp_screen = Tempreaturescreen
         weatherdata.register_observers(Tempreaturescreen)
         self.assertEqual(len(weatherdata.observers), 1)
         weatherdata.unregister_observers(Tempreaturescreen)
         self.assertEqual(len(weatherdata.observers), 0)

    def test_unregister_observers_from_empty_observer(self):
        weatherdata = WeatherData(100, 9, 10)
        temp_screen = Tempreaturescreen
        with self.assertRaises(EmptyObserverException) as context:
            weatherdata.unregister_observers(Tempreaturescreen)
        self.assertEqual(str(context.exception.message), "No Observers Found")

    
    def test_notify_observers(self):
        weatherdata = WeatherData(100, 9, 10)
        temp_screen = Tempreaturescreen()
        weatherdata.register_observers(temp_screen)
        weatherdata.set_weather_data(1,2,3)
        result = temp_screen.display()
        self.assertEqual(result, "This is the tempraeture: 1")

    def test_multiple_notify_observers(self):
        weatherdata = WeatherData(100, 9, 10)
        temp_screen = Tempreaturescreen()
        weather_screen = Weatherscreen()
        humidity_screen = Humidityescreen()
        weatherdata.register_observers(temp_screen)
        weatherdata.register_observers(weather_screen)
        weatherdata.register_observers(humidity_screen)
        weatherdata.set_weather_data(1,2,3)
        result = temp_screen.display()
        humidity_result = humidity_screen.display()
        weather_result = weather_screen.display()
        self.assertEqual(result, "This is the tempraeture: 1")
        self.assertEqual(humidity_result, "This is the humidity: 2")
        self.assertEqual(weather_result, "This is the weather: 3")