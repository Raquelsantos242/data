import time

print('vou dormir por 3 segundos')
time.sleep(3)
print('acorde')

#3.1 ctime():conberte em timestamp para uma string
ts2 = 1572879180
print(time.ctime(ts2))

#3.2 gmtime(): converte um timestamp para um struct_time
#              (uma estrutura com as partes da data separadas)
st2 = time.gmtime(ts2)
print(st2)

#3.3 acttime(): cinverte struct_time pra string
str2 = time.asctime(st2)
print(str2)

#3.4 mktime(): cria um timestamp a partir de uma tela tuple
my_time_tuple = (2019, 11, 4, 11, 53, 0, 0, 0, 0)
print(time.mktime(my_time_tuple))