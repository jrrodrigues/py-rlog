# Desafio 3 - Analisador de Gastos
import pandas as pd
import matplotlib.pyplot as plt

def analisar_gastos():
    # 1. Ler o arquivo
    # TODO: use pd.read_csv()
    try:
        df = pd.read_csv("gastos.csv")
        df['data'] = pd.to_datetime(df['data'])
    except FileNotFoundError:
        print("Arquivo gastos.csv não encontrado!")
        return

    print("=== SEUS GASTOS ===")
    print(df)

    # 2. Total por categoria
    print("\n--- Total por categoria ---")
    total_categoria = df.groupby('categoria')['valor'].sum()
    print(total_categoria)

    # 3. Mês que mais gastou
    # TODO: Crie uma coluna 'mes' a partir da data
    df['mes'] = df['data'].dt.to_period('M')
    total_mes = df.groupby('mes')['valor'].sum()
    print("\n--- Total por mês ---")
    print(total_mes)
    print(f"\nMês que mais gastou: {total_mes.idxmax()} - R$ {total_mes.max():.2f}")

    # 4. Gráfico
    total_categoria.plot(kind='bar', title='Gastos por Categoria')
    plt.ylabel('R$')
    plt.tight_layout()
    plt.savefig('grafico_gastos.png') # salva a imagem
    print("\nGráfico salvo como grafico_gastos.png")
    plt.show()

analisar_gastos()