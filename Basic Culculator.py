
    
#num1 = float(input(" Enter num1: "))
#ope = input(" Enter operator: +, -, *, /, %: ")
#num2 = float(input(" Enter num2: "))

#if ope == "+":
#   print ("Result: ", (num1 + num2))
#elif ope == "-":
#   print ("Result: ", (num1 - num2))
#elif ope == "/":
#    print ("Result: ", (num1 / num2))
#elif ope == "*":
#    print ("Result: ", (num1 * num2))
#elif ope == "%":
#    print ("Result: ", (num1 % num2))
#else:
#    print (" Try next time")
# در فرومول بالا پروسه فقط یکبار تکرار میشد و اگر بار دیگر میخاستیم انجام دهیم باید رن میکردیم 

# حالا اگر باخیم پروسه تا وقتی که ما میخایم پیش برود چی کار باید بکنیم 


while True:
    num1 = (float(input("Enter Number 1: ")))
    ope = input("Enter operetor: +, -, *, /, %: ")
    num2 = (float(input("Enter Number 2: ")))

    if ope == "+":
        print("Reslut: ", num1 + num2)
    elif ope == "-":
        print("Reslut: ", num1 - num2)
    elif ope == "*":
        print("Reslut: ", num1 * num2)
    elif ope == "/":
        print("Reslut: ", num1 / num2)
    elif ope == "%":
        print("Reslut: ", num1 % num2)
    
    else:
        break

    

