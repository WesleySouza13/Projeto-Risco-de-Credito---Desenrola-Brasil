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




