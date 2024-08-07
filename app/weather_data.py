
from abc import ABC, abstractmethod
from app.exceptions import EmptyObserverException


class WeatherData:
    def __init__(self, tempreature, humidity, weather):
        self.tempreature = tempreature
        self.humidity = humidity
        self.weather = weather
        self.changed = True
        self.observers = []
    
    def set_weather_data(self, tempreature, humidity, weather):
        self.tempreature = tempreature
        self.humidity = humidity
        self.weather = weather
        self.notify_observers()

    
    def register_observers(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def unregister_observers(self, observer):
        if self.observers:
            self.observers.remove(observer)
        else:
            raise EmptyObserverException("No Observers Found")
    
    def notify_observers(self):
        if self.observers:
            for observer in self.observers:
                observer.set_data(self.tempreature, self.weather, self.humidity)

class Observer(ABC):  
    
    @abstractmethod
    def set_data(self):
        raise NotImplementedError
    
class Display(ABC):

    @abstractmethod
    def display(self):
        raise NotImplementedError

class Tempreaturescreen(Observer,Display):
    def __init__(self, tempreature=None, weather=None, humidity=None):
        self.tempreature = tempreature
        self.weather = weather
        self.humidity = humidity

    def set_data(self, tempreature, weather, humidity):
        self.tempreature = tempreature
        self.weather = weather
        self.humidity = humidity
        
    def display(self):
        return "This is the tempraeture: " +str(self.tempreature)
    
class Humidityescreen(Observer, Display):
    def __init__(self, tempreature=None, weather=None, humidity=None):
        self.tempreature = tempreature
        self.weather = weather
        self.humidity = humidity
    
    def set_data(self, tempreature, weather, humidity):
        self.tempreature = tempreature
        self.weather = weather
        self.humidity = humidity
       
    def display(self):
        return "This is the humidity: " +str(self.humidity)


class Weatherscreen(Observer, Display):
    def __init__(self, tempreature=None, weather=None, humidity=None):
        self.tempreature = tempreature
        self.weather = weather
        self.humidity = humidity
    
    def set_data(self, tempreature, weather, humidity):
        self.tempreature = tempreature
        self.weather = weather
        self.humidity = humidity

    def display(self):
        return "This is the weather: " +str(self.weather)
