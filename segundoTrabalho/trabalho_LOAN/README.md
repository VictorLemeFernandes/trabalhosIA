# Loan Rejection or Approval
Utilizando KNN para classificar o status de um empréstimo.
-

# Problemas enfrentados
Durante o desenvolvimento e manuseio do dataset enfrentamos alguns **problemas**:
- Dados em strings que o algoritmo da biblioteca ```sklearn``` não aceitava;
- Dados NaN que a biblioteca também não aceitava;
- Dois valores sem sentido que alteramos sem afetar a originalidade do código.

Vamos começar citando os **valores que eram strings e tivemos que transformar em números** para o algoritmo funcionar.

Nas seguintes colunas fizemos as seguintes alterações:
- Gender
  - Male = 0
  - Female = 1
- Married
  - Yes = 1
  - No = 0
- Education
  - Graduate = 1
  - Not-Graduate = 0
- Self-Employed
  - Yes = 1
  - No = 0
- Property Area
  - Urban = 0
  - Semi-urban = 1
  - Rural = 2
- Loan Status
  - Yes = 1
  - No = 2
  
Também tivemos dois valores na coluna ```CoapplicantIncome``` que o algoritmo não conseguiu reconhecer como números, são eles:
- 9.857.999.877.999.990
- 1.612.000.084

Para solucionar esse problema, **tivemos que tirar os pontos e adicionar um .0 no final**, ficando:
- 9857999877999990.0
- 1612000084.0

Por fim, **outro problema que tivemos foi com dados NaN**, que basicamente eram espaços vazios no arquivo .csv, infelizmente tivemos que remover esses registros pois não conseguimos encontrar uma solução para fazer a classificação com eles.

#

# O código
A implementação foi relativamente simples, criamos a função ```knn(k, colunasDrops)``` como a função que vai fazer o necessário para o algoritmo.

Dentro dessa função começamos removendo a coluna ```'Loan_Status'``` (queé a que utilizaremos para classificação) e outros atributos, podendo ser estabelicidos dentro do array ```colunasDropadas```. Fizemos todas as funções necessárias para a implementação do algoritmo:
- ```train_test_split()```
  - Separa os dados em treino e testes;
  - Separamos o conjunto de teste em 30%.
- ```fit_transform()``` e ```transform()```
  - Fazem a padronização dos dados de teste e treino
- Instanciamos um objeto do tipo ```KNeighborsClassifier``` da seguinte forma:
```python
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
```
- ```predict()```
  - Objetivo é estabelecer as previsões do conjunto de testes
- ```accuracy_score()```
  - Basicamente efetua o cálculo da acurácia
- ```f1_score()```
  - Faz o cálculo da medida F
- ```confusion_matrix()```
  - Retorna a matriz de confusão

Por fim, há dois loops ```for``` que executam o KNN inúmeras vezes para podermos ter vários valores para que uma média precisa seja calculada. Logo em seguida, há a plotagem do gráfico utilizando a biblioteca ```pyplot```.


# Executando
Para executar o código basta baixar todas os módulos necessários e executar como qualquer outro arquivo Python:
- sci-learn
- matplotlib
- numpy
- pandas