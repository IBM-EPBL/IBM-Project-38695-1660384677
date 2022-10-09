import random
Temp_Value = random.randint(18,40)
Hum_Value = random.randint(20,90)

print("Humidity =",Hum_Value,"%")

if  Temp_Value > 35:
   print("Temperature =",Temp_Value,"C")
   print("----------Warning----------")
   print(" !! High Temperature !! ")
   
else:
  print("Temperature =",Temp_Value,"C")

