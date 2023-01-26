# Convert Fahrenheit to Celsius

inp = input('Enter the temperature in Fahrenheit: ')
try:
  Fahrenheit = float(inp)
  Celsius = (5.0/9.0)*(Fahrenheit-32.0)
  print('This is the temperature in Celsius: ')
  print(Celsius)
except:
  print('Please enter a number')
