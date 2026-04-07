jumlah = int(input())
data = {}

for i in range (jumlah):
    kata = input().split()
    k = kata[0]
    v = kata [1]
    data[k] = v

    
target = input()
print(data[target])