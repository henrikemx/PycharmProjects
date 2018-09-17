from datetime import datetime
from datetime import date

# Data final
d2 = datetime.strptime('2017-05-05', '%Y-%m-%d')

# Data inicial
d1 = datetime.strptime('2017-05-01', '%Y-%m-%d')

# Calculo da quantidade de dias
quantidade_dias = abs((d2 - d1).days)

print(quantidade_dias)
#print(f'Data atual pelo formato do sistema: {date.today()}')
#print(datetime.strptime(str(date.today()), '%Y-%m-%d'))
#print(date.weekday(date.today()))
#print(date.isoweekday(date.today()))
#print(date.ctime(date.today()))
#print(date.today())
#print(date.ctime(datetime(year=1964, month=11, day=24)))

#date1 = date.ctime(date.today())
#date2 = date.ctime(datetime(year=1964, month=11, day=24))

for e in date.ctime(date.today()):
    print(e, end='')
