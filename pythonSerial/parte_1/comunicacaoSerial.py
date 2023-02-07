import serial


try:
    conectado = serial.Serial("COM3", 9600, timeout= 0.5)
    print("Conectado com a porta USB!", conectado.portstr)
except serial.SerialException:
    print("Porta USB não encontrada!")
    pass


while True:
    comando = input("Digite L para ligar e D para desligar:")
    if comando == "l":
        conectado.write(b'1')
    else:
        conectado.write(b'0')
        
    if input("Deseja continuar?").upper()=="n":    
        break    
conectado.close()
print("Conecção fechado")
pass