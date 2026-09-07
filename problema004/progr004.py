# Desafio 4 - Forca com Ranking
import random

PALAVRAS = ["python", "poupanca", "programar", "dados", "algoritmo"]

def jogar_forca():
    palavra_secreta = random.choice(PALAVRAS)
    letras_certas = ["_"] * len(palavra_secreta)
    letras_erradas = []
    tentativas = 6

    print("=== JOGO DA FORCA ===")

    while tentativas > 0 and "_" in letras_certas:
        print(f"\nPalavra: {' '.join(letras_certas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {letras_erradas}")

        letra = input("Digite uma letra: ").lower()

        # TODO 1: Validação - não pode repetir letra e tem que ser 1 letra só
        if len(letra)!= 1 or not letra.isalpha():
            print("Digite apenas UMA letra!")
            continue
        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra!")
            continue

        # TODO 2: Lógica principal
        if letra in palavra_secreta:
            print("Acertou!")
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_certas[i] = letra
        else:
            print("Errou!")
            letras_erradas.append(letra)
            tentativas -= 1

    # Fim de jogo
    if "_" not in letras_certas:
        print(f"\nVocê GANHOU! A palavra era {palavra_secreta}")
        # TODO 3: Salvar no ranking
        nome = input("Digite seu nome para o ranking: ")
        erros = len(letras_erradas)
        with open("ranking.txt", "a", encoding="utf-8") as f:
            f.write(f"{nome} - {palavra_secreta} - {erros} erros\n")
        print("Salvo no ranking.txt!")
    else:
        print(f"\nVocê PERDEU! A palavra era {palavra_secreta}")

jogar_forca()