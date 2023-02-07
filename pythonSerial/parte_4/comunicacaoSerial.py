import serial

try:
    conectado = serial.Serial("COM3", 9600, timeout= 0.5)
    print("Conectado com a porta USB!", conectado.portstr)
except serial.SerialException:
    print("Porta USB não encontrada!")
    pass

while True:
    rota1 = ["cer", "ssa", "vix"]
    rota2 = ["rio", "sao"]
    rota3 = ["tzx", "tzo"]

    print('Digite AWB!') 
    gaiola = input()
    
    
    if gaiola not in rota1:
        ##conectado.write(b'0')
        print('Não liga led' + gaiola)
    else:
        ##conectado.write(b'1')
        print(gaiola + ' liga led 1.')
    if gaiola not in rota2:
        ##conectado.write(b'0')
        print('Não liga led' + gaiola)
    else:
        ##conectado.write(b'2')
        print(gaiola + ' liga led 2.')
    if gaiola not in rota3:
        ##conectado.write(b'0')
        print('Não liga led' + gaiola)
    else:
        ##conectado.write(b'3')
        print(gaiola + ' liga led 3.')            
                
conectado.close()
print("Conecção fechado")
pass