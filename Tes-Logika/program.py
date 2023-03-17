n = int(input("Masukkan nilai N: "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FULLSTACK")
    elif i % 3 == 0:
        print("FRONTEND")
    elif i % 5 == 0:
        print("BACKEND")
    else:
        print(i)
