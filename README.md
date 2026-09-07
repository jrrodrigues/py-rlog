# py-rlog

Cinco problemas, do mais fácil pro mais difícil. Todos ótimos pra raciocínio lógico + Python

### _1. Calculadora de Aposentadoria da Poupança _

_Baseado no que você me perguntou no início._[Iniciante]

_Problema:_ O usuário digita quanto tem hoje, quanto quer sacar por mês e o rendimento da poupança. O programa diz por quantos meses o dinheiro dura.

_Entrada:_ 22000, 1000, 0.67%
_Saída:_ "Seu dinheiro dura 24 meses. Sobra R$ 0,00"

> Habilidade: loop while, if, porcentagem.

### _2. Detector de CPF Válido [Lógica]_

_Problema:_ Recebe um CPF "123.456.789-09" e diz se é válido ou não pelas regras dos 2 dígitos verificadores. Sem usar biblioteca pronta.

_Entrada:_ 52998224725
_Saída:_ Válido / Inválido

> Habilidade: string, lista, resto de divisão %, lógica de algoritmo.

### _3. Analisador de Gastos _

_Problema:_ Você tem um arquivo `gastos.csv` com colunas: data, categoria, valor. O programa deve:

1. Ler o CSV
2. Mostrar total gasto por categoria
3. Mostrar em qual mês gastou mais
4. Criar um gráfico de barras[Pandas]

_Entrada:_ http://gastos.csv
_Saída:_ Tabela + gráfico

> Habilidade: pandas, groupby, matplotlib. É seu primeiro projeto de dados.

### _4. Jogo da Forca com Ranking [Intermediário]_

_Problema:_ O programa escolhe uma palavra secreta de uma lista. O usuário tem 6 tentativas. Salva nome + tentativas usadas num arquivo `ranking.txt`.

_Extras:_ Não pode repetir letra, mostra letras já tentadas.

_Entrada:_ letra por vez
_Saída:_ "\_ \_ \_ \_", "Você ganhou em 4 tentativas!"

> Habilidade: funções, arquivos, random, lógica de jogo.

### _5. Previsor de Preço Simples [Ciência de Dados]_

_Problema:_ Com a base `casas.csv` (tamanho_m2, quartos, preço). Treine uma Regressão Linear e preveja o preço de uma casa nova que o usuário digitar.

_Entrada:_ 70 m2, 2 quartos
_Saída:_ "Preço previsto: R$ 350.000"

> Habilidade: scikit-learn, train_test_split, LinearRegression. Seu primeiro modelo de ML.

Quer que eu te mande o código-base do _Problema 1_ pra você começar agora e ir completando?
