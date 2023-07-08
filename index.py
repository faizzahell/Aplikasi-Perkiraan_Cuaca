from function import function
import os

looping = True

while looping == True:
  os.system('cls' if os.name == 'nt' else 'clear')
  print('======================================')
  print('------ Aplikasi Perkiraan Cuaca ------')
  print('======================================\n')

  city = input(" Masukkan nama kota : ")

  print('\n======================================\n')

  value = function.getWeather(city)

  print(' Kota            : ', city.capitalize())
  print(' Suhu            : ', value[0])
  print(' Cuaca           : ', value[1])
  print(' Kelembaban      : ', value[2])
  print(' Kecepatan Angin : ', value[3])

  print('\n======================================\n')

  loopingCondition = True
  while loopingCondition == True:
    backMenu = input(" Kembali ke menu (Y/n) : ")
    
    if (backMenu == 'Y') | (backMenu == 'y'):
      looping = True
      loopingCondition = False
    elif (backMenu == 'N') | (backMenu == 'n'):
      looping = False
      loopingCondition = False
    else:
      print('\n======================================\n')
      print(' Input salah, Masukkan kembali !!')
      print('\n======================================\n')
    
print('\n======================================')
print('---------- Aplikasi Selesai ----------')
print('======================================')

