#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message
#and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


#solution
#---------


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        if largest is None:
            largest = int(num)
        if smallest is None:
            smallest = int(num)
        if int(num) > largest:
            largest = int(num)
        if int(num) < smallest:
            smallest = int(num)
    except ValueError:
        print ("Invalid input")
        continue
print("Maximum is"+str(largest))
print("Minimum is"+str(smallest))



#Your Output
#------------
#Invalid input
#Maximum is 10
#Minimum is 2


#Desired Output
#--------------
#Invalid input
#Maximum is 10
#Minimum is 2
