import serial

try:
    conectado = serial.Serial("COM3", 9600, timeout= 0.5)
    print("Conectado com a porta USB!", conectado.portstr)
except serial.SerialException:
    print("Porta USB não encontrada!")
    pass

while True:
    rotas = ['cer', 'ssa', 'vix']
    print('Digite AWB!')
    
    gaiola1 = input()
    
    if gaiola1 not in rotas:
        conectado.write(b'0')
        print('Não liga Led ' + gaiola1)
    else:
        conectado.write(b'1')
        print(gaiola1 + ' liga led 1.')
    
    
conectado.close()
print("Conecção fechado")
pass