assignment
def sunny(temp):
    if temp >=80:
        print('Go to the beach when the temperature is '+ str(temp))
    else:
        print('stay home when the temperature is '+ str(temp))

def rainy(hum,temp):
    if hum >= 90:
        temp = temp + 5
        print('The real feel is ' + str(temp) + 'degrees,when its raining')
    else:
        print('The real feel is ' + str(temp) + 'degrees,when its raining')


filepath = 'data.csv'
with open(filepath) as fp:
    line = 'X'
    while line != '':
        line = fp.readline()
        if line != '':
            temp = int(line[2] + line[3])
            hum = int(line[5] + line[6])
            if line != '' and line[0] == 'S':
                sunny(temp)
            elif line != '' and line[0] == 'r':
                rainy(hum,temp)
            else:
     print('This code was written by your assignment')
fp.close()     
            

    
