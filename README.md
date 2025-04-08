# 🌸 Explorateur d'Iris avec Streamlit

Une application web simple en Python (avec Streamlit) pour visualiser et filtrer le célèbre jeu de données `iris`.  

---

## Dépendances

La liste des dépendances est indiquée dans le fichier `requirements.txt`.

Installation des dépendances:

```
pip install -r requirements.txt
```

## Exécution

Pour exécuter cette application, deux possibilités

```
streamlit run app.py --server.port 5800 --server.address 0.0.0.0
# Ou utiliser le script déjà écrit
./start_streamlit.sh
```

## Utilisation avec Onyxia

Un fichier d'init est présent dans le repository. Celui-ci télécharge les dépendances de requirement.txt pour avoir un environnement prêt à l'emploi immédiatement.

Afin d'accéder au serveur ouvert par streamlit, il est nécessaire d'ouvrir dans la configuration via la configuration du service. Dans la configuration de l'instance vscode sélectionnez "Networking detail" -> "Enable a custom service port" -> Définir le port 5800 comme étant ouvert.

Au démarrage de l'instance par onyxia, un lien pour accéder au port 5800 du conteneur sera fourni. Le lien fonctionnera dès que le serveur streamlit sera démarré.

Pour exécuter la ligne de commandes streamlit, dans vscode server sélectionner le menu déroulant (en haut à gauche) -> Terminal -> New terminal.

Puis lancer `./start_streamlit.sh`
