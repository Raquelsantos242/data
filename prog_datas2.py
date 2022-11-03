from datetime import time

# 1.1 today(): recupera dia/mês/ano corrente
t1 = time(14, 53, 20, 1)
print('tempo: ', t1)
print('hora: ', t1.hour)
print('minuto: ', t1.minute)
print('segundo: ', t1.second)
print('microssegundo: ', t1.microsecond)