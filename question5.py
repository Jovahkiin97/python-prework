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