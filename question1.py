# Question 1
# Write a function to print "hello_USERNAME!"

def hello_name():
    prompt = "What's your name?"
    user_name = input(prompt)
    print("\nhello_" + user_name.upper() + "!")

hello_name()