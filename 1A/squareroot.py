angka = int(input())
hasil = 0

for i in range (1, angka + 1):
    hasil = i ** 2
    if hasil > angka :
        print("Not a perfect square")
        break
    if hasil == angka :
        print(i)
        break

