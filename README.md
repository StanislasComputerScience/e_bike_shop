
# 🚴‍♂️ eBike_Shop – Application Streamlit pour boutique de vélos

par Rémi Labonne, Augustin Dendievel & César Gatano

---

Bonjour 👋,

Bienvenu dans le fichier README du projet **e_bike_shop**, une application Streamlit connectée à une base de données relationnelles gérée avec la technologie sqlite3 sous Python dédiée à la gestion d'une boutique en ligne de vélos. Ce document vous guidera à travers les fonctionnalités de l'application et les étapes nécessaires pour commencer à la tester.

<img src="./assets/logo/python.png" height="50"/>
<img src="./assets/logo/sqlite.png" height="50"/>
<img src="./assets/logo/streamlit.png" height="50"/>

---

## 🚴‍♂️ Présentation de l'application

**e_bike_shop** est une application web interactive développée avec Streamlit, conçue pour faciliter la gestion d'une boutique de vélos en ligne. Elle offre une interface conviviale permettant de visualiser, ajouter, modifier et supprimer des produits, ainsi que de gérer les commandes et les clients.

---

## 🛠️ Fonctionnalités principales

- **Gestion des produits** : Ajoutez, modifiez ou supprimez des vélos de votre catalogue.
- **Visualisation des données** : Consultez les statistiques de ventes et les tendances du marché.
- **Gestion des commandes** : Suivez les commandes en cours et l'historique des ventes.
- **Interface utilisateur intuitive** : Naviguez facilement grâce à une interface claire et responsive.
- **Authentification sécurisée** : Protégez l'accès à l'application avec un système de connexion sécurisé.

---

## 🚀 Installation et démarrage

Suivez ces étapes pour installer et exécuter l'application en local :

1. **Cloner le dépôt GitHub** :

   ```bash
   git clone https://github.com/StanislasComputerScience/e_bike_shop.git
   cd e_bike_shop
   git checkout controller
   ```

2. **Créer un environnement virtuel** (optionnel mais recommandé) :

   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Exécuter l'application** :

   ```bash
   streamlit run Home.py
   ```

   L'application sera accessible à l'adresse : [http://localhost:8501](http://localhost:8501)

---

## 📁 Structure du projet

```bash
e_bike_shop/
├── Home.py                 # Point d'entrée de l'application Streamlit
├── pages/                  # Pages supplémentaires de l'application
├── requirements.txt        # Liste des dépendances Python
├── create_db.sh            # Script pour initialiser la base de données
├── remove_bd.sh            # Script pour supprimer la base de données
├── run_app.sh              # Script pour lancer l'application
├── README.md               # Ce fichier
└── LICENSE                 # Licence du projet
```

---

## 🔐 Authentification

L'application utilise le système d'authentification intégré de Streamlit (à partir de la version 1.42) pour sécuriser l'accès. Vous pouvez configurer les fournisseurs d'identité (Google, Microsoft, etc.) en suivant la documentation officielle de Streamlit.

---

## ☁️ Déploiement

Pour rendre l'application accessible en ligne, vous pouvez la déployer sur des plateformes telles que :

- **Streamlit Community Cloud** : Solution gratuite et simple pour héberger des applications Streamlit.
- **Heroku** : Plateforme cloud permettant de déployer des applications web.
- **AWS / Google Cloud** : Pour des besoins plus avancés en termes de scalabilité et de personnalisation.

---

## 💡 Ressources supplémentaires

- [Documentation officielle de Streamlit](https://docs.streamlit.io/)
- [Guide de déploiement Streamlit](https://docs.streamlit.io/streamlit-cloud)
- [Liste des émojis compatibles Streamlit](https://share.streamlit.io/streamlit/emoji-shortcodes)

---

## 📞 Support

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur le dépôt GitHub ou à me contacter directement.

---

Merci d'avoir choisi **e_bike_shop** pour gérer votre boutique en ligne de vélos ! 🚴‍♀️💨
