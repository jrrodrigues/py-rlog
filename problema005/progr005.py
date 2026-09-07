# Desafio 5 - Previsor de Preços com IA
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def treinar_modelo():
    # 1. Carregar dados
    df = pd.read_csv("casas.csv")

    # X = o que o modelo usa pra aprender, y = o que ele tem que prever
    X = df[["tamanho_m2", "quartos"]]
    y = df["preco"]

    # 2. Separar em treino e teste (80% treina, 20% testa)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Criar e treinar o modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # 4. Ver a nota do modelo
    nota = modelo.score(X_test, y_test)
    print(f"Nota do modelo: {nota*100:.1f}% de acerto")

    # 5. Prever casa nova
    print("\n=== PREVISOR DE CASAS ===")
    tamanho = float(input("Tamanho em m2: "))
    quartos = int(input("Qtd de quartos: "))

    # TODO: O modelo espera um DataFrame com o mesmo formato do X
    casa_nova = pd.DataFrame([[tamanho, quartos]], columns=["tamanho_m2", "quartos"])
    preco_previsto = modelo.predict(casa_nova)

    print(f"\n>>> Preço previsto: R$ {preco_previsto[0]:,.2f}")

    # Bônus: mostra a fórmula que a IA aprendeu
    print(f"\nFórmula da IA: Preço = {modelo.coef_[0]:.2f} * m2 + {modelo.coef_[1]:.2f} * quartos + {modelo.intercept_:.2f}")

treinar_modelo()