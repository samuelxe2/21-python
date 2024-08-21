def dividir(dividendo, divisor):
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    
    if dividendo == -2**31 and divisor == -1:
        return 2**31 - 1
    
    dividendo_abs = abs(dividendo)
    divisor_abs = abs(divisor)
    
    cociente = 0
    bit = 1
    
    while (divisor_abs << 1) <= dividendo_abs:
        divisor_abs <<= 1
        bit <<= 1
    
    while bit > 0:
        if dividendo_abs >= divisor_abs:
            dividendo_abs -= divisor_abs
            cociente |= bit
        
        divisor_abs >>= 1
        bit >>= 1
    
    return -cociente if (dividendo < 0) != (divisor < 0) else cociente

# Ejemplo de uso con input
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

print("Resultado:", dividir(dividendo, divisor))

