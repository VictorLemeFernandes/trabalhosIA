from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy
import matplotlib.pyplot as plt

# Salvando o caminho dos dados
url = "segundoTrabalho\\trabalho_LOAN\\data-set\\arquivoKNN_normalizado.csv"

# Atribuindo nomes para as colunas para printar a tabela
names = ['Loan ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']

# Lê o dataset
df = pd.read_csv(url, names=names)

todasAcuracias = []
todasMedidasF = []
todasMatrizesConfusao = []
acuraciasParaGrafico = []
medidasF_Grafico = []

def knn(k, colunasDrops):
    X = df.drop(colunasDrops, axis=1) # Remove a coluna 'Loan_Status' do dataframe
    y = df['Loan_Status'] # Armazena os dados da coluna 'Loan_Status' na variável y

    # Separa dados de testes e treino e coloca o tamanho do teste em 30%
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Faz a padronização dos dados de treinamento e teste
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Cria instância do classificador KNN com n_neighbors vizinhos e depois o treina com os dados de treinamento padronizados
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Previsões nos dados de teste
    y_pred = knn.predict(X_test)

    # Calculo da acurácia
    accuracy = accuracy_score(y_test, y_pred)
    todasAcuracias.append(accuracy)

    # Medida F
    f1 = f1_score(y_test, y_pred, average='weighted')
    todasMedidasF.append(f1)

    # Calculando matriz de confusão
    conf_matrix = confusion_matrix(y_test, y_pred)
    todasMatrizesConfusao.append(conf_matrix)


# Colunas/atributos que podem ser retirados da classificação
colunasDropadas = [
    ['Loan_Status'],
    ['Loan_Status', 'Gender', 'Married'],
    ['Loan_Status', 'Self_Employed', 'Education', 'Loan_Amount_Term', 'Credit_History'],
    ['Loan_Status', 'Property_Area', 'LoanAmount'],
    ['Loan_Status', 'Education'],
    ['Loan_Status', 'Gender', 'Self_Employed', 'Credit_History']
]

iteracoes = 500

for j in colunasDropadas:
    for i in range(0, iteracoes):
        knn(11, j) # knn(k = vizinhos, colunasDropadas)
    
    print(f'Retirando as seguintes colunas: {j}')
    print(f'Média da acurácia: {numpy.mean(todasAcuracias)}')
    print(f'Média da medida F: {numpy.mean(todasMedidasF)}')
    
    acuraciasParaGrafico.append(numpy.mean(todasAcuracias))
    medidasF_Grafico.append(numpy.mean(todasMedidasF))

    matrizAuxiliar = numpy.array(todasMatrizesConfusao) # Transforma a matriz em tridimensional p/ ser tratada no numpy
    print(f'Média das matrizes de confusão: \n{numpy.mean(matrizAuxiliar, axis=0)}')
    todasAcuracias = []
    todasMedidasF = []
    todasMatrizesConfusao = []
    print('\n')


# Variação da acurácia e da medida F ao longo das N iterações do algoritmo KNN
plt.figure(figsize=(10, 6))

# Plotando a variação da acurácia
plt.plot(range(1, len(acuraciasParaGrafico) + 1), acuraciasParaGrafico, label='Acurácia', color='blue')

# Plotando a variação da medida F
plt.plot(range(1, len(medidasF_Grafico) + 1), medidasF_Grafico, label='Medida F', color='green')

#legendas
plt.title('Variação da Acurácia e Medida F ao longo das iterações (qtde de testes de drop colunas)')
plt.xlabel('Iterações')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
