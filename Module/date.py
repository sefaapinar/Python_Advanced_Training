from datetime import datetime
from typing import List

from datetime import datetime
from datetime import *
# from datetime import date
# import datetime

# result = dir(datetime.now)

simdi = datetime.now()
result = datetime.now().year
result = simdi.time()

simdi.today()

result = datetime.ctime(simdi) #Bugünün saatini belirler.
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%D')
result = datetime.strftime(simdi,'%M')

# t = '21 Nisan 2021'
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)
# print(result)

# t = '21 April 2019 Hour 10:12:30'

# dt = datetime.strptime(t,'%D %B %Y' )

birthday = datetime(2000,12,4)

result = datetime.timestamp(birthday) #Saniye bilgisi veriri.

result = datetime.fromtimestamp(result) #Datetime bilgisi verir.

result = datetime.fromtimestamp(0)

result = simdi - birthday #time delta.

result = result.days

result = simdi + timedelta(days=10)
print(result)