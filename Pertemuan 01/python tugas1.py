# ==========================================================
# TUGAS PERTEMUAN 1
# ALGORITMA DAN PEMROGRAMAN
# Program Menentukan Bilangan Terbesar dari Tiga Bilangan
# ==========================================================

print("==============================================")
print(" PROGRAM MENENTUKAN BILANGAN TERBESAR")
print("==============================================")

# Input
a = float(input("Masukkan bilangan pertama  : "))
b = float(input("Masukkan bilangan kedua    : "))
c = float(input("Masukkan bilangan ketiga   : "))

# Proses menentukan bilangan terbesar
if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

# Output
print("\n==============================================")
print("HASIL")
print("==============================================")
print("Bilangan pertama :", a)
print("Bilangan kedua   :", b)
print("Bilangan ketiga  :", c)
print("----------------------------------------------")
print("Bilangan terbesar adalah =", terbesar)
print("==============================================")
