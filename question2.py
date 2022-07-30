# Question 2
#Write a function that prints the odd numbers from 1-100 and returns nothing

def first_odds(n):
    return [x for x in range(0, n) if x%2 != 0]

print(first_odds(100))