def conta_algarismos(n):
    if (n//10 == False):
        return 1
    else:
        return conta_algarismos(n//10) + 1

print(conta_algarismos(1234))