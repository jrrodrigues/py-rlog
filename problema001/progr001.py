# Desafio 1 - Calculadora de Aposentadoria da Poupança

def calcular_duracao_poupanca():
    print("=== Calculadora de Poupança ===")
    
    # 1. Entrada de dados
    saldo = float(input("Quanto você tem hoje? R$ "))
    saque_mensal = float(input("Quanto quer sacar por mês? R$ "))
    rendimento = float(input("Rendimento mensal em % (ex: 0.67): ")) / 100

    meses = 0
    
    # 2. Lógica principal
    # TODO: Crie um loop while que rode enquanto saldo > 0
    
    while saldo > 0:
        # a) Aplica o rendimento do mês
        saldo = saldo * (1 + rendimento)
        
        # b) Tira o saque (se não tiver saldo suficiente, zera)
        if saldo >= saque_mensal:
            saldo -= saque_mensal
        else:
            # último mês - saca o que sobrou
            saque_mensal = saldo
            saldo = 0
            
        meses += 1
        
        # c) Segurança: para não rodar infinito se o rendimento for maior que o saque
        if meses > 1200: # 100 anos
            print("Seu dinheiro nunca acaba! Rendimento maior que saque.")
            break
        
        print(f"Mês {meses}: saldo restante R$ {saldo:.2f}")

    # 3. Saída
    print("\n--- RESULTADO ---")
    print(f"Seu dinheiro dura {meses} meses, que são {meses // 12} anos e {meses % 12} meses.")

# Roda o programa
calcular_duracao_poupanca()