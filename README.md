# api-flask-project
# 🚀 API REST Flask — Gestionnaire de Tâches

# À livrer le Dimanche

---

## 🧑‍💻 Rôle de chaque membre

---

`Pouye`
`app.py` : C'est le chef d'orchestre. Il initialise le serveur Flask, enregistre les routes et démarre l'application. C'est le point d'entrée du projet — on le lance avec `python app.py`.

---

`config.py` : C'est le panneau de contrôle. Il centralise toute la configuration du projet : le chemin vers la base de données, le mode DEBUG, le HOST et le PORT. Les autres fichiers viennent y lire leurs paramètres.

---

`Mamadou Seck`
`models.py` : C'est la mémoire. Il s'occupe uniquement de communiquer avec la base SQLite : créer la table au démarrage, lire, insérer, modifier et supprimer des tâches. Il ne sait pas comment les données sont affichées ni comment les routes fonctionnent.

---

`Mamadou Moussé Ndiaye`
`routes.py` : C'est la façade. Il définit tous les endpoints de l'API (GET, POST, PUT, DELETE), valide les données reçues, appelle les fonctions de `models.py` et retourne des réponses JSON avec les bons codes HTTP.

---

`Abdoul Aziz Diop`
`tests/` : C'est le filet de sécurité. Il contient les scripts de test et la collection Postman. Il vérifie que chaque route répond correctement, aussi bien dans les cas normaux que dans les cas d'erreur (ID inexistant, JSON invalide, etc.).

---

## Ce que fait le projet

Ce projet est une **API REST qui fonctionne en local**. Elle permet de créer, lire, modifier et supprimer des tâches via des requêtes HTTP, testables depuis **Postman** ou un navigateur. Les tâches sont sauvegardées dans une base **SQLite** sur l'ordinateur, ce qui signifie qu'elles sont **conservées même après avoir redémarré le serveur**.

---

## Fonctionnement concret

Quand on lance le serveur avec `python app.py`, il écoute sur `http://localhost:5000`. On peut ensuite lui envoyer des requêtes HTTP :

1. Lister toutes les tâches — `GET /api/taches`**  
Le serveur retourne la liste complète des tâches enregistrées dans la base, au format JSON.

2. Récupérer une tâche — `GET /api/taches/<id>`**  
On précise l'ID d'une tâche. Le serveur retourne ses détails. Si l'ID n'existe pas, il répond `404`.

3. Ajouter une tâche — `POST /api/taches`**  
On envoie un JSON avec un titre. Le serveur crée automatiquement un ID unique et attribue le statut `à faire` par défaut. La tâche est immédiatement sauvegardée dans la base.

4. Modifier une tâche — `PUT /api/taches/<id>`**  
On précise l'ID et on envoie les nouvelles valeurs (titre, statut). Le serveur met à jour la tâche dans la base.

5. Supprimer une tâche — `DELETE /api/taches/<id>`**  
On précise l'ID de la tâche à effacer. Le serveur la retire de la base et confirme la suppression.

---

## Comment les données sont stockées

Toutes les tâches sont enregistrées dans une base **SQLite** (`database.db`) sous ce format :

```json
[
    {"id": 1, "titre": "Préparer la présentation", "statut": "en cours"},
    {"id": 2, "titre": "Rendre le rapport", "statut": "à faire"}
]
```

Ce fichier est créé automatiquement au premier lancement grâce à la fonction `init_db()` dans `models.py`. Si la base est absente, elle est recréée proprement sans planter.

---

## Nom des fonctions

```python
# models.py — Mamadou Seck
init_db, get_all_taches, get_tache_by_id, create_tache, update_tache, delete_tache

# routes.py — Mamadou Moussé Ndiaye
lister_taches, detail_tache, ajouter_tache, modifier_tache, supprimer_tache

# app.py — Pouye
create_app
```