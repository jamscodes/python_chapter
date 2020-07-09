import random
def randInt(min=0, max=100):
    if type(min) or type(max) is not int:
        return "Error: both min and max must be passed as int"
    if min > max:
        # return "Error: first value (or min) should be less than second value (or max)" # this if we wanted an error to be thrown
        temp = min # this if we want to assume what the user meant
        min = max
        max = temp
    num = round(random.random() * (max - min) + min)
    return num
# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
# print(randInt(500,40)) 	    # depending on solution, will throw error or intuit what the user meant
# print(randInt(-4,-2)) 	    # should print a random integer between -4 to -2
# print(randInt("zero",40)) 	    # should print an error
# print(randInt(True))        # should print an error