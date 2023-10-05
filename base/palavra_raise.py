def dividir(a,b):
    if b == 0:
        #a palavra raise cria exceções personalizadas
        raise ValueError("Divisão por zero não é permitido.")
    return a / b

try:
    resultado = dividir(10,0)
    print(resultado) 
except ValueError as e:
    print(f"Erro: {e}")
