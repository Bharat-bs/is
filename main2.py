alpha = "abcdefghijklmnopqrstuvwxyz"


def encrpt(message, key):
    n = len(message)
    enmessage = ""
    messagemat = matrixmultiplication(key, message)
    messagemat = transpose(messagemat)
    for i in range(n):
        for j in range(n):
            enmessage += alpha[(messagemat[i][j] % 26)]
    return enmessage


def matinp(message, n):
    l = [[23] * n for i in range(0, n)]
    c = 0
    for i in range(n):
        for j in range(n):
            try:
                l[i][j] = alpha.index(message[c])
                c += 1
            except:
                pass
    l = transpose(l)
    return l


def minor(matrix, r, c):
    n = len(matrix)
    l = []
    for i in range(n):
        l1 = []
        for j in range(n):

            if (i != r and j != c):
                l1.append(matrix[i][j])
        l.append(l1)
    l.remove([])
    print(l)
    return l


def determinant(m):
    if len(m) == 1:
        return m[0][0]
    d = 0
    for c in range(len(m)):
        d += ((-1) ** c) * m[0][c] * determinant(minor(m, 0, c))
    return d % 26


def cofactor(matrix):
    n = len(matrix)
    cofact = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            m = minor(matrix, i, j)
            cofact[i][j] = ((-1) ** (i + j)) * determinant(m)
    return cofact


def transpose(matrix):
    n = len(matrix)
    trans = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            trans[i][j] = matrix[j][i]
    return trans


def multiplicative_inverse(determinant):
    inverse = -1
    for i in range(26):
        x = determinant * i
        if x % 26 == 1:
            inverse = i
            break
    print(inverse)
    return inverse % 26


def inverse(matrix):
    n = len(matrix)
    inverse = [[0] * n for i in range(n)]
    D = determinant(matrix)
    I = multiplicative_inverse(D)
    cofact = cofactor(matrix)
    adjoint = transpose(cofact)
    for i in range(n):
        for j in range(n):
            inverse[i][j] = ((I) * adjoint[i][j]) % 26
    return inverse


def matrixmultiplication(mat1, mat2):
    result = [[0] * len(mat1) for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += (mat1[i][k] * mat2[k][j])
    return result


def deccrpt(cipher, key):
    n = len(cipher)
    dec = [[i] * n for i in range(n)]
    keyi = inverse(key)
    res = matrixmultiplication(keyi, cipher)
    for i in range(n):
        for j in range(n):
            dec[i][j] = res[i][j] % 26
    dec = transpose(dec)
    denmessage = ""
    for i in range(n):
        for j in range(n):
            denmessage += alpha[dec[i][j]]
    return denmessage


def encryption(n):
    usinp = input("Enter the plain text : ")
    message = matinp(usinp, n)
    keyinp = input("Enter the key : ")
    key = matinp(keyinp, n)
    print("Plain text matrix : ", message)
    print("Key matrix : ", key)
    cipher = encrpt(message, key)
    print("Encrytped text", cipher)


def decryption(n):
    usinp = input("Enter the cipher text : ")
    message = matinp(usinp, n)
    keyinp = input("Enter the key : ")
    key = matinp(keyinp, n)
    print("cipher text matrix : ", message)
    print("Key matrix : ", key)
    plain = deccrpt(message, key)
    print("decrpyted text", plain)


def knownplaincipher(n):
    usinp = input("Enter the plain text : ")
    message = matinp(usinp, n)
    ciphermat = input("Enter the cipher text : ")
    cipher = matinp(ciphermat, n)
    print("plain text matrix : ", message)
    print("cipher text matrix : ", cipher)
    dec = [[i] * n for i in range(n)]
    plaini = inverse(message)
    res = matrixmultiplication(cipher, plaini)
    for i in range(n):
        for j in range(n):
            dec[i][j] = res[i][j] % 26
    dec = transpose(dec)
    key = ""
    for i in range(n):
        for j in range(n):
            key += alpha[dec[i][j]]
    print("key matrix : ", matinp(key, n))
    print("key matrix as text : ", key)


# print("ENCRYPTION ")
# encryption(3)
# print("DECRYPTION ")
# decryption(3)
# print("KNOWN CT-PT ")
# knownplaincipher(3)
multiplicative_inverse(5)
