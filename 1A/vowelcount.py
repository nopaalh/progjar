vowel = ['a','i','u','e','o','A','E','I','U','O']

kata = input()
jumlah = 0

for i in kata:
    if i in vowel:
        jumlah += 1

print(jumlah)