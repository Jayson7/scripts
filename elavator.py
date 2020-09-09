# this is a simple elevator analyzer
# jaysonCodes


pick = input(" please press a number from 1 - 20:   ")


alph = "a", "A", "b", 'B', 'c', 'C', 'd','D', 'E', 'e', 'f', 'F', 'g', 'G', 'h', 'i', 'H', 'I', 'J', 'K', 'L','l','j', 'k', 'm', 'M', 'N', 'n', 'o', 'O', 'p', 'P', 'Q','q', 'r', 'R','s','S','t','T','u','U','v','V','W','w','x','X','y','Y','z','Z'

pick = int(pick)

if pick in alph:
    print("Numbers please")
    print("you are rquired to input integers")

if pick > 20:
    print("You are wrong")
    print("print please input a correct location")
if pick < 20:
    print('welcome') 
else:
    print("you are wrong")

if pick in range(1, 20):
    print(pick * "*")
    print(pick * "||")
    pick = str(pick)
    print("You are going to ground " + pick)





#jaysoncodes