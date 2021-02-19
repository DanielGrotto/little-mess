#Conversão de temperaturas

temp_c = float(input('Digite a temperatura em graus Celcius: '))

temp_f = 1.8*temp_c + 32 #Converte Celsius em Fahrenheit
temp_k = temp_c + 273.15 #Converte Celsius em Kelvin

#Conversão final
print('Temperatura em Celsius: ' + str(temp_c))
print('Temperatura em Fahrenheit: ' + str(temp_f))
print('Temperatura em Kelvin: ' + str(temp_k))
