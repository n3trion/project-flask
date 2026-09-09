from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello WOrld!"

@app.route("/o-nas") 
def onas():
    return "Jesteśmy klasą 4 Technik Programista. Robimy sklep."

@app.route("/kontakt")
def kontakt():
    return "Napisz: sklep@example.com"

@app.route("/regulamin")
def regulamin():
    return "regulamin"

@app.route("/admin")
def admin():
    return "Brak dostępu", 403

@app.route("/app/info")
def appinfo():
    return {"nazwa": "flask-start","autor": "Pavlo Kavkovskyi", "wersja": "0.1"}
if __name__ == "__main__":
    app.run(debug=True)