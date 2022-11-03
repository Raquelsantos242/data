from datetime import datetime

# 1.1 today(): recupera dia/mês/ano corrente
hoje_completo = datetime.today() 
print(hoje_completo)

# 1.2 now(): igual ao today, exceto se a gente passar um timezone
hoje_completo = datetime.now() 
print(hoje_completo)

# 1.3 datetime(): crio um datetime
dt1 = datetime(2020, 10, 4, 14, 55, 9)#ano, mês, dia, hora, minuto, segundo
print(dt1)

# 1.4 timestamp(): converto um datetime para timestamp
print(dt1.timestamp())