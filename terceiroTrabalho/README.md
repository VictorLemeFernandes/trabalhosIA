# README: Análise de Clusters com K-Means

Este código realiza uma análise de clusters em um conjunto de dados de clientes de um shopping center utilizando o algoritmo de K-Means. Ele busca identificar grupos de clientes com base em características como idade, renda anual e pontuação de gastos.

## Passos Realizados no Código:

1. **Carregamento dos Dados:** O conjunto de dados é carregado a partir de um arquivo CSV ("Mall_Customers.csv").

2. **Padronização dos Dados:** As características relevantes para a análise (idade, renda anual e pontuação de gastos) são padronizadas para terem média zero e desvio padrão 1.

3. **Seleção do Valor de k:** Diferentes valores de k (número de clusters) são testados para determinar o número ideal de clusters. Os valores testados variam de 2 a 10.

4. **Treinamento do Modelo K-Means:** Para cada valor de k, o modelo K-Means é treinado usando os dados padronizados.

5. **Cálculo do Score de Silhueta:** O score de silhueta é calculado para cada modelo K-Means como uma métrica de avaliação da qualidade dos clusters formados.

6. **Seleção do Melhor Valor de k:** O valor de k que maximiza o score de silhueta é escolhido como o melhor valor.

7. **Treinamento do Melhor Modelo K-Means:** O modelo K-Means é treinado novamente usando o melhor valor de k.

8. **Visualização dos Clusters:** Os clusters são visualizados em um gráfico bidimensional com a renda anual no eixo x e a pontuação de gastos no eixo y. Cada cluster é representado por pontos de dados, enquanto os centroides de cada cluster são marcados com um 'x' vermelho.

9. **Salvamento das Visualizações:** Duas visualizações são salvas como arquivos PNG: uma mostrando a variação do score de silhueta em função de k e outra mostrando os clusters com o melhor valor de k.
