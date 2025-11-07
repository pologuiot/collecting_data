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

# --- Initialisation de session_state ---
if "page" not in st.session_state:
    st.session_state.page = 1
if "composition" not in st.session_state:
    st.session_state.composition = {i: " " for i in range(1, 24)}

# --- Page 1 : sélection des joueurs ---
if st.session_state.page == 1:
    st.title("🏉 Composition d'équipe de Rugby")
    st.markdown("Sélectionne les **23 joueurs** de ton équipe :")

    # Création des 23 champs
    for i in range(1, 24):
        st.session_state.composition[i] = st.selectbox(
            f"n°{i}", joueurs,
            index=joueurs.index(st.session_state.composition[i]),
            key=f"joueur_{i}"
        )

    # Vérification que toutes les cases sont remplies
    all_filled = all(st.session_state.composition[i] != " " for i in range(1, 24))

    # Bouton pour passer à la page 2
    btn = st.button("Valider la composition", disabled=not all_filled)
    if btn:
        st.session_state.page = 2
        st.experimental_rerun()  # Cette fois, la rerun est OK car elle vient après la fin de la boucle principale

# --- Page 2 : message de fin ---
elif st.session_state.page == 2:
    st.title("✅ La compo est finie")
    st.markdown("Vous avez terminé la sélection des 23 joueurs.")
