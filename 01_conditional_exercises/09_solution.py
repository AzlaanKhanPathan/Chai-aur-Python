year = 2025 

if ( year % 400 == 0 ) or ( year % 4 == 0 and year % 100 !=0 ):
    print(year, "Is a Leap Year")
else: 
    print(year , "is NOT a leap year")