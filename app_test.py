import streamlit as st

st.set_page_config(page_title="Composition de Rugby", layout="wide")

# --- Liste des joueurs disponibles ---
joueurs = [
    "Dupont", "Ntamack", "Fickou", "Penaud", "Jalibert",
    "Alldritt", "Ollivon", "Jelonch", "Marchand", "Baille",
    "Atonio", "Flament", "Woki", "Ramos", "Danty"
]

st.title("🏉 Composition d'équipe de Rugby")

st.markdown("""
<style>
    .terrain {
        position: relative;
        width: 100%;
        height: 600px;
        background: linear-gradient(to right, #4CAF50 20%, #66BB6A 80%);
        border: 4px solid #388E3C;
        border-radius: 15px;
        margin-top: 20px;
    }
    .joueur-box {
        position: absolute;
        width: 8vw;      /* Longueur approximative (fixe) */
        height: 40px;    /* Hauteur fixe */
        background-color: white;
        border-radius: 8px;
        box-shadow: 0px 3px 6px rgba(0,0,0,0.3);
        padding: 4px;
        text-align: center;
    }
    label, .stSelectbox {
        font-size: 0.9rem !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Coordonnées (x,y) données ---
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

# --- Conversion coord -> position CSS ---
def coord_to_css(x, y, width=4, height=0.5):
    # Normalisation pour correspondre à la hauteur/largeur du terrain
    left = f"{x * 4.5}%"   # facteur pour adapter la largeur
    top = f"{(6.5 - y) * 13}%"  # inverser l’axe Y pour correspondre à ton repère
    return f"left:{left}; top:{top};"

# --- Affichage du terrain ---
st.markdown("<div class='terrain'>", unsafe_allow_html=True)

for i in range(1, 16):
    css_pos = coord_to_css(*positions[i])
    st.markdown(f"<div class='joueur-box' style='{css_pos}'>", unsafe_allow_html=True)
    joueur = st.selectbox(f"Joueur {i}", joueurs, key=f"joueur_{i}")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Résumé ---
st.markdown("---")
st.subheader("📋 Composition finale")
for i in range(1, 16):
    st.write(f"{i}. {st.session_state[f'joueur_{i}']}")
