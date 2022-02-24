# Contagem regressiva
# Contar de 10 até 0 com um intervalo de 1s entre as contagens
from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BOOOM!!!')
