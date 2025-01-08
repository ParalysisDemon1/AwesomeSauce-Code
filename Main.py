import random
import time
print("code keys: pythagorean calculator 1, goofball calculator (dice) 2")
requestedproduct = input("what code do you want? ")

if (requestedproduct == "1"):
    haveC = input("do you have the C? (y or n) ")

    if (haveC == "n"):
     a = int(input("input the A variable "))
     b = int(input("input the B variable "))

     a = a**2
     b = b**2
     answer = f"{a} + {b})"
     print("c^2 = ",answer)
     answer = a + b
     answer = answer**0.5
     print("c = ",answer)

    if (haveC == "y") :
     a = int(input("input the A variable "))
     c = int(input("input the C variable "))
     b = f"b^2 = {c}^2 - {a}^2"
     print(b)
     c = c**2
     a = a**2
     print(f"b^2 = {c} - {a}")
     b = c - a
     print(f"b = {b}^0.5")
     b = b**0.5
     print("b = ",b)

if (requestedproduct == "2"):
  count = 6
  while (count > 0):
    goofball = random.randint(1,6)
    print(f"goofball = {goofball}")
    count -= 1
    time.sleep(0.75)
  print(f"goofball calculator finished, goofball = {goofball}")
