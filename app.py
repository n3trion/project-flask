from flask import Flask,request,url_for,redirect,abort,Response, render_template
app = Flask(__name__)


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

@app.route("/czesc/<imie>/<int:wiek>")
def czesc(imie, wiek):
    return f"Cześć, {imie} {wiek}!"

@app.route("/produkt/<int:id>")
def produkt(id):
 return f"Produkt numer {id}, typ: {type(id).__name__}"



@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"{a}+{b} = {a+b}"
@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 404
    return f"{a}/{b} = {a/b}"
@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"{a}-{b} = {a-b}"
@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"{a}*{b} = {a*b}"
@app.route("/potega/<int:a>/<int:b>")
def potega(a, b):
    return f"{a}^{b} = {a**b}"




@app.route("/powitanie")
def powitanie():
    imie = request.args.get("imie", "nieznajomy")
    godzina = request.args.get("godzina", type=int)
    if godzina is not None and godzina < 12:
        return f"Dzień dobry, {imie}"
    return f"Witaj {imie}!"

@app.route("/linki")
def linki():
    return url_for("produkt", id=5) # zwróci: /produkt/5

@app.route("/stary-adres")
def stary():
    return redirect(url_for("powitanie"))



@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if not (1<=n<=20):
        return "Musi być w przedziale od 1 do 20", 400
    wiersz = [f"{i} * {n} = {i*n}" for i in range(1,11)]
    wynik = "\n".join(wiersz)
    return Response(wynik, mimetype='text/plain')



@app.route("/produkty123")
def produkty123():
    kategoria = request.args.get("kat", "wszystkie")
    sortowanie = request.args.get("sort", "domyslnie")
    return f"Kategoria: {kategoria}, sortowanie: {sortowanie}"


ELEMENTY = {1: "produkty", 2: "ogloszenia", 3: "sale", 4: "posty"}
@app.route("/element/<int:id>")
def element(id):
    if id not in ELEMENTY:
        abort(404)
    return f"Element: {ELEMENTY[id]}"
@app.route("/elementy")
def elementy():
    return f"Wszystkie elementy: {ELEMENTY}"


@app.route("/start")
def start():
    return redirect(url_for("/"))




@app.route("/")
def index():
    return render_template("index.html", imie="Pavlo", zalogowany=True, rola="admin", nazwa="Flask")

PRODUKTY = [
 {"id": 1, "nazwa": "Laptop", "cena": 2999, "dostepny": True},
 {"id": 2, "nazwa": "Mysz", "cena": 49, "dostepny": False},
 {"id": 3, "nazwa": "Klawiatura", "cena": 199, "dostepny": True},
]
@app.route("/lista")
def lista():
 return render_template("produkty.html",lista=PRODUKTY)
 
@app.route("/szukaj")
def szukaj():
    baza_produktow = ["Laptop", "Mysz bezprzewodowa", "Klawiatura mechaniczna"]
    fraza = request.args.get('q', '').strip()
    wyniki = [p for p in baza_produktow if fraza.lower() in p.lower()] if fraza else[]
    liczba_wynikow = len(wyniki)
    return render_template("szukaj.html", fraza=fraza, wyniki=wyniki, liczba_wynikow=liczba_wynikow)

@app.route("/dodaj1", methods=["GET", "POST"])
def dodaj1():
    if request.method == "POST":
        nowa_nazwa = request.form.get("nazwa_produktu", "").strip()
        cena = request.form.get("cena_produktu", "").strip()
        status_wybor = request.form.get("status_produktu", "true").strip()
        jest_dostepny = True if status_wybor == "true" else False
        if nowa_nazwa:
            nowy_obiekt_produktu = {
                "id": len(PRODUKTY) + 1,
                "nazwa": nowa_nazwa,
                "cena": cena,
                "dostepny": jest_dostepny
            }
            PRODUKTY.append(nowy_obiekt_produktu)
        return redirect(url_for("lista"))    
    return render_template("dodaj1.html")
if __name__ == "__main__":
    app.run(debug=True)