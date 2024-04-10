import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

path = "terceiroTrabalho\\Mall_Customers.csv"

# Carregando o DataSet
df = pd.read_csv(path)

# Padronizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(
    df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])

# Definindo a faixa de valores de k que serão testados
k_values = range(2, 11)

# Lista para armazenar os scores de silhueta para cada valor de k
silhouette_scores = []

# Testando diferentes valores de k
for k in k_values:
    # Treinando o modelo K-Means
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)

    # Calculando o score de silhueta
    silhouette_avg = silhouette_score(df_scaled, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)

# Plotando o gráfico
plt.plot(k_values, silhouette_scores, marker='o')
plt.title('Variação do Score de Silhueta em função de k')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Score de Silhueta')
plt.xticks(k_values)
plt.grid(True)

# Salvando o gráfico como PNG
plt.savefig('terceiroTrabalho\\score_silhueta.png')

# Encontrando o melhor valor de k com base no score de silhueta
best_k = k_values[np.argmax(silhouette_scores)]

# Treinando o modelo K-Means com o melhor valor de k
best_kmeans = KMeans(n_clusters=best_k, random_state=42)
best_kmeans.fit(df_scaled)

df['Cluster'] = best_kmeans.labels_

# Adicionando as labels dos clusters ao DataFrame original
df['Cluster'] = best_kmeans.labels_

# Visualizando os clusters
plt.figure(figsize=(10, 6))

# Plotando os pontos para cada cluster
for cluster in range(best_k):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['Annual Income (k$)'], cluster_data['Spending Score (1-100)'],
                label=f'Cluster {cluster}', alpha=0.7)

# Plotando os centroides
centroids = scaler.inverse_transform(best_kmeans.cluster_centers_)
plt.scatter(centroids[:, 1], centroids[:, 2], marker='x',
            s=200, c='red', label='Centroides')

plt.title(f'Clusters com k = {best_k}')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)

# Salvando o melhor cluster como PNG
plt.savefig('terceiroTrabalho\\best_Cluster.png')
