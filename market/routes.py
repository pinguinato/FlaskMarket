from market import app
from flask import render_template
from flask import redirect
from flask import url_for
from market.models import Item
from market.models import User
from market.forms import RegisterForm
from market import db
from flask import flash


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #Se non ci sono errori
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}') # scrive errore sul terminale
            flash(f'There was an error with creating a user: {err_msg}', category='danger') # scrive errore su pagina web

    return render_template('register.html', form=form)
