n = int(input())
jumlah = 0
for i in range (n):
    sequence = int(input())
    if sequence % 2 == 0 :
        jumlah += sequence

print(jumlah)