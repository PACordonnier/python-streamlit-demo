import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
iris = sns.load_dataset("iris")

# Titre
st.title("Explorateur d'iris 🌸")

# Sélecteur d'espèce
species = st.selectbox("Choisissez une espèce :", iris['species'].unique())

# Filtrer les données
filtered_data = iris[iris['species'] == species]

# Afficher les données
st.write(f"Voici les données pour l'espèce : **{species}**")
st.dataframe(filtered_data)

# Graphe
fig, ax = plt.subplots()
ax.scatter(filtered_data['sepal_length'], filtered_data['petal_length'], color='green')
ax.set_xlabel("Longueur des sépales")
ax.set_ylabel("Longueur des pétales")
ax.set_title(f"Sépales vs Pétales - {species}")

# Afficher le graphe
st.pyplot(fig)
