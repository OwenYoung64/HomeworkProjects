sum = 4
pro = 5
	# If their sum and their product are equal - tell the user
while(sum!=pro):
    if(sum!=4 and pro != 5):
        print("your sum and product need to be equal")
    num1 = input("what is your first number")
    num2 = input("what is your second number")
    sum = (int(num1) + int(num2))
    pro= (int(num1) * int(num2))


print("your sum and product are equal")
	# otherwise ask for two more numbers