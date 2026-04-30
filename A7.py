
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q

phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if phi % e != 0:
        break
    e += 1

d = 1
while (d * e) % phi != 1:
    d += 1

print("\n--- Key Generation ---")
print("n =", n)
print("phi(n) =", phi)
print("Public Key (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))

message = int(input("\nEnter numeric plaintext message: "))
cipher = (message ** e) % n
print("Encrypted Message:", cipher)

decrypted = (cipher ** d) % n
print("Decrypted Message:", decrypted)