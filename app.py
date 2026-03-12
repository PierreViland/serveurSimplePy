from flask import Flask, request

app = Flask(__name__)

VALID_USER = "admin"
VALID_PASS = "unTienVautMieuxQueDeuxTuLAuras"  

@app.route("/", methods=["GET"])
def index():
    return """
    <html>
      <body>
        <h2>Authentification</h2>

        <form action="/login" method="POST">
          <label>Login:</label><br>
          <input type="text" name="login"><br><br>
          <label>Password:</label><br>
          <input type="password" name="password"><br><br>
          <input type="submit" value="Se connecter">
        </form>
        <p style="font-size:10px;">Site web basé sur :</p>
        <p style="font-size:10px;"><a href="https://github.com/PierreViland/serveurSimplePy/">https://github.com/PierreViland/serveurSimplePy/</a></p>
    </body>
    </html>
    """

@app.route("/login", methods=["POST"])
def login():
    login = request.form.get("login", "")
    password = request.form.get("password", "")

    if login == VALID_USER and password == VALID_PASS:
        return "<h1>Bienvenue ! Authentification réussie. <strong>Le Flag est le mot de passe</strong></h1>"
    else:
        return "<h1>Identifiants incorrects.</h1><a href='/'>Retour</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

