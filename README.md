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

## 12 Flask Forms

    pip install wtforms

    pip install flask-wtf

Realizzare una form di registrazione (forms.py):

    from flask_wtf import FlaskForm
    from wtforms import StringField
    from wtforms import PasswordField
    from wtforms import SubmitField


    class RegisterForm(FlaskForm):
      username = StringField(label='username')
      email_address = StringField(label='email')
      password1 = PasswordField(label='password1')
      password2 = PasswordField(label='password2')
      submit = SubmitField(label='submit')

template html (register.html):

    {% extends 'base.html' %}
    {% block title %}
      Register Page
    {% endblock %}
    {% block content %}
      <h1>Register Form</h1>
    {% endblock %}

Ricordarsi di definire un secret key all'interno di __init__.py altrimenti non si possono usare le features del pacchetto dei forms:

    app.config['SECRET_KEY'] = 'a1a9db1281afaf34d50225e9'

è possibile definirla aprendo un temrinale python in questo modo:

    import os
    os.random(12).hex()

## 13 Importare la form dentro il template file

Esempio (register.html):

    {% block content %}
      <body class="text-center">
        <div class="container">
        <form method="POST" class="form-register" style="color:white;">
            <img class="mb-4" src="https://res.cloudinary.com/jimshapedcoding/image/upload/v1597332609/android-icon-192x192_ove2a7.png" alt="">
            <h1 class="h3 mb-3 font-weight-normal">
                Please Create your Account
            </h1>
            <br>
            {{ form.username.label() }}
            {{ form.username(class="form-control", placeholder="User name") }}
            {{ form.email_address.label() }}
            {{ form.email_address(class="form-control", placeholder="Email Address") }}
            {{ form.password1.label() }}
            {{ form.password1(class="form-control", placeholder="Password") }}
            {{ form.password2.label() }}
            {{ form.password2(class="form-control", placeholder="Confirm Password") }}
            <br>
            {{ form.submit(class="btn btn-lg btn-block btn-primary") }}
        </form>
      </div>
    </body>
    {% endblock %}

## 14 Flask Validazione dei forms

