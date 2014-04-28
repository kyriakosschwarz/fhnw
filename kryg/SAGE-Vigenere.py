A = AlphabeticStrings()
M = "Treffpunkt Bahnhof Brugg zwanzig Uhr"
mes = A.encoding(M)
V = VigenereCryptosystem(A, 4)
K = A("FHNW")
enc = V(K)
enc(mes)
