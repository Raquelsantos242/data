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