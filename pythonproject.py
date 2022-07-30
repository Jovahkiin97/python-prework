# Question 1
# Write a function to print "hello_USERNAME!"

def hello_name():
    prompt = "What's your name?"
    user_name = input(prompt)
    print("\nhello_" + user_name.upper() + "!")

hello_name()

# Question 2
#Write a function that prints the odd numbers from 1-100 and returns nothing

def first_odds(n):
    return [x for x in range(0, n) if x%2 != 0]

print(first_odds(100))

# Question 3
# Write a function to return the max number of a given list.

a_list = [150, 4, 300, 14, 11, 9000]

def max_num_in_list(a_list):
    return max(a_list)

print (max_num_in_list(a_list))

#Question 4
#Write a function to return if the given year is a leap year

def is_leap_year(a_year): 
    if a_year%4==0:
        print ("True")
    elif a_year%100 and a_year%400==0:
        print ("True")
    else:
        print("False")

(is_leap_year(1997))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers

def is_consecutive(a_list):
    a_list = [1, 2, 3, 4, 5, 6]
    maximum = max(a_list)
    if sum(a_list) == maximum * (maximum+1) /2 :
        return True
    else:
        return False
    
print(is_consecutive("a_list"))