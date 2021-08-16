# Flask Market

Fonte: http://jimshapedcoding.com/home/ e
http://jimshapedcoding.com/courses/Flask%20Full%20Series

## 1
        pip install flask

## 2

       flask --version

        Python 3.8.6
        Flask 2.0.1
        Werkzeug 2.0.1

## 3

Setting di una var d'ambiente in Windows Terminal:

        set FLASK_APP=market.py

## 4

Lancio dell'applicazione:

        flask run

## 5

Cartella /templates dove Flask legge gli HTML di default, è ncessario importare il metodo **render_template()** in grado di richiamare gli html.

        from flask import render_template

Esempio:

        @app.route('/')
        def home_page():
            return render_template('home.html')

## 6 Integrazione Bootstrap dentro Flask

https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template

## 7 Abilitare il DEBUG

Digitare al terminale:

        set FLASK_DEBUG=1

## 8 Passaggio dati ai templates con Jinja2

Esempio:

        @app.route('/market')
        def market_page():
            items = [
                {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
                {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
                {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
            ]
            return render_template('market.html', items=items)


        ...
        <tbody>
        <!-- Your rows inside the table HERE: -->
        {% for item in items %}
            <tr>
                <td>{{ item.id }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.barcode }}</td>
                <td>{{ item.price }} €</td>
                <td>
                    <button class="btn btn-outline btn-info">More info</button>
                    <button class="btn btn-outline btn-success">Purchase this item</button>
                </td>
            </tr>
        {% endfor %}
        </tbody>
        ...

## 9 Ereditarietà dei templates

Esempio:

- definite un file html chiamandolo base.html dentro la cartella dei templates
- modificare i file html in modo che ereditino il base.html in questo modo:

        {% extends 'base.html' %}

- per rendere dinamico il titolo della pagina usare il tag block di Jinja:

In base.html

        <title>
          {% block title %}
          {% endblock %}
        </title>

e poi nel file home.html

        {% block title %}
            Home Page
        {% endblock %}

- per personalizzare il contenuto del body della pagina html:

In base.html

        {% block content %}
        {% endblock %}

e in home.html

        {% block content %}
            This is our content for the Home Page
        {% endblock %}

ecc... ecc...

## 10 dinamicizzare gli URL

        <a class="nav-link" href="{{ url_for('home_page') }}">Home <span class="sr-only">(current)</span></a>

## 11 Collegamento a SQLlite

Bisogna installare dei tools per Flask

    pip install flask-sqlalchemy

poi nel file python dell'applicazione:

    from flask_sqlalchemy import SQLAlchemy

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
    db = SQLAlchemy(app)

poi è necessario definire una classe MODELLO di dati:

    class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

Alcuni esempi di come si interagisce con un DB sqlite e Python direttamente dalla console:

- creazione del database da zero:

      db.create.all()

- inserimento di un item nel db:

      from market import Item
      
      item1 = Item(name="IPhone 10", price=500, barcode='987654321234', description="telefono cellulare Iphone 10")
      db.session.add()
      db.session.commit()

- visualizzazione contenuto del db:

      Item.query.all()

- drop di tutte le tabelle

      db.drop_all()

- ricreazione

      db.create_all()

**Importante**

      def __repr__(self):
        return f'Item {self.name}'

Serve per vedere il contenuto dei records nel DB:

      >>> Item.query.all()
      [Item IPhone 10, Item MSI GF63 Thin]

**Importante**

Passiamo i dati del DB alla pagina del market:

    @app.route('/market')
    def market_page():
      items = Item.query.all()
      return render_template('market.html', items=items)


