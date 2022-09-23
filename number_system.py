def bin_To_dec(N):
    try:
        N = int(N)
    except ValueError:
        return "Error!"
    dec = 0
    i = 0
    while N:
        if N%10 == 1 or N%10 == 0:
            dec += (N%10) * (2**i)
        else:
            return "Error!"
        N //= 10
        i += 1
    return dec
def dec_To_bin(N):
    try:
        N = int(N)
    except ValueError:
        return "Error!"
    bin = 0
    i = 1
    while N:
        bin += (N%2) * i
        N //= 2
        i *= 10
    return bin

def dec_To_oct(N):
    try:
        N = int(N)
    except ValueError:
        return "Error!"
    oct = 0
    i = 0
    while N:
        oct += (N%8) * (10**i)
        N //= 8
        i += 1
    return oct
def oct_To_dec(N):
    try:
        N = int(N)
    except ValueError:
        return "Error!"
    dec = 0
    i = 0
    while N:
        dec += (N%10) * (8**i)
        N //= 10
        i += 1
    return dec

def dec_To_hex(N):
    try:
        N = int(N)
    except ValueError:
        return "Error!"
    hex = ""
    while N:
        rem = N%16
        if rem>9:
            if rem == 10:
                hex += "A"
            elif rem == 11:
                hex += "B"
            elif rem == 12:
                hex += "C"
            elif rem == 13:
                hex += "D"
            elif rem == 14:
                hex += "E"
            elif rem == 15:
                hex += "F"
        else:
            hex += str(rem)
        N //= 16
    return hex[::-1]
def hex_To_dec(N):
    N = N.upper()
    dec = 0
    j = len(N) - 1
    for i in range(len(N)):
        s = N[i]
        try:
            digit = int(s)
        except ValueError:
            if s == "A":
                digit = 10
            elif s == "B":
                digit = 11
            elif s == "C":
                digit = 12
            elif s == "D":
                digit = 13
            elif s == "E":
                digit = 14
            elif s == "F":
                digit = 15
            else:
                return "Error!"
        dec += digit * (16**j)
        j -= 1
    return dec

def oct_To_bin(N):
    N = oct_To_dec(N)
    return dec_To_bin(N)
def bin_To_oct(N):
    N = bin_To_dec(N)
    return dec_To_oct(N)
def bin_To_hex(N):
    N = bin_To_dec(N)
    return dec_To_hex(N)
def oct_To_hex(N):
    N = oct_To_dec(N)
    return dec_To_hex(N)
def hex_To_bin(N):
    N = hex_To_dec(N)
    return dec_To_bin(N)
def hex_To_oct(N):
    N = hex_To_dec(N)
    return dec_To_oct(N)


