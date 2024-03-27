from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

# Salvando o caminho dos dados
url = "segundoTrabalho\\trabalho_LOAN\\data-set\\arquivoKNN_normalizado.csv"

# Atribuindo nomes para as colunas para printar a tabela
names = ['Loan ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']

# Lê o dataset
df = pd.read_csv(url, names=names)

df.head()

X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

# Separa dados de testes e treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)

# Medida F
f1 = f1_score(y_test, y_pred, average='weighted')
print(f'Medida F: {f1}')

# Calculando matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Matriz de confusão: \n{conf_matrix}')