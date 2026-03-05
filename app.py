from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

#de geheime sleutel
app.secret_key = 'hanze_super_geheim_2026'

#voor makkelijk db te openen
def get_db_connection():
    conn = sqlite3.connect('datingsite.db')
    conn.row_factory = sqlite3.Row
    return conn


#route naar homepagina
@app.route('/')
def index():
    return render_template('index.html')

#route naar registreer pagina
@app.route('/registreer', methods=['GET', 'POST'])
def registreer():

    if request.method == 'POST':
        gebruikersnaam = request.form['gebruikersnaam']
        wachtwoord = request.form['wachtwoord']

        gehasht_wachtwoord = generate_password_hash(wachtwoord)

        conn = get_db_connection()

        try:
            conn.execute('INSERT INTO gebruikers (gebruikersnaam, wachtwoord) VALUES (?, ?)',
            (gebruikersnaam, gehasht_wachtwoord))
            conn.commit()

            flash('Account succesvol aangemaakt! Je kunt nu inloggen.', 'success')
            return redirect(url_for('login'))
        
        except sqlite3.IntegrityError:
            flash('Deze gebruikersnaam bestaat al. Kies een andere.', 'danger')
        finally:
            conn.close()

    return render_template('registreer.html')

#route naar Loginpagina
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        gebruikersnaam = request.form['gebruikersnaam']
        wachtwoord = request.form['wachtwoord']

        conn = get_db_connection()
        gebruiker = conn.execute('SELECT * FROM gebruikers WHERE gebruikersnaam = ?', (gebruikersnaam,)).fetchone()

        if gebruiker and check_password_hash(gebruiker['wachtwoord'], wachtwoord):
            session['gebruiker_id'] = gebruiker['id']
            session['gebruikersnaam'] = gebruiker['gebruikersnaam']
            
            profiel = conn.execute('SELECT * FROM profielen WHERE gebruiker_id = ?', (gebruiker['id'],)).fetchone()
            conn.close()
            
            if profiel:
                flash('Succesvol ingelogd! Welkom terug.', 'success')
                return redirect(url_for('profielen'))
            else:
                flash('Welkom! Maak eerst even je profiel aan voordat je kunt rondkijken.', 'info')
                return redirect(url_for('maak_profiel'))
        else:
            conn.close()
            flash('Verkeerde gebruikersnaam of wachtwoord', 'danger')

    return render_template('login.html')

#uitloggen
@app.route('/uitloggen')
def uitloggen():
    session.clear()
    flash('Je bent succesvol uitgelogd. Tot ziens!', 'info')
    return redirect(url_for('index'))

#profiel maken
@app.route('/maak_profiel', methods=['GET', 'POST'])
def maak_profiel():
    if 'gebruiker_id' not in session:
        flash('Je moet ingelogd zijn om een profiel aan te maken.', 'warning')
        return redirect(url_for('login'))
    if request.method == 'POST':
        naam = request.form['naam']
        leeftijd = request.form['leeftijd']
        geslacht = request.form['geslacht']
        foto_url = request.form['foto_url']
        bio = request.form['bio']
        gebruiker_id = session['gebruiker_id']

        conn = get_db_connection()
        try:
            conn.execute('''
                        INSERT INTO profielen (gebruiker_id, naam, leeftijd, geslacht, foto_url, bio)   
                        VALUES (?, ?, ?, ?, ?, ?)                        
                    ''', (gebruiker_id, naam, leeftijd, geslacht, foto_url, bio))
            conn.commit()

            flash('Je profiel is succesvol aangemaakt! je kunt nu rondkijken.', 'success')
            return redirect(url_for('profielen'))
        except sqlite3.IntegrityError:
            flash('Je hebt al een profiel!', 'warning')
            return redirect(url_for('profielen'))
        finally:
            conn.close()
        
    return render_template('maak_profiel.html')

#route naar profielen
@app.route('/profielen')
def profielen():
    if 'gebruiker_id' not in session:
        flash('Je moet ingelogd zijn om de singles te bekijken.', 'warning')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    mijn_profiel = conn.execute('SELECT * FROM profielen WHERE gebruiker_id = ?', (session['gebruiker_id'],)).fetchone()

    if not mijn_profiel:
        conn.close()
        flash('Je mag pas rondkijken als je zelf een profiel hebt gemaakt.', 'danger')
        return redirect(url_for('maak_profiel'))


    andere_singles = conn.execute('SELECT * FROM profielen WHERE gebruiker_id != ?', (session['gebruiker_id'],)).fetchall()
    conn.close()
    return render_template('profielen.html', profielen=andere_singles)

#mijn profiel functie
@app.route('/mijn_profiel')
def mijn_profiel():
    if 'gebruiker_id' not in session:
        flash('Je moet ingelogd zijn om je profiel te bekijken.', 'warning')
        return redirect(url_for('index'))

    huidige_gebruiker_id = session['gebruiker_id']

    conn = get_db_connection()
    mijn_gegevens = conn.execute('SELECT * FROM profielen WHERE id = ?', (huidige_gebruiker_id,)).fetchone()
    conn.close()

    if not mijn_gegevens:
        flash('Je hebt nog geen profiel aangemaakt!', 'info')
        return redirect(url_for('maak_profiel'))

    return render_template('mijn_profiel.html', profiel=mijn_gegevens)


#server start
if __name__ == '__main__':
    app.run(debug=True)