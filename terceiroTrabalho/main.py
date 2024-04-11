import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Caminho para o arquivo CSV
path = "terceiroTrabalho/Mall_Customers.csv"

# Carregando o DataSet
df = pd.read_csv(path)
# Nomes das colunas relevantes para o clustering
names = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

# Padronizando os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[names])

# Definindo a faixa de valores de k que serão testados
k_values = range(2, 11)

# Lista para armazenar os scores de silhueta para cada valor de k
silhouette_scores = []

# Lista para armazenar os valores SSE (Sum of Squared Errors) para cada valor de k
sse_values = []

# Loop sobre diferentes valores de k
for k in k_values:
    # Inicializando o modelo K-Means com o número de clusters (k) e random_state definido como 42
    kmeans = KMeans(n_clusters=k, random_state=42)
    
    # Treinando o modelo K-Means nos dados padronizados
    kmeans.fit(df_scaled)

    # Calculando o score de silhueta para avaliar a qualidade da clusterização
    silhouette_avg = silhouette_score(df_scaled, kmeans.labels_)
    
    # Adicionando o score de silhueta à lista de scores de silhueta
    silhouette_scores.append(silhouette_avg)

    # Calculando o SSE (Sum of Squared Errors) para avaliar a compactação dos clusters
    sse_values.append(kmeans.inertia_)


# Plotando o gráfico com o score de silhueta
plt.plot(k_values, silhouette_scores, marker='o')
plt.title('Variação do Score de Silhueta em função de k')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Score de Silhueta')
plt.xticks(k_values)
plt.grid(True)

# Salvando o gráfico como PNG
plt.savefig('terceiroTrabalho/score_silhueta.png')
plt.clf()

# Plotando o gráfico com relação ao SSE
print(f'O melhor SSE: {min(sse_values)}')
plt.plot(k_values, sse_values, marker='o')
plt.title('Variação do SSE em função de k')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('SSE')
plt.xticks(k_values)
plt.grid(True)

# Salvando o gráfico como PNG
plt.savefig('terceiroTrabalho/sse_Values.png')
plt.clf()

# Encontrando o melhor valor de k com base no score de silhueta
print(f'A melhor silhueta: {max(silhouette_scores)}')
best_k = k_values[np.argmax(silhouette_scores)]
print(f'O melhor valor de K é: {best_k}')

# Treinando o modelo K-Means com o melhor valor de k
best_kmeans = KMeans(n_clusters=best_k, random_state=42)
best_kmeans.fit(df_scaled)

# Adicionando as labels dos clusters ao DataFrame original
df['Cluster'] = best_kmeans.labels_

# Visualizando os clusters
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotando os pontos para cada cluster
for cluster in range(best_k):
    cluster_data = df[df['Cluster'] == cluster]
    ax.scatter(cluster_data['Annual Income (k$)'], cluster_data['Spending Score (1-100)'],
               cluster_data['Age'], label=f'Cluster {cluster}', alpha=0.7)
    
# Plotando os centroides
centroids = scaler.inverse_transform(best_kmeans.cluster_centers_)
ax.scatter(centroids[:, 1], centroids[:, 2], centroids[:, 0], marker='x',
           s=200, c='red', label='Centroides')

ax.set_title(f'Clusters com k = {best_k}')
ax.set_xlabel('Annual Income (k$)')
ax.set_ylabel('Spending Score (1-100)')
ax.set_zlabel('Age')
ax.legend()
ax.grid(True)

# Salvando o gráfico 3D como PNG
plt.savefig('terceiroTrabalho/best_Cluster_3D.png')
plt.clf()

# # Visualizando os clusters
# plt.figure(figsize=(10, 6))

# # Plotando os pontos para cada cluster
# for cluster in range(best_k):
#     cluster_data = df[df['Cluster'] == cluster]
#     plt.scatter(cluster_data['Annual Income (k$)'], cluster_data['Spending Score (1-100)'],
#                 label=f'Cluster {cluster}', alpha=0.7)

# # Plotando os centroides
# centroids = scaler.inverse_transform(best_kmeans.cluster_centers_)
# plt.scatter(centroids[:, 1], centroids[:, 2], marker='x',
#             s=200, c='red', label='Centroides')

# plt.title(f'Clusters com k = {best_k}')
# plt.xlabel('Annual Income (k$)')
# plt.ylabel('Spending Score (1-100)')
# plt.legend()
# plt.grid(True)

# # Salvando o melhor cluster como PNG
# plt.savefig('terceiroTrabalho/best_Cluster.png')
# plt.clf()