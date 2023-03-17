total = 0
# range di bawah 2021
for i in range(1, 2021):
  #kelipatan 3/7 -> modulus 3/7
    if i % 3 == 0 or i % 7 == 0:
      #print(i)
      total += i

print("Total penjumlahan bilangan asli di bawah 2021 yang merupakan kelipatan 3 atau 7 adalah:", total)
