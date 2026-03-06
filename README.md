# 💘 Flask Dating App (Hanze Project)

Een overzichtelijke en gebruiksvriendelijke webapplicatie gebouwd met Python en Flask. Deze app stelt gebruikers in staat om een account aan te maken, een persoonlijk profiel in te vullen en andere singles te ontdekken.

## ✨ Features
* **Gebruikersauthenticatie:** Veilig registreren en inloggen met gehashte wachtwoorden (Werkzeug).
* **Profielbeheer:** Gebruikers kunnen hun eigen profiel aanmaken en bekijken met een bio, leeftijd en profielfoto.
* **Ontdekken:** Een overzichtelijke pagina waar ingelogde gebruikers de profielen van andere singles kunnen bekijken.
* **Beveiligde Routes:** Bepaalde pagina's zijn alleen toegankelijk voor ingelogde gebruikers.

## 🛠️ Gebruikte Technologieën
* **Backend:** Python, Flask
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templates
* **Security:** Werkzeug Security (Password Hashing), python-dotenv (Environment variables)

## 🚀 Lokaal Installeren

Wil je dit project lokaal draaien op je eigen machine? Volg dan deze stappen:

### 1. Clone de repository
```bash
git clone [https://github.com/liron06/Hanze-Dating-app.git](https://github.com/liron06/Hanze-Dating-app.git)
cd Hanze-Dating-app

```

### 2. Maak een virtuele omgeving aan (optioneel maar aangeraden)

```bash
python -m venv venv
source venv/bin/activate  # Voor Mac/Linux
venv\Scripts\activate     # Voor Windows

```

### 3. Installeer de benodigdheden

Zorg dat je de benodigde Python-pakketten installeert:

```bash
pip install Flask Werkzeug python-dotenv

```

### 4. Omgevingsvariabelen instellen (.env)

Maak een bestand aan genaamd `.env` in de hoofdmap van het project en voeg je eigen geheime sleutel toe voor Flask-sessies:

```env
SECRET_KEY=jouw_eigen_geheime_sleutel_hier

```

### 5. Database instellen

*(Let op: De database wordt om veiligheidsredenen niet meegeleverd in deze repo. Je moet zelf de tabellen `gebruikers` en `profielen` aanmaken in een `datingsite.db` bestand via SQLite).*

### 6. Start de applicatie

```bash
python app.py

```

De applicatie draait nu lokaal op `http://127.0.0.1:5000/`.

## 📌 Status van het project

Dit project is momenteel in actieve ontwikkeling. Toekomstige features zijn onder andere een zoekfunctie en de mogelijkheid om profielen te bewerken.
