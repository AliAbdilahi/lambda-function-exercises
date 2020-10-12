from datetime import date
current_date = date.today()
print(current_date)
year= lambda current_date: current_date.year
print (year(current_date))  
month= lambda current_date: current_date.month
print (month(current_date))
day= lambda current_date: current_date.day
print (day(current_date))  
