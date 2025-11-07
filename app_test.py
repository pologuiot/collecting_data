import streamlit as st

st.set_page_config(page_title="Composition de Rugby", layout="wide")

# --- Liste des joueurs disponibles ---
joueurs = [
    "Dupont", "Ntamack", "Fickou", "Penaud", "Jalibert",
    "Alldritt", "Ollivon", "Jelonch", "Marchand", "Baille",
    "Atonio", "Flament", "Woki", "Ramos", "Danty"
]

st.title("🏉 Composition d'équipe de Rugby")

# --- Styles CSS (sans fond vert) ---
st.markdown("""
<style>
    .terrain {
        position: relative;
        width: 100%;
        height: 600px;
        background: transparent;
        margin-top: 20px;
    }
    .joueur-box {
        position: absolute;
        width: 8vw;       /* largeur fixe */
        height: 50px;     /* hauteur fixe */
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
        padding: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stSelectbox {
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Coordonnées (x, y) données ---
positions = {
    1: (3, 5.5),
    2: (9, 5.5),
    3: (15, 5.5),
    4: (6, 4.5),
    5: (12, 4.5),
    6: (3, 3.5),
    7: (15, 3.5),
    8: (9, 3.5),
    9: (4, 2.5),
    10: (14, 2.5),
    11: (0, 1.5),
    12: (6, 1.5),
    13: (12, 1.5),
    14: (18, 1.5),
    15: (9, 0.5)
}

# --- Conversion coordonnées → position CSS ---
def coord_to_css(x, y):
    left = f"{x * 4.5}%"         # étalement horizontal
    top = f"{(6.5 - y) * 13}%"   # inversion verticale pour ton repère
    return f"left:{left}; top:{top};"

# --- Conteneur principal ---
st.markdown("<div class='terrain'>", unsafe_allow_html=True)

# Création des 15 encadrés
for i in range(1, 16):
    css_pos = coord_to_css(*positions[i])
    st.markdown(f"<div class='joueur-box' style='{css_pos}'>", unsafe_allow_html=True)
    st.selectbox(f"Poste {i}", joueurs, key=f"joueur_{i}", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Résumé final ---
st.markdown("---")
st.subheader("📋 Composition finale")
for i in range(1, 16):
    st.write(f"{i}. {st.session_state[f'joueur_{i}']}")
