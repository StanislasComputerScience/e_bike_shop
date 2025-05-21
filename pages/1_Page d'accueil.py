import streamlit as st
import pandas as pd

st.title("📥 Importation et Préparation des Données")

# Charger un fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file:
    # Lire le fichier CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    st.subheader("Statistiques descriptives")
    st.write(df.describe())

    st.subheader("Colonnes du dataset")
    st.write(df.columns.tolist())

    # Nettoyage simple : supprimer les valeurs manquantes
    if st.checkbox("Supprimer les lignes contenant des valeurs manquantes"):
        df_cleaned = df.dropna()
        st.write("Nombre de lignes après suppression :", len(df_cleaned))
        st.dataframe(df_cleaned.head())

    # Mémoire pour les autres pages
    st.session_state.df = df
else:
    st.info("Veuillez importer un fichier CSV pour commencer.")
