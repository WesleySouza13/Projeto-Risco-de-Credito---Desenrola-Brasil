![image](https://github.com/user-attachments/assets/c538c6ee-3403-4cc9-9f48-d811da300119)



# Previsão do Volume Financeiro de Renegociações no Desenrola Brasil 

O Desenrola Brasil, ou simplesmente "desenrola", é um programa implementado pelo ministerio da fazenda que visa a renegociação de dívidas de natureza privada de pessoas físicas inscritas em cadastro de inadimplentes, bem como a redução do endividamento e facilitação de acesso ao mercado de crédito pelas mesmas. 

## Objetivo: 
 O governo e instituições financeiras precisam prever o volume de renegociações para se organizarem com antecedência, direcionarem campanhas e alocar recursos com precisão.
Com isso, temos os seguintes pontos:

- Criar um modelo confiável para prever o volume financeiro;
- Apoiar, por meio de análises, decisões para o setor público e privado;
- Analisar tendências e padrões que influenciam o comportamento de renegociação.

  ## Base de Dados

 Deixarei a base de dados na pasta "data" deste repositório.


# Explicação das Variáveis
DATA_BASE: Data de referência em que o dado foi coletado 

TIPO_DESENROLA: Categoria ou modalidade da renegociação dentro do programa Desenrola Brasil

UNIDADE_FEDERACAO: Unidade da Federação (UF) onde a operação foi registrada

COD_CONGLOMERADO_FINANCEIRO: Identificador numérico único do conglomerado financeiro participante da renegociação

NOME_CONGLOMERADO_FINANCEIRO: Nome do conglomerado financeiro (banco ou instituição) (público ou privado) envolvido na renegociação

NUMERO_OPERACOES: Quantidade total de operações de renegociação realizadas no mês

VOLUME_OPERACOES: Volume financeiro total (em reais) das operações realizadas no período.


# Entendimento das variáveis:

# Bancos com maiores frequencia no programa: 

![image](https://github.com/user-attachments/assets/639855e8-ae46-489b-b354-ced60759a22b)

O Bradesco foi o banco que mais apareceu entre os participantes do programa desenrola. 


# Bancos com maior volume de operações:

![image](https://github.com/user-attachments/assets/5c21b6f9-fe2f-41fd-b956-966c6d912ffe)

O banco Nubank apresenta um volume de negociações de dívidas esmagador em relação aos demais bancos.

O dado apresentado revela que o Nubank lidera com folga o ranking de volume de negociações de dívidas, com 547.423 transações. Esse número é significativamente superior ao da Caixa Econômica Federal, que ocupa o segundo lugar com 400.810 negociações. Em seguida, aparecem o BTG Pactual (332.136), o Itaú (318.524) e o Santander (298.376).

Esse cenário reforça a atuação agressiva do Nubank no segmento de crédito e renegociação de dívidas, reflexo de sua grande base de clientes, forte presença digital e políticas de crédito mais acessíveis, que muitas vezes levam a um volume maior de renegociações.

# Estados com maior volume de renegociações:

![image](https://github.com/user-attachments/assets/66c51616-a424-448d-85fd-4868259f22cd)

Como o gráfico já deixa explícito, o volume de operações em São Paulo é esmagador em relação aos outros estados, o que evidencia a forte concentração econômica e populacional na região.

# Comportamento temporal do volume de operações:

# Série: 

![image](https://github.com/user-attachments/assets/372cdd01-9b0f-4bf3-b7a8-22909317be88)

O gráfico mostra uma instabilidade em relação ao volume de operações entre as datas de novembro de 2023 e junho de 2024. No entanto, observa-se uma melhora a partir do meio de 2024 e mais acentuadamente no final do ano. Uma variável que pode explicar esse comportamento é a sazonalidade, como o pagamento do 13º salário no segundo semestre, que amplia a capacidade de quitação de dívidas, além de fatores culturais e psicológicos, como a superstição de não terminar o ano com pendências financeiras.

# Distribuição Temporal: Tendecia do volume

![image](https://github.com/user-attachments/assets/95504a58-95d1-4d24-bf3c-9548a0f21b1e)

# Sazonalidade:

![image](https://github.com/user-attachments/assets/a72e1c11-03c5-4a66-ac5d-4f3e41147256)

O gráfico de sazonalidade corrobora a análise que fizemos sobre o comportamento da série, evidenciando padrões recorrentes que explicam as variações no volume de operações ao longo do tempo.

# Volatidade da Série:

A volatilidade da série explica os desvios observados ao longo do tempo. A seguir, apresentamos o gráfico que fundamenta o nosso estudo.

![image](https://github.com/user-attachments/assets/01bae4fd-a039-428c-94f4-ae5bc6a7923a)

# Gráficos de Autocorrelação: 

Explicando autocorrelaçao de forma mais básica possivel: 

Esse tipo de vizualizaçao nos mostra o comportamento de ontem em relaçao a hoje, ou seja, "qual é a correlaçao de ontem comparado a hoje?".

Por exemplo:

Se eu sou alto hoje, será que amanhã também serei alto?

- O eixo X explica os dias passados (autocorrelaçao até 30 dias)

- O Y explica o nível de autocorrelaçao (-1 a 1)

  ![image](https://github.com/user-attachments/assets/386fc3f1-bc16-49b6-92bb-9c6e51e8a57f)

  Explicando resultados:

  **TIPO_DESENROLA:**

- Os dias apresentam boa autocorrelaçao, variando pouco ou quase nada em relaçao ao tempo. Se depender apenas dessa variável, podemos trabalhar com modelos recorrentes. 

**COD_CONGLOMERADO_FINANCEIRO**

 - O passado apresenta autocorrelação, porém baixa. Com o tempo, essa autocorrelação some. 

 **NUMERO_OPERACOES**

 - Mesma lógica da última coluna, a autocorrelação some com o tempo. 

 **VOLUME_OPERACOES** 

 - Autocorrelação fraca, também some com o tempo. 

 **MEDIA_OPERACOES**

 - Boa autocorrelação, que se mantém constante durante um tempo. Mas nao apresenta um score muito significativo. 

# Modelagem:

**Modelos utilizados na modelagem:**

Árvore de Decisão (DecisionTreeRegressor)

Regressão Linear (LinearRegression)

XGBoost (XGBRegressor)

AdaBoost (AdaBoostRegressor)

Random Forest (RandomForestRegressor)

Ridge (com alpha=0.1)

Lasso (com alpha=0.1)

Utilizei o MinMaxScaler para escalar os nossos dados, e o OneHot Encoder para fazer o encoder. 

# Métricas do treinamento: 

1. Melhor modelo: DecisionTreeRegressor

R²: 0.77 

MAE: ~197 mil

MSE: ~9 tri

Melhor desempenho geral, especialmente no R² e erro absoluto. Indica que o modelo consegue capturar bem as não linearidades do problema.

2. XGBRegressor

R²: 0.77 

MAE: ~202 mil

MSE: ~9 tri

Excelente desempenho, muito próximo da árvore de decisão. Vantagem: maior robustez a overfitting e capacidade de generalização.

3. RandomForestRegressor

R²: 0.67

MAE: ~170 mil 

MSE: ~13 tri

Apesar do menor R², apresentou um dos menores MAE. Pode indicar que é um modelo conservador, com boas previsões em média, mas que não explica toda a variância.

4. AdaBoostRegressor

R²: 0.70

MAE: ~1 milhão

MSE: ~12 tri

Não conseguiu reduzir o erro absoluto, indicando dificuldade em ajustar aos dados.

5. Modelos Lineares (LinearRegression, Ridge, Lasso)
R²: ~0.575

MAE: ~960 mil

MSE: ~16 a 17 tri

Pior desempenho geral, altos erros, explicam pouco da variância dos dados. Provavelmente, o problema é não linear, o que explica o fraco desempenho dos modelos lineares.

# Optuna:

**Utilizei o Optuna para ajuste de parametros do modelo, e escolhi para o estudo o modelo de arvore de decisao e o xgboost**

---Resumo do estudo---

O modelo de árvore de decisão apresentou melhores métricas com os parâmetros default, porém, para o nosso problema, é necessário um pouco mais de complexidade. Com isso, conduzi um estudo aprofundado com o segundo melhor modelo (XGBoost), utilizando o Optuna.

Depois do estudo, observei que, com o aumento da complexidade do modelo de árvore de decisão, as métricas caíram de forma significativa.

O contrário aconteceu com o XGBoost, que obteve quase 80% de explicação na variabilidade dos dados, com um MAE adequado para o nosso problema.


**---- Métricas ----**

 - metricas XGBoost (pós optuna): {'r2_score': 0.7776174521667012, 'mean_absolute_error': 192982.35, 'mean_ap_error': 5.802680771293433, 'mean_square_error': 8839704999617.56}


 - métricas arvore de decisao (pós optuna) {'r2_score': 0.623834479833066, 'mean_absolute_error': 366904.74, 'mean_ap_error': 248.16838087138714, 'mean_square_error': 14952577266971.52}


# Gráfico de predições

![image](https://github.com/user-attachments/assets/a2bfb1fc-4cb6-4523-aa1c-f2abe4946910)


# Cross Validate - Utilizando r2_score

Cross-Validation — R² Score
Resultados:
Árvore de Decisão

Score Máximo: 0.9515

Score Mínimo: 0.2898

Score Médio: 0.7813

Desvio Padrão: 0.1925

XGBoost

Score Máximo: 0.9873

Score Mínimo: 0.3658

Score Médio: 0.7955

Desvio Padrão: 0.2279

# Interpretação dos Resultados de Cross-Validation — R² Score

Árvore de Decisão:

A Árvore de Decisão apresentou um score médio alto (0.7813), o que indica uma boa capacidade preditiva na média. No entanto, o desvio padrão de 0.1925 revela uma certa variabilidade entre os folds, o que significa que o desempenho do modelo pode oscilar dependendo do subconjunto de dados utilizado na validação. O score mínimo relativamente baixo (0.2898) reforça essa instabilidade em alguns cenários.

XGBoost:

O XGBoost demonstrou o melhor desempenho médio (0.7955) e também atingiu o maior score máximo (0.9873), evidenciando um potencial muito alto em alguns subconjuntos de dados. Contudo, o desvio padrão elevado (0.2279) e o score mínimo de 0.3658 indicam que, embora potente, o modelo pode ser sensível a variações nos dados, mostrando instabilidade em determinados casos.
