#Question 4
#Write a function to return if the given year is a leap year

def is_leap_year(a_year): 
    if a_year%4==0:
        print ("Yes")
    elif a_year%100 and a_year%400==0:
        print ("Yes")
    else:
        print("No")

(is_leap_year(1997))