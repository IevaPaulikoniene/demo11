import random

print('hi')

if 5 > 3 :
    print("5 yra daugiau uz 3")

print("labas")

if 5 > 3 > 2:#pvz1
    print("5 yra daugiau uz 3")
    print("labas")

if 5 > 3 and 3 > 2:#pvz2
    print("5 yra daugiau uz 3")
    print("labas")

    taiKasKinta = True

    if taiKasKinta:
        print("tiesa")
    else:
        print("netiesa")

print("-----------------------------------")
randomNum = random.randint(0, 1000)
print(randomNum)

if randomNum < 10:  # false
    print("random skaicius yra vienzenklis")
elif randomNum < 100:  # false
    print("random skaicius yra dvizenklis")
elif randomNum < 1000:  # true
    print("random skaicius yra trizenklis")
else:
    print("random skaicius yra keturzenklis")

print("-----------------------------------")



randomNum = random.randint(0, 1000)
print(randomNum)

print("-----------------------------------")

if randomNum != 0:
    if randomNum % 2 == 0:
        print(randomNum / 2)
    else:
        print(randomNum * 2)

# 4 % 2 # 4 - 2 = 2; 2 - 2 = 0;
# 5 % 2 # 5 - 2 = 3; 3 - 2 = 1;

print("-----------------------------------")

#
# print("iveskite skaiciu:")
# #vartotojoIvestis = int(input())
# vartotojoIvestis = int(input("iveskite skaiciu:"))
#
# if vartotojoIvestis % 2 == 0:
#     print(f'skaicius {vartotojoIvestis} yra porinis')
# else:
#     print(f'skaicius {vartotojoIvestis} yra NEporinis')

print("-----------------------------------")

#print()
#print('---uzduotis1--')
#print()

#vardas = input('Iveskiti varda:')
#amzius = int(input("amzius:"))
#priezastis = input('priezastis:')
#print(vardas,amzius,priezastis)
###

#print('---2uzduotis--')
#norimas_simbolis = input("simbolis: ")
#print(f' {norimas_simbolis},{norimas_simbolis},{norimas_simbolis} \n {norimas_simbolis},{norimas_simbolis},{norimas_simbolis} \n {norimas_simbolis},{norimas_simbolis},{norimas_simbolis}')

#print('---3uzduotis---')
#simbolis = input("simbolis:")
#print(f' {simbolis}\n {simbolis}{simbolis}\n {simbolis}{simbolis}{simbolis}')

#print('---4uzduotis--')

#Iveskite_varda = input("vardas:")
#iveskite_amziu = int(input("amzius:"))
#ugis = str(input ('ugis:'))

#print('--5uzduotis--')
#print('iveskite 5 savo pazymius:')
#pirmas = int(input())
#antras = int(input())
#trecias = int(input())
#ketvirtas = int(input())
#penktas = int(input())
#vidurkis = (pirmas + antras + trecias + ketvirtas + penktas )/5
#print('vidurkis:', vidurkis)

#print('---6uzduotis--')
#metrai = float(input('iveskite metrus:'))
#centimetrai = metrai * 100
#milimetrai = metrai * 1000
#kilometrai = metrai / 1000

#print(f'{metrai} metru yra {centimetrai} centimetru')
#print(f'{metrai} metru yra {milimetru} milimetru')
#print(f'{metrai} metru yra {kilometrai} kilometru')

#print('--7uzduotis--')
#print('iveskite du skaicius:')
#pirmas = int(input())
#antras = int(input())

#print(f'{pirmas} + {antras} = {pirmas + antras},{pirmas} - {antras} = {pirmas - antras},{pirmas} * {antras} = {pirmas * antras}, {pirmas} / {antras} = {pirmas / antras}')
#print("----8uzd_isveskite_kokia_gaunasi_liekana----")

#print("iveskite du skaicius:")
#pirmas = int(input())
#antras = int(input())
#if pirmas > antras:
 #  print('liekana', pirmas % antras)
#else:
  #  print("antas % pirmas", antras % pirmas)

#print('--9uzduotis--')
#print('iveskite du skaicius')
#pirmas = int(input())
#antras = int(input())
#print('keliam laipsniu', pirmas**antras, antras**pirmas )
#print("Patikrinimo salygs if")
#print('---1uzduotis---')
#a = 1
#b = 2
#c = 3
#if a == b:
   # print('a lygu b')
#if b == c:
   # print("b lygu c")
#if a > b:
   # print("a didesnis uz b")
#if b > c * 2:
   # print("b didesnis uz c")
#if 1 % 2 == 0:
   # print('skaicius dalinasi is 2')
#if 2 % 2 != 0:
    #print('skaicius nesidalina is 2')
#if 3 > 0:
    #print("skaicius didesnis uz 0")
#if 3 < 0:
   # print('mazesnis uz 0')
#if 2 % 4:
   # print("dalinasi is 4")
#if 3 % 8:
    #print("dalinasi is 8")
#print("---2 uzduotis---")

#amzius = int(input())
#if amzius >= 18:
  # print('amzius', amzius, 'galite balsuoti')

#print('---3uzd--')
#pirmas = int(input())
#antras = int(input())
#trecias = int(input())
#vidurkis = (pirmas + antras + trecias) / 3
#if vidurkis >= 5:
 #   print('vidurkis teigiamas')
#else:
#    print('vidurkis neigiamas')
#print('--4uzd--')
#a = 20
#if a % 5 == 0:
   # print("a*1",a*1,"a*2",a*2,"a*3",a*3,"a*4",a*4,"a*5",a*5)
#else:
   # print('nesidalina')

#if 20==20:
   # print(a*a % 2)
#b = 21
#print(a+b,a-b,a*b,a%b)

#print('---5 uzd---')
#pasirinkimas = int(input('iveskite pasirinkima (1-4):'))
#if pasirinkimas == 1:
   # print('pasirinkote 1')
#elif pasirinkimas == 2:
    #print('pasirinkote ==2')
#elif pasirinkimas == 3:
    #print('pasirinkote 3')
#elif pasirinkimas == 4:
    #('pasirinkimas 4')
#a = 3
#b = 2
#c = 1
#d = 4

#if a < b :
   # print("didesnis uz antra:")
#elif b < c:
  #  print('didesnis uz trecia')
#elif c < a:
   # print('didesnis uz pirma')
#elif d < b:
   # print
print('---6uzd---')
git config --global user.name "IevaPaulikoniene"
git config --global user.email "ievapaulikonis@gmail.com"

































