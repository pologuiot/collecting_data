import streamlit as st

st.set_page_config(page_title="Composition de Rugby", layout="centered")

# --- Liste des joueurs disponibles ---
joueurs = [
    "Dupont", "Ntamack", "Fickou", "Penaud", "Jalibert",
    "Alldritt", "Ollivon", "Jelonch", "Marchand", "Baille",
    "Atonio", "Flament", "Woki", "Ramos", "Danty",
    "Lucu", "Bielle-Biarrey", "Moefana", "Boudehent",
    "Gabrillagues", "Colombe", "Le Garrec", "Villière"
]

st.title("🏉 Composition d'équipe de Rugby")
st.markdown("Sélectionne les **23 joueurs** de ton équipe :")

# --- Création des 23 champs ---
composition = {}
for i in range(1, 24):
    st.markdown(f"### n°{i}")
    composition[i] = st.selectbox(f"Choisis le joueur n°{i}", joueurs, key=f"joueur_{i}")

# --- Résumé final ---
st.markdown("---")
st.subheader("📋 Composition finale")
for i in range(1, 24):
    st.write(f"**n°{i}** → {composition[i]}")
