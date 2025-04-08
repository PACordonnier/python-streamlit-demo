#!/bin/bash

# Définir une valeur par défaut pour WORK_DIR si non défini
WORK_DIR=${WORK_DIR:-"python-streamlit-demo"}

# Tenter de se déplacer dans le dossier
if cd "$WORK_DIR"; then
  echo "Dans le dossier : $WORK_DIR"
else
  echo "Le dossier $WORK_DIR est introuvable ou inaccessible, poursuite du script..."
fi

pip install -r requirements.txt
