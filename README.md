
# 🚴‍♂️ eBike Shop – Application Streamlit pour boutique de vélos

par Rémi Labonne, Augustin Dendievel & César Gatano

---

Bonjour 👋,

Bienvenu dans le fichier README du projet **eBike Shop**, une application Streamlit connectée à une base de données relationnelle gérée avec la technologie sqlite3 sous Python dédiée à la gestion d'une boutique en ligne de vélos. Ce document vous guidera à travers les fonctionnalités de l'application et les étapes nécessaires pour commencer à l'utiliser.

<img src="./assets/logo/python.png" height="50"/> &nbsp;&nbsp;&nbsp;
<img src="./assets/logo/sqlite.png" height="50"/>  &nbsp;&nbsp;&nbsp;
<img src="./assets/logo/streamlit.png" height="50"/>

---

## 🚴‍♂️ Présentation de l'application

**eBike Shop** est une application web interactive développée avec Streamlit, conçue pour faciliter la gestion d'une boutique de vélos en ligne. Elle offre une interface conviviale permettant à des clients de visualiser les produits, de créer un panier et
de commander de façon fictive les produits sélectionnés. Cette application offre
également une interface simple pour administrer l'application avec des fonctionnalités
supplémentaires comme l'ajout de produits au catalogue, la gestion des stocks, ...

---

## 🛠️ Fonctionnalités client/utilisateur

- **Accueil** : Accueil sur l'application avec un aperçu des produits les plus vendus et des produits les plus populaires

<img src="./assets/screenshots/Home.png"/>

- **Mosaïque** : Visualisation sous forme de mosaïque de tous les produits du catalogue.

<img src="./assets/screenshots/Mosaique.png"/>

- **Interface catalogue** : Naviguation page par page du catalogue des produits avec toutes les informations disponibles.
  
<video width="1280" height="480" controls>
  <source src="./assets/screenshots/Catalogue.mp4" type="video/mp4">
</video>

- **Authentification sécurisée** : Système de connexions sécurisées avec mot de passe cryptée via la technologie bcrypt

<img src="./assets/screenshots/Connexion.png"/>

- **Création de panier**: Création automatique d'un panier dès l'ajout du premier produit
- **Gestion du panier**: Gestion du panier grâce à une page dédié: modification des quantités, suppression d'une ligne de commande et affichage instantannée des prix HT, TTC, totaux par produit et pour le panier entier.

<img src="./assets/screenshots/Panier.png"/>

- **Système de commande** : Création d'une facture à partir du panier et choix de l'adresse de livraison.

<img src="./assets/screenshots/Commande.png"/>

---

## 🛠️ Fonctionnalités administrateur

- **À venir...**


## 🚀 Installation et démarrage

Suivez ces étapes pour installer et exécuter l'application en local :

1. **Cloner le dépôt GitHub** :

   ```bash
   git clone https://github.com/StanislasComputerScience/e_bike_shop
   cd e_bike_shop
   ```

2. **Créer un environnement virtuel** (optionnel mais recommandé) :

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
   ```

3. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Création de la base de données de test** :

   ```bash
   python ./bdd/manager_db.py
   ```
   La base de données de test est créée à partir du fichier `ecommerce_databse.json`. Ce dernier peut-être copié-collé et adapté à vos besoins. Veillez à conserver la version
   originale de ce fichier ou à la récupérer depuis le repository sur gitHub pour toujours avoir une version fonctionnelle du fichier `ecommerce_databse.json`.

   **Attention:** En cas de test effectuée, il est probable qu'il faille supprimer le fichier
   `ecommerce_databse.json` et de le récréer avec commande ci-dessus.

6. **Exécuter l'application** :

   ```bash
   streamlit run Home.py
   ```

   ou

   ```bash
   ./scripts/run_app.sh
   ```

   L'application sera accessible à l'adresse : [http://localhost:8501](http://localhost:8501)

---

## 📁 Structure du projet

```bash
e_bike_shop/
├── Home.py                   # Point d'entrée de l'application Streamlit
├── const_values.py           # Constante utilisée par les différents programmes
├── pages/                    # Dossier contenant les pages supplémentaires
├──── 1_Connexion.py          # Page de connexion
├──── 2_Catalogue_produits.py # Page de catalogues de produits avec toutes les informations
├──── 3_Mosaique.py           # Mosaïque de produits sur une seule page
├──── 4_Panier.py             # Page dédiée à la gestion du panier
├──── 5_Commandes.py          # Page de facture et du choix de livraison
├──── 6_Administrateur.py     # Page réservé aux administrateurs
├── bdd/                      # Dossier contenant la base de données
├──── ecommerce_database.json # Instruction pour la création de la base de données de test
├──── ecommerce_database.db   # Base de données (créée après éxecution de manager_db.py)
├──── manager_db.py           # Programme de création de la base de données, version test
├────── assets/               # Ressources référées par la base de données
├──────── products/           # Dossier des ressources pour la table Product
├────────── *.jpeg/jpg/png    # Images des différents produits
├─── controller/              # Dossier de fonctionnalités python communicantes avec la BDD
├───── controller.py          # Librairie de fonctionnalités éxecutant les requêtes SQL
├───── tools.py               # Librairie d'outils supplémentaires
├─── scripts/                 # Dossier de scripts bash
├───── run_app.sh             # Lance l'application streamlit
├───── remove_db.sh           # Supprime la base de données
├───── create_db.sh           # Crée la base de données à partir du fichier json
├── requirements.txt          # Liste des dépendances Python
├── README.md                 # Ce fichier
├── LICENSE                   # Licence du projet
├── assets/                   # Ressources pour le README
├──── logo/                   # Dossier de logos
├────── *.png                 # Images des logos
└──── *.png                   # Illustrations des auteurs
```

---

## 🔐 Authentification

L'application utilise le système d'authentification intégré de Streamlit (à partir de la version 1.42) pour sécuriser l'accès. Vous pouvez configurer les fournisseurs d'identité (Google, Microsoft, etc.) en suivant la documentation officielle de Streamlit.

---

Merci d'avoir choisi **e_bike_shop** pour gérer votre boutique en ligne de vélos ! 🚴‍♀️💨
