import streamlit as st

st.set_page_config(page_title="Composition de Rugby", layout="centered")

# Liste des joueurs disponibles
joueurs = [
    "Dupont", "Ntamack", "Fickou", "Penaud", "Jalibert",
    "Alldritt", "Ollivon", "Jelonch", "Marchand", "Baille",
    "Atonio", "Flament", "Woki", "Ramos", "Danty"
]

st.title("🏉 Composition d'équipe de Rugby")

st.markdown("### Sélectionne tes joueurs par poste :")

# --- Disposition en colonnes selon la composition classique ---
# Ligne 1 : première ligne (3 joueurs)
col1, col2, col3 = st.columns(3)
with col1:
    p1 = st.selectbox("Pilier gauche", joueurs, key="p1")
with col2:
    p2 = st.selectbox("Talonneur", joueurs, key="p2")
with col3:
    p3 = st.selectbox("Pilier droit", joueurs, key="p3")

# Ligne 2 : deuxième ligne (2 joueurs)
col4, col5 = st.columns(2)
with col4:
    p4 = st.selectbox("Deuxième ligne gauche", joueurs, key="p4")
with col5:
    p5 = st.selectbox("Deuxième ligne droite", joueurs, key="p5")

# Ligne 3 : troisième ligne (3 joueurs)
col6, col7, col8 = st.columns(3)
with col6:
    p6 = st.selectbox("Flanker gauche", joueurs, key="p6")
with col7:
    p7 = st.selectbox("Numéro 8", joueurs, key="p7")
with col8:
    p8 = st.selectbox("Flanker droit", joueurs, key="p8")

# Ligne 4 : charnière (2 joueurs)
col9, col10 = st.columns(2)
with col9:
    p9 = st.selectbox("Demi de mêlée", joueurs, key="p9")
with col10:
    p10 = st.selectbox("Demi d’ouverture", joueurs, key="p10")

# Ligne 5 : trois-quarts (4 joueurs)
col11, col12, col13, col14 = st.columns(4)
with col11:
    p11 = st.selectbox("Ailier gauche", joueurs, key="p11")
with col12:
    p12 = st.selectbox("Centre intérieur", joueurs, key="p12")
with col13:
    p13 = st.selectbox("Centre extérieur", joueurs, key="p13")
with col14:
    p14 = st.selectbox("Ailier droit", joueurs, key="p14")

# Ligne 6 : arrière (1 joueur)
p15 = st.selectbox("Arrière", joueurs, key="p15")

# --- Affichage de la composition ---
st.markdown("---")
st.header("🏉 Composition finale")

composition = [
    (1, p1), (2, p2), (3, p3),
    (4, p4), (5, p5),
    (6, p6), (7, p7), (8, p8),
    (9, p9), (10, p10),
    (11, p11), (12, p12), (13, p13), (14, p14), (15, p15)
]

for num, joueur in composition:
    st.write(f"**{num}.** {joueur}")
