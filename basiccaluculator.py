a=int(input("enter a value:"))
b=int(input("enter b value:"))
while True:
  print("1.add")
  print("2.subtraction")
  print("3.Multiplication")
  print("4.Division")
  print("5.Modulus")
  print("6.exit")
  print("enter your choice:")
  choice=int(input())
  if(choice==1):
    print("The addition of two numbers is:",a+b)
  elif(choice==2):
    print("The subtraction of two numbers is:",a-b)
  elif(choice==3):
    print("The Multiplication of two numbers is",a*b)
  elif(choice==4):
    print("The division of two numbers is:",a/b)
  elif(choice==5):
    print("The modulus of two numbers is:",a%b)
  elif(choice==6):
    break

  else:
    print("invalid number")

