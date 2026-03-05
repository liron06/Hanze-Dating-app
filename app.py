from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

#de geheime sleutel
app.secret_key = 'hanze_super_geheim_2026'

#voor makkelijk db te openen
def get_db_connection():
    conn = sqlite3.connect('datingsite.db')
    conn.row_factory = sqlite3.row
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

        conn = get_db_connection

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
@app.route('/login')
def login():
    return "<h1>Hier komt straks de login pagina te staan</h1>"

#route naar profielen
@app.route('/profielen')
def profielen():
    return "<h1>Hier komt straks de profielen pagina te staan</h1>"

#server start
if __name__ == '__main__':
    app.run(debug=True)