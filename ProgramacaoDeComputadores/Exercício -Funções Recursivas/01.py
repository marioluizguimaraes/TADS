def conta_divisores_r(n, div):
    if div == 1:
        return 1
    else:
        if n % div == 0:
            return 1 + conta_divisores_r(n, div - 1)
        else:
            return 0 + conta_divisores_r(n, div - 1)

def conta_divisores(n):
    return conta_divisores_r(n, n)


