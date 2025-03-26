# Projeto: Análise de Fatores que Influenciam os Preços de Imóveis

Este projeto utiliza o dataset "House Prices - São Paulo" do Kaggle para identificar e analisar os fatores que influenciam os preços dos imóveis na cidade de São Paulo. O objetivo é aplicar técnicas de pré-processamento, análise exploratória, modelagem preditiva e avaliação para construir um modelo que explique e preveja os preços dos imóveis.

## Objetivo

- Identificar os fatores mais relevantes que influenciam os preços dos imóveis.
- Construir modelos preditivos para prever os preços com base nas variáveis disponíveis.
- Avaliar o desempenho dos modelos e interpretar os resultados.

## Dataset

O dataset contém informações detalhadas sobre imóveis em São Paulo, incluindo:
- **logradouro**: Nome da rua.
- **bairro**: Bairro do imóvel.
- **cidade**: Cidade (São Paulo).
- **tipo_imovel**: Tipo do imóvel (casa, apartamento, comercial, etc.).
- **area_util**: Área útil do imóvel (m²).
- **banheiros**: Número de banheiros.
- **suites**: Número de suítes.
- **quartos**: Número de quartos.
- **vagas_garagem**: Número de vagas de garagem.
- **preco_venda**: Preço de venda do imóvel (variável alvo).
- **taxa_condominio**: Valor do condomínio (se aplicável).
- **preco_aluguel**: Preço de aluguel (se aplicável).
- **iptu_ano**: Valor do IPTU anual.

## Etapas do Projeto

1. **Exploração e Pré-processamento dos Dados**:
   - Análise descritiva e visualização inicial dos dados.
   - Tratamento de valores ausentes e remoção de outliers.
   - Seleção de variáveis relevantes para a modelagem.

2. **Análise Exploratória**:
   - Análise de correlação entre as variáveis.
   - Visualização de distribuições e relações entre as variáveis.

3. **Divisão dos Dados**:
   - Separação dos dados em conjuntos de treino (80%) e teste (20%).

4. **Modelagem Preditiva**:
   - **Regressão Linear**: Modelo base para estabelecer um benchmark.
   - **Random Forest**: Modelo para capturar relações não lineares.
   - **Gradient Boosting**: Modelo avançado para melhorar a performance.

5. **Avaliação dos Modelos**:
   - Métricas utilizadas:
     - **MSE (Mean Squared Error)**: Erro médio ao quadrado.
     - **RMSE (Root Mean Squared Error)**: Raiz quadrada do MSE.
     - **R² (Coeficiente de Determinação)**: Proporção da variância explicada pelo modelo.
   - Validação cruzada para garantir a robustez dos resultados.

6. **Conclusões e Recomendações**:
   - Interpretação dos resultados e insights sobre o mercado imobiliário.
   - Recomendações para melhorias futuras, como ajuste de hiperparâmetros e engenharia de features.

## Resultados

- **Regressão Linear**:
  - R² no conjunto de teste: ~0,045.
  - Modelo base com desempenho limitado, indicando relações não lineares entre as variáveis.

- **Random Forest**:
  - R² no conjunto de teste: ~0,76.
  - Capturou melhor as relações não lineares, mostrando robustez.

- **Gradient Boosting**:
  - R² no conjunto de teste: ~0,80.
  - Melhor modelo, explicando ~80% da variância dos preços.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas` e `numpy` para manipulação de dados.
  - `matplotlib` e `seaborn` para visualização de dados.
  - `scikit-learn` para modelagem e avaliação.
  - `statsmodels` para análise estatística.

## Como Executar o Projeto

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/SEU_USUARIO/House_Prices.git
   cd House_Prices

   2. Clone o repositório para o seu ambiente local:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Instale as dependências:
   ```bash
   jupyter notebook House_Prices.ipynb

## Conclusões
O projeto demonstrou que modelos baseados em árvores, como Random Forest e Gradient Boosting, são mais eficazes para prever preços de imóveis devido à sua capacidade de capturar relações não lineares.
A regressão linear, embora simples, não foi suficiente para explicar a complexidade do problema.
O Gradient Boosting foi o modelo com melhor desempenho, alcançando um R² de ~0,80 no conjunto de teste.

## Recomendações Finais
Engenharia de Features: Criar novas variáveis ou transformar as existentes pode melhorar os resultados.
Ajuste de Hiperparâmetros: Utilizar técnicas como GridSearchCV para otimizar os modelos.
Interpretação dos Modelos: Analisar a importância das variáveis para fornecer insights estratégicos.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Referências
Kaggle - House Prices - São Paulo
