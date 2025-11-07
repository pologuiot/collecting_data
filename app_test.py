import streamlit as st

st.set_page_config(page_title="Composition de Rugby", layout="centered")

# --- Liste des joueurs ---
joueurs = [" "] + [
    "Dupont", "Ntamack", "Fickou", "Penaud", "Jalibert",
    "Alldritt", "Ollivon", "Jelonch", "Marchand", "Baille",
    "Atonio", "Flament", "Woki", "Ramos", "Danty",
    "Lucu", "Bielle-Biarrey", "Moefana", "Boudehent",
    "Gabrillagues", "Colombe", "Le Garrec", "Villière"
]

# --- Gestion de la "page" ---
if "page" not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:

    st.title("🏉 Composition d'équipe de Rugby")
    st.markdown("Sélectionne les **23 joueurs** de ton équipe :")

    # --- Création des 23 champs ---
    if "composition" not in st.session_state:
        st.session_state.composition = {i: " " for i in range(1, 24)}

    for i in range(1, 24):
        st.session_state.composition[i] = st.selectbox(
            f"n°{i}", joueurs, index=joueurs.index(st.session_state.composition[i]), key=f"joueur_{i}"
        )

    # --- Vérifier si toutes les cases sont remplies ---
    all_filled = all(st.session_state.composition[i] != " " for i in range(1, 24))

    # --- Bouton pour passer à la page 2 ---
    if st.button("Valider la composition", disabled=not all_filled):
        st.session_state.page = 2
        st.experimental_rerun()

elif st.session_state.page == 2:
    st.title("✅ La compo est finie")
    st.markdown("Vous avez terminé la sélection des 23 joueurs.")
