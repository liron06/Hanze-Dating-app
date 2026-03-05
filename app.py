from flask import Flask, render_template

app = Flask(__name__)


#route naar homepagina
@app.route('/')
def index():
    return render_template('index.html')

#route naar registreer pagina
@app.route('/registreer')
def registreer():
    return "<h1>Hier komt straks mijn registreer pagina te staan</h1>"

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