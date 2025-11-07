# import streamlit as st
# import pandas as pd
# from io import BytesIO

# st.set_page_config(page_title="Composition de Rugby", layout="wide")

# # --- Nombre de joueurs ---
# nbr_joueur = 4

# # --- Liste des joueurs ---
# joueurs = [" "] + [
#     "Dupont", "Ntamack", "Fickou", "Penaud", "Jalibert",
#     "Alldritt", "Ollivon", "Jelonch", "Marchand", "Baille",
#     "Atonio", "Flament", "Woki", "Ramos", "Danty",
#     "Lucu", "Bielle-Biarrey", "Moefana", "Boudehent",
#     "Gabrillagues", "Colombe", "Le Garrec", "Villière"
# ]

# # --- Initialisation session_state ---
# if "page" not in st.session_state:
#     st.session_state.page = 1
# if "composition" not in st.session_state:
#     st.session_state.composition = {i: " " for i in range(1, nbr_joueur)}
# if "joueur_validated" not in st.session_state:
#     st.session_state.joueur_validated = {i: False for i in range(1, nbr_joueur)}
# if "joueur_phrase" not in st.session_state:
#     st.session_state.joueur_phrase = {i: "" for i in range(1, nbr_joueur)}
# if "current_joueur" not in st.session_state:
#     st.session_state.current_joueur = None
# if "check_joueur" not in st.session_state:
#     st.session_state.check_joueur = {i: False for i in range(1, nbr_joueur)}  # ✅ nouvelle variable

# # --- PAGE 1 : sélection des joueurs ---
# if st.session_state.page == 1:
#     st.title("🏉 Composition d'équipe de Rugby")
#     st.markdown(f"Sélectionne les **{nbr_joueur-1} joueurs** de ton équipe :")

#     for i in range(1, nbr_joueur):
#         st.session_state.composition[i] = st.selectbox(
#             f"n°{i}", joueurs,
#             index=joueurs.index(st.session_state.composition[i]),
#             key=f"joueur_{i}"
#         )

#     all_filled = all(st.session_state.composition[i] != " " for i in range(1, nbr_joueur))
#     if st.button("Valider la composition", disabled=not all_filled):
#         st.session_state.page = 2

# # --- PAGE 2 : récap + boutons joueurs + export Excel ---
# elif st.session_state.page == 2:
#     st.title("✅ La compo est finie")
#     st.subheader("📋 Composition finale")

#     ## Affichage composition
#     # for i in range(1, nbr_joueur):
#     #     st.write(f"n°{i} → {st.session_state.composition[i]}")

#     # st.markdown("---")
#     st.subheader("🔴 Joueurs : cliquer pour sélectionner phrase")

#     # Création des boutons colorés avec ✅ si check_joueur True
#     cols = st.columns(4)
#     for i in range(1, nbr_joueur):
#         col = cols[(i - 1) % 4]
#         checked = " ✅" if st.session_state.check_joueur[i] else ""
#         color = "background-color: green; color: white;" if st.session_state.joueur_validated[i] else "background-color: red; color: white;"
#         if col.button(f"n°{i} : {st.session_state.composition[i]}{checked}", key=f"btn_{i}"):
#             st.session_state.current_joueur = i
#             st.session_state.page = 3

#     # Bouton pour générer Excel
#     if all(st.session_state.joueur_validated[i] for i in range(1, nbr_joueur)):
#         st.markdown("---")
#         st.subheader("📥 Exporter la composition finale en Excel")

#         # Préparation du DataFrame
#         data = {
#             "Numéro": [i for i in range(1, nbr_joueur)],
#             "Nom": [st.session_state.composition[i] for i in range(1, nbr_joueur)],
#             "Choix": [st.session_state.joueur_phrase[i] for i in range(1, nbr_joueur)]
#         }
#         df = pd.DataFrame(data)

#         # Convertir en Excel en mémoire
#         output = BytesIO()
#         with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#             df.to_excel(writer, index=False, sheet_name="Composition")
#         excel_data = output.getvalue()

#         st.download_button(
#             label="Télécharger Excel",
#             data=excel_data,
#             file_name="composition.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )

# # --- PAGE 3 : page joueur individuel ---
# elif st.session_state.page == 3:
#     idx = st.session_state.current_joueur
#     nom_joueur = st.session_state.composition[idx]
#     st.title(f"🧑 Joueur : {nom_joueur}")

#     st.markdown("Choisis une phrase :")
#     choix = st.radio(
#         "Phrase",
#         ["nike", "adidas"],
#         index=0 if st.session_state.joueur_phrase[idx]=="" else ["nike", "adidas"].index(st.session_state.joueur_phrase[idx])
#     )

#     if st.button("Valider la phrase"):
#         st.session_state.joueur_phrase[idx] = choix
#         st.session_state.joueur_validated[idx] = True
#         st.session_state.check_joueur[idx] = True  # ✅ coche le joueur
#         st.session_state.page = 2


import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Composition de Rugby", layout="wide")

# --- Nombre de joueurs ---
nbr_joueur = 24

# --- Liste des joueurs ---
joueurs = [" "] + [
    "Dupont", "Ntamack", "Fickou", "Penaud", "Jalibert",
    "Alldritt", "Ollivon", "Jelonch", "Marchand", "Baille",
    "Atonio", "Flament", "Woki", "Ramos", "Danty",
    "Lucu", "Bielle-Biarrey", "Moefana", "Boudehent",
    "Gabrillagues", "Colombe", "Le Garrec", "Villière"
]

# --- Initialisation session_state ---
if "page" not in st.session_state:
    st.session_state.page = 1
if "composition" not in st.session_state:
    st.session_state.composition = {i: " " for i in range(1, nbr_joueur)}
if "joueur_validated" not in st.session_state:
    st.session_state.joueur_validated = {i: False for i in range(1, nbr_joueur)}
if "joueur_phrase" not in st.session_state:
    st.session_state.joueur_phrase = {i: "" for i in range(1, nbr_joueur)}
if "current_joueur" not in st.session_state:
    st.session_state.current_joueur = None
if "check_joueur" not in st.session_state:
    st.session_state.check_joueur = {i: False for i in range(1, nbr_joueur)}  # ✅ nouvelle variable

# --- PAGE 1 : sélection des joueurs ---
if st.session_state.page == 1:
    st.title("🏉 Composition d'équipe de Rugby")
    st.markdown(f"Sélectionne les **{nbr_joueur-1} joueurs** de ton équipe :")

    for i in range(1, nbr_joueur):
        st.session_state.composition[i] = st.selectbox(
            f"n°{i}", joueurs,
            index=joueurs.index(st.session_state.composition[i]),
            key=f"joueur_{i}"
        )

    all_filled = all(st.session_state.composition[i] != " " for i in range(1, nbr_joueur))
    if st.button("Valider la composition", disabled=not all_filled):
        st.session_state.page = 2

# --- PAGE 2 : récap + boutons joueurs + export Excel ---
elif st.session_state.page == 2:
    st.title("✅ La compo est finie")
    st.subheader("📋 Composition finale")

    # Affichage composition
    for i in range(1, nbr_joueur):
        st.write(f"n°{i} → {st.session_state.composition[i]}")

    st.markdown("---")
    st.subheader("🔴 Joueurs : cliquer pour sélectionner phrase")

    # Création des boutons colorés avec ✅ si check_joueur True
    cols = st.columns(4)
    for i in range(1, nbr_joueur):
        col = cols[(i - 1) % 4]
        checked = " ✅" if st.session_state.check_joueur[i] else ""
        color = "background-color: green; color: white;" if st.session_state.joueur_validated[i] else "background-color: red; color: white;"
        if col.button(f"n°{i} : {st.session_state.composition[i]}{checked}", key=f"btn_{i}"):
            st.session_state.current_joueur = i  # stocke l'index du joueur cliqué

    # Navigation vers page 3 si un joueur a été cliqué
    if st.session_state.current_joueur is not None:
        st.session_state.page = 3

    # Bouton pour générer Excel
    if all(st.session_state.joueur_validated[i] for i in range(1, nbr_joueur)):
        st.markdown("---")
        st.subheader("📥 Exporter la composition finale en Excel")

        # Préparation du DataFrame
        data = {
            "Numéro": [i for i in range(1, nbr_joueur)],
            "Nom": [st.session_state.composition[i] for i in range(1, nbr_joueur)],
            "Choix": [st.session_state.joueur_phrase[i] for i in range(1, nbr_joueur)]
        }
        df = pd.DataFrame(data)

        # Convertir en Excel en mémoire
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Composition")
        excel_data = output.getvalue()

        st.download_button(
            label="Télécharger Excel",
            data=excel_data,
            file_name="composition.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

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
        st.session_state.check_joueur[idx] = True  # coche le joueur
        st.session_state.current_joueur = None
        st.session_state.page = 2  # retourne à la page 2
