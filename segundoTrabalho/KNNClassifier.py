import numpy as np

class KNNClassifier:
    # K é o numero de visinhos proximos
    def __init__(self, k=3):
        self.k = k

    # O fit é o metodo usado para claassificar
    # Ele recebe os dados de treinamento (X_train) e os rótulos de classe correspondentes (y_train) como entrada e os armazena internamente no objeto do classificador.
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # Ele recebe os dados de teste (X_test) e retorna as previsões correspondentes.
    def predict(self, X_test):
        y_pred = [self._predict(x) for x in X_test]
        return np.array(y_pred)

    # Ele calcula a classe prevista para um único ponto de teste x.
    # Primeiro, calcula as distâncias entre x e todos os pontos de treinamento usando a distância euclidiana.
    # Em seguida, seleciona os k vizinhos mais próximos com base nas menores distâncias.
    # Conta a frequência das classes dos vizinhos mais próximos e retorna a classe mais comum.
    def _predict(self, x):
        distances = [np.sqrt(np.sum((x - x_train)**2)) for x_train in self.X_train] # calculo da distancia euclidiana.
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = np.argmax(np.bincount(k_nearest_labels))
        return most_common
