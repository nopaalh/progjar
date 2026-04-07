angka = int(input())
total = 0

if angka > 0 :
    for i in range (1 , angka + 1):
        total += i
elif angka < 0 :
    for i in range(-1 , angka  - 1 , -1):
        total += i
else : 
    total = 0

print(total)
