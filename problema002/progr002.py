# Desafio 2 - Validador de CPF

def validar_cpf(cpf):
    # 1. Limpeza - tira pontos e traço
    cpf = cpf.replace(".", "").replace("-", "").strip()

    # 2. Validações básicas
    if len(cpf)!= 11 or not cpf.isdigit():
        return False

    # CPF com todos os dígitos iguais é inválido (ex: 11111111111)
    if len(set(cpf)) == 1:
        return False

    # 3. Calcula o 1º dígito verificador
    # TODO: sua lógica aqui
    # Regra: soma = (d1*10 + d2*9 + d3*8... d9*2)
    # resto = (soma * 10) % 11
    # se resto == 10, vira 0

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    if digito1!= int(cpf[9]):
        return False

    # 4. Calcula o 2º dígito verificador
    # TODO: agora inclui o digito1 na conta
    # Regra: soma = (d1*11 + d2*10... d9*3 + digito1*2)

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    if digito2!= int(cpf[10]):
        return False

    return True

# Teste
cpf_teste = input("Digite o CPF: ")
if validar_cpf(cpf_teste):
    print("✓ CPF VÁLIDO")
else:
    print("✗ CPF INVÁLIDO")

# Teste rápido com esses valores (tem que dar Válido):
# 52998224725
# 529.982.247-25