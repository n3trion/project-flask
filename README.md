# flask-start

Pierwsza aplikajca Flask - trasy tekstowe.

## Uruchomienie
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

## Autor
Pavlo Kavkovskyi, 4 Technik Programista

git init 
git add .
git commit -m "Flask: hello world i trasy tekstowe"
git branch -M main
git remote add origin https://github.com/n3trion/flask-start.git
git push -u origin main

## karoche
abort – zakończ z błędem:
ELEMENTY = {1: "produkty", 2: "ogloszenia", 3: "sale", 4: "posty"}
@app.route("/element/<int:id>")
def element(id):
    if id not in ELEMENTY:
        abort(404)
    return f"Element: {ELEMENTY[id]}"


redirect – przekierowanie:
@app.route("/start")
def start():
    return redirect(url_for("/"))


url_for – nie wpisuj adresów ręcznie:
@app.route("/start")
def start():
    return redirect(url_for("/"))

Query string:
@app.route("/produkty")
def produkty():
    kategoria = request.args.get("kat", "wszystkie")
    sortowanie = request.args.get("sort", "domyslnie")
    return f"Kategoria: {kategoria}, sortowanie: {sortowanie}"


    