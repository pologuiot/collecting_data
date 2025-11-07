import streamlit as st

st.set_page_config(page_title="Composition de Rugby", layout="wide")

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
if "joueur_validated" not in st.session_state:
    st.session_state.joueur_validated = {i: False for i in range(1, 24)}
if "joueur_phrase" not in st.session_state:
    st.session_state.joueur_phrase = {i: "" for i in range(1, 24)}
if "current_joueur" not in st.session_state:
    st.session_state.current_joueur = None

# --- PAGE 1 : sélection des joueurs ---
if st.session_state.page == 1:
    st.title("🏉 Composition d'équipe de Rugby")
    st.markdown("Sélectionne les **23 joueurs** de ton équipe :")

    for i in range(1, 24):
        st.session_state.composition[i] = st.selectbox(
            f"n°{i}", joueurs,
            index=joueurs.index(st.session_state.composition[i]),
            key=f"joueur_{i}"
        )

    all_filled = all(st.session_state.composition[i] != " " for i in range(1, 24))

    if st.button("Valider la composition", disabled=not all_filled):
        st.session_state.page = 2

# --- PAGE 2 : récap + boutons joueurs ---
elif st.session_state.page == 2:
    st.title("✅ La compo est finie")
    st.subheader("📋 Composition finale")

    for i in range(1, 24):
        st.write(f"n°{i} → {st.session_state.composition[i]}")

    st.markdown("---")
    st.subheader("🔴 Joueurs : cliquer pour sélectionner phrase")

    cols = st.columns(4)
    for i in range(1, 24):
        col = cols[(i - 1) % 4]
        color = "green" if st.session_state.joueur_validated[i] else "red"
        if col.button(f"n°{i} : {st.session_state.composition[i]}", key=f"btn_{i}", help="Cliquer pour entrer dans page joueur", use_container_width=True):
            st.session_state.current_joueur = i
            st.session_state.page = 3

# --- PAGE 3 : page joueur individuel ---
elif st.session_state.page == 3:
    idx = st.session_state.current_joueur
    nom_joueur = st.session_state.composition[idx]
    st.title(f"🧑 Joueur : {nom_joueur}")

    st.markdown("Choisis une phrase :")
    choix = st.radio(
        "Phrase",
        ["nike", "adidas"],
        index=0 if st.session_state.joueur_phrase[idx]=="" else ["nike", "adidas"].index(st.session_state.joueur_phrase[idx])
    )

    if st.button("Valider la phrase"):
        st.session_state.joueur_phrase[idx] = choix
        st.session_state.joueur_validated[idx] = True
        st.session_state.page = 2
