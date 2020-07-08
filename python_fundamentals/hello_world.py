# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = "Jonathan"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)	# with a comma
print("Hello " + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

oldShout = "I USED TO BE SHOUTING"
print(oldShout.lower())

oldQuiet = "i used to be quiet"
print(oldQuiet.upper())

print("This is the length of oldShout + oldQuiet: ", len(oldQuiet) + len(oldShout))

centerText = "I am text that's been moved!"
print(centerText.center(100))