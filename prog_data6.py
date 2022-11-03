# ----------------------------------------------------
# 6- operações com data, hora e datetime
#    qualquer opração aritmética com date/time/datetime
#    retorna um objeto da classe timedelta
# ----------------------------------------------------
print('-----------------------------------------------')

from datetime import date, time, datetime, timedelta
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2, type(d1 - d2))

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2, type(dt1 - dt2))


delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
print('dias:', delta.days)
print('microssegundos:', delta.microseconds)

delta2 = delta * 2
print(delta2)

print(date(2019,10,4) + delta2)
