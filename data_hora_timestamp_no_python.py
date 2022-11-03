"""
Introdução ao módulo datetime
- oferece classes para você trabalhar com datas e horas
- aplicações práticas:
  1- log de eventos -> para sabermos quando exatamente um erro crítico ocorreu
                      na rede, no S.O., no SGBD, etc.
  2- acompanhar modificações em um banco de dados -> em BDs é necessário
                      saber quando um registro foi inserido/modificado/apagado
  3- validação de dados -> ex.: o seu sistema dá um desconto para a compra de
                           um produto, mas o cupom tem validade
  4- armazenamento de informação crítica -> ex.: em um sistema de uma instituição
                           finaneceiras é necessário saber o momento exato em que
                           um dinheiro foi aplicado ou sacado
"""

# ----------------------------------------------------
# 1- classe date
#    objetos dessa classe consistem em ano, mês e dia
# ----------------------------------------------------
from datetime import date

# 1.1 today(): recupera dia/mês/ano corrente
hoje = date.today()   

print("Hoje:", hoje)
print("Dia:", hoje.day, " - Mês:", hoje.month, " - Ano:", hoje.year)

# 1.2 criando a sua própria data
d1 = date(1970, 6, 21)  # usamos o construtor date()
print(d1)

# 1.3 criando uma data a partir de um timestamp
#  O que é timestamp: número de segundos que passou desde 1/1/1970
#                     essa data e chamada de Unix epoch
import time

ts = time.time()   # retornar o timestamp referente a data/hora corrente
print('hoje no formato timestamp:', ts)

ts_data = date.fromtimestamp(ts)
print('hoje no formato data (só a parte a/m/d):', ts_data)

# 1.4 criando uma data no formato ISO: YYYY-MM-DD
d2 = date.fromisoformat('1982-07-05')
print(d2)

# 1.5 o método replace(): usado para alterar uma data
d2 = d2.replace(year=1992, month=9, day=15)
print(d2)

# 1.6 weekday: retorna número dizendo qual é o dia da semana
#              0-segunda, 1-terça, ... 4-sexta, 5-sábado, 6-domingo  
print(hoje.weekday())

# 1.7 isoweekday: 1-segunda, ..., 7-Domingo
print(hoje.isoweekday())

# ----------------------------------------------------
# 2- módulo time (do pacote datetime)
#    - criar objetos do tipo (hora, minuto, segundo, microssegundo, tzinfo, fold)
# ----------------------------------------------------
print('-----------------------------------------------')

from datetime import time

# 1.1 today(): recupera dia/mês/ano corrente
t1 = time(14, 53, 20, 1)
print('tempo: ', t1)
print('hora: ', t1.hour)
print('minuto: ', t1.minute)
print('segundo: ', t1.second)
print('microssegundo: ', t1.microsecond)

# ----------------------------------------------------
# 3- módulo time (que não é do pacote datetime)
#    - fornece várias funções relacionadas a tempo
# ----------------------------------------------------
print('-----------------------------------------------')

import time

#print('Vou dormir por 3 segundos...')
#time.sleep(3)
#print('ACORDEI!!!')

# 3.1 ctime(): converte um timestamp para uma string
ts2 = 1572879180
print(time.ctime(ts2))

# 3.2 gmtime(): converte um timestamp para um struct_time
#              (uma estrutura com as partes da data separadas) 
st2 = time.gmtime(ts2)
print(st2)

# 3.3 asctime(): converte struct_time para string
str2 = time.asctime(st2)
print(str2)

# 3.4 mktime(): cria um timestamp a partir de uma time_tuple
my_time_tuple = (2019, 11, 4, 11, 53, 0, 0, 0, 0)
print(time.mktime(my_time_tuple))

# ----------------------------------------------------
# 4- módulo datetime do pacote datetime
#    objetos dessa classe date + time
# ----------------------------------------------------
print('-----------------------------------------------')

from datetime import datetime

# 1.1 today(): recupera dia/mês/ano corrente
hoje_completo = datetime.today() 
print(hoje_completo)

# 1.2 now(): igual ao today, exceto se a gente passar um timezone
hoje_completo = datetime.now() 
print(hoje_completo)

# 1.3 datetime(): crio um datetime
dt1 = datetime(2020, 10, 4, 14, 55)
print(dt1)

# 1.4 timestamp(): converto um datetime para timestamp
print(dt1.timestamp())

# ----------------------------------------------------
# 5- funções de formatação
# ----------------------------------------------------
from datetime import time
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

# ----------------------------------------------------
# 6- operações com data, hora e datetime
#    qualquer opração aritmética com date/time/datetime
#    retorna um objeto da classe timedelta
# ----------------------------------------------------
print('-----------------------------------------------')

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2, type(d1 - d2))

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2, type(dt1 - dt2))

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
print('dias:', delta.days)
print('microssegundos:', delta.microseconds)

delta2 = delta * 2
print(delta2)

print(date(2019,10,4) + delta2)






























