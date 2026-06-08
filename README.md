# mission-control-ai

Mission Control AI

Descrição do Projeto

O Mission Control AI é um sistema desenvolvido em Python para simular o monitoramento inteligente de uma missão espacial experimental.

O programa analisa diferentes ciclos da missão, verificando informações importantes como temperatura, comunicação, bateria, oxigênio e estabilidade operacional. A partir desses dados, o sistema calcula níveis de risco, gera alertas automáticos, identifica tendências da missão e produz um relatório final para auxiliar na tomada de decisões.

Este projeto foi desenvolvido para a disciplina de Pensamento Computacional e Automação com Python da FIAP.

---

Objetivo

Desenvolver um sistema capaz de:

Monitorar dados simulados de uma missão espacial;
Classificar situações como NORMAL, ATENÇÃO ou CRÍTICO;
Calcular o risco de cada ciclo;
Identificar a tendência da missão;
Detectar a área mais afetada durante a operação;
Gerar recomendações automáticas;
Exibir um relatório final completo.

---

Dados Monitorados

O sistema monitora as seguintes áreas:

1. Temperatura Interna
2. Comunicação com a Base
3. Sistema de Energia
4. Suporte de Oxigênio
5. Estabilidade Operacional

Cada ciclo da missão é representado pela estrutura:

[temperatura, comunicacao, bateria, oxigenio, estabilidade]

Exemplo:

[24, 92, 88, 96, 90]

---

Regras de Classificação

Temperatura

 Condição           Status  
 --------------  ------- 
 Menor que 18°C     ATENÇÃO 
 Entre 18°C e 30°C  NORMAL  
 Entre 31°C e 35°C  ATENÇÃO 
 Acima de 35°C      CRÍTICO 

Comunicação

 Condição          Status  
 ---------------  ------- 
 Menor que 30%    CRÍTICO 
 Entre 30% e 59%  ATENÇÃO 
 60% ou mais      NORMAL  

Bateria

 Condição         Status  
 ---------------  ------- 
 Menor que 20%    CRÍTICO 
 Entre 20% e 49%  ATENÇÃO 
 50% ou mais      NORMAL  

Oxigênio

 Condição         Status  
 ---------------  ------- 
 Menor que 80%    CRÍTICO 
 Entre 80% e 89%  ATENÇÃO 
 90% ou mais      NORMAL  

Estabilidade

 Condição         Status  
 ---------------  ------- 
 Menor que 40%    CRÍTICO 
 Entre 40% e 69%  ATENÇÃO 
 70% ou mais      NORMAL  

---

Pontuação de Risco

 Classificação  Pontos 
 -------------  ------ 
 NORMAL         0      
 ATENÇÃO        1      
 CRÍTICO        2      

Classificação final do ciclo:

 Pontuação  Resultado         
 ---------  ----------------- 
 0 a 2      MISSÃO ESTÁVEL    
 3 a 5      MISSÃO EM ATENÇÃO 
 6 a 10     MISSÃO CRÍTICA    

---

Funções Utilizadas

O projeto utiliza diversas funções para modularizar o código:

* analisar_temperatura()
* analisar_comunicacao()
* analisar_bateria()
* analisar_oxigenio()
* analisar_estabilidade()
* classificar_ciclo()
* analisar_tendencia()
* gerar_recomendacao()

---

Funcionalidades

Monitoramento de múltiplos ciclos

Cálculo automático de risco

Geração de alertas

Classificação da missão

Identificação da área mais afetada

Análise de tendência

Relatório final completo

---

Como Executar

1. Instale o Python 3.
2. Baixe o projeto.
3. Abra o terminal na pasta do projeto.
4. Execute:

python mission_control.py

---

Estrutura do Projeto

mission-control-ai/
 README.md
 mission_control.py

---

Integrantes

Nome Dos Alunos: 

Enzo De Nadai Vieira - RM: 569985
Leonardo Duarte - RM: 569029

---

Disciplina

Pensamento Computacional e Automação com Python

FIAP - Global Solution 2026

---

Conclusão

O Mission Control AI demonstra como conceitos de lógica de programação, estruturas de dados, funções e análise de informações podem ser utilizados para criar sistemas inteligentes de monitoramento. O projeto simula situações reais encontradas em missões espaciais, permitindo a identificação de riscos e auxiliando na tomada de decisões.

