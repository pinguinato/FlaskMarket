# Flask Market

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



