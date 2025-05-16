class TemperatureConverter:
    @staticmethod
    def celsium_to_fahrenheit(c):
        if c < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        return (c * 9/5) + 32
    
celsium_temp = 40
fahrenheit_temp = TemperatureConverter.celsium_to_fahrenheit(celsium_temp)
print(f"{celsium_temp}°C is equal to {fahrenheit_temp}°F")