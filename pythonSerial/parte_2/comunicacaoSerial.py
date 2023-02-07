rotas = ['cer', 'ssa', 'vix']
print('Digite AWB!')
gaiola1 = input()
if gaiola1 not in rotas:
    print('Não liga Led ' + gaiola1)
else:
    print(gaiola1 + ' liga led 1.')