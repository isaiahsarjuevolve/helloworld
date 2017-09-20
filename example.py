import datetime

def current_year():
 current_date = datetime.datetime.now()
 return current_date.year

def current_plus(years):
 plus_time = current_year() + years
 return plus_time

def main():
 print(current_plus(int(input("How many?\n>")))) 

main()
