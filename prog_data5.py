# ----------------------------------------------------
# 5- funções de formatação
# ----------------------------------------------------
from datetime import date, time, datetime
print('-----------------------------------------------')

# 5.1 strftime(): formata uma data ou datetime 
# %d, %m, %Y, etc. são diretivas de formatação. Consulte em: https://strftime.org/

d3 = date(2020, 1, 4)
print(d3)
print(d3.strftime('%d/%m/%Y'))

t3 = time(14, 53)
print(t3)
print(t3.strftime('%H horas e %M minutos'))

dt3 = datetime(2020, 1, 4, 14, 53)
print(dt3)
print(dt3.strftime('%d/%m/%Y às %H horas e %M minutos'))

import time
print('-----------------------------------------------')

ts4 = 1572879180
st4 = time.gmtime(ts4)
print(ts4)
print(st4)
print(time.strftime('%d/%m/%Y às %H horas e %M minutos', st4))

# 5.2 strptime(): recebe uma data em uma string e usa as diretivas
#                 para converter da string para datetime/date/time
dt5 = datetime.strptime("04/11/2019 14:53:00", "%d/%m/%Y %H:%M:%S")
print(dt5, type(dt5))