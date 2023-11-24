# # 1
# number = int(input("Enter even numbers: "))
# if number % 2:
#     print('It is not even number!')
# else:
#     print("Thank you!")

#2
# f = int(input("Enter your age:"))
#
# if f <= 4 and f >= 60:
#     print("You do not have to pay!")
# elif f > 4 and f <= 18:
#     print("You have to pay 10.000.")
# elif f >18 and f <=60:
#     print("You have to pay 20.000")


 #3
# numb = int(input("Enter any integer: "))
#
# for t in range(1,11):
#     if not (numb % t):
#         print(f"{numb} soni {t} ga qoldiqsiz bo'linadi")


# #append bu listni oxiriga qoshadi
# #list
# things=[1, 2, "Hello world","cars", True, False]
# things.append("Odina")  #qoshish
# print(things)
#
# things.remove("cars")  #ayirish
# print(things)
#
# print(len(things))  #uzunligini korish
#
#
# #index bu 0dan boshlab sanidi
# things.insert(3,"sardor")  #index orqali qoshadi
# print(things)
#
# del things[0] #ochirib tashidi index va nomini yozamiz
# print(things)
#
#
# name=things[2] #bitta bizga kkli narsani chqarib beradi
# print(name)
#
# a=things[-1]
# b=things[-2]
# print(a, b)
#
# things[2], things[-1],= things[-1], things[2]  #joylashuvini ozgartiradi
# print(things)
#
# things.reverse()
# print(things)


#
# if things[3] == "Odina":
#     print("Hello Odina!")
# else:
#     print("Who are you?")

# number = list(range(1,10))
# print(number)
# things=[1, 2, "hello world", " Odina", True, False]
#
#
# if "Odina" in things:
#     print("Hello Odina!")
# else:
#     print("Who are you?")
#
# thing = [1,2,3,4,5,5]
# count = thing.count(5) #ichida nechta borligini aniqlab beradi
#
# thing = [3,8,5,1]
# a = thing.sort()  #sonlarni ketma ket chiqaradi
# print(count)
#
# things = [1,2," hello world","sardor", True, False]
# number = things.pop(2) #ctrl+x
# print(f"Salom{number}")
# print(things)
#
# if things.insert(2,"Umida") == True:
#     print("Ok")
#     print(things)
#
# list = [1, 3, 4, "Damas", "Captiva", True]
#
# #цикл for
# for x in list: #list boyicha tekshiruv olib boriladi
#     if x == "Damas":
#         print(f"{x} this car in list!")
#         break # x topilganda qidiruv toxtatilsin!
#     else:
#         print("It is not in our list!")


# list = [1, 3, 4, "Damas", "Captiva", True]

# #цикл for
# for x in list: #list boyicha tekshiruv olib boriladi
#     if x == "Damas":
#         print(f"{x} this car in list!")
#         continue# x topilganda bir marta toxtab kn yana davom ettiradi!
#
#     elif x == "Captiva":
#         print("Have")


    # else:
    #     print("It is not in our list!")

# number = int(input("Enter number:"))
# summa = 0
# for x in range(1, number + 1):
#     summa += x
# print(summa)

#1
n = input("Enter number: ")
num = 1
for i in range(1, n+1):
    num = num * i
    print(num)

# #2
names = ["Ali","Vali","Hasan","Husan","Olim"]
name = input("Enter your name:")
for name in names:
    print(f"Hello, {name}.")

print(f"Kod {len(names)} marta takrorlandi")

#3
a = range(11,100)
for d in a:
 if d % 2 == 1:
    print(d ** 3)

#4
nohuman = input("Bugun necha kishi bn suhbat qildingiz?>>>")
ismlar = []
for n in range(nohuman):
    ismlar.append(input(f" {n+1} -suhbat qilgan odamingiz kim edi: "))
print(ismlar)
