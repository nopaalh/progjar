digit = int(input())

digitlist = [int(x) for x in str(digit)]
jumlah = 0
for i in digitlist:
    jumlah += i

print(jumlah)