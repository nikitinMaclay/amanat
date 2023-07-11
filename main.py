import datetime

from flask import Flask, render_template, redirect, request, make_response, abort, jsonify

from data import db_session
from data.users import User
from data.products import Product
from data.users_products import UserProduct
from data.status import Status

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from forms.sign_up import RegistrationForm
from forms.sign_in import LoginForm
from forms.create_product import CreateProductForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'amanat_copy'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        return redirect("/index_after_enter")
    form_regist = RegistrationForm()
    form_login = LoginForm()
    if form_regist.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.phone_number == form_regist.phone_num.data).first():
            return render_template('index.html', title='Регистрация',
                                   form_regist=form_regist, form_login=form_login,
                                   message="Такой пользователь уже есть", login="", regist="active show")
        user = User(
            phone_number=form_regist.phone_num.data,
            name=form_regist.username.data,
            user_city=form_regist.city.data,
        )
        user.set_password(form_regist.password.data)
        db_sess.add(user)
        db_sess.commit()
        login_user(user, remember=True)
        return redirect("/index_after_enter")
    if form_login.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.phone_number == form_login.phone_num.data).first()
        if user and user.check_password(form_login.password.data):
            login_user(user, remember=True)
            return redirect("/index_after_enter")
        return render_template('index.html',
                               message_login="Неправильный логин или пароль",
                               form_regist=form_regist, form_login=form_login, login="active show",
                               message="", regist="")
    return render_template('index.html', form_regist=form_regist,
                           form_login=form_login, login="active show", message="", regist="", message_login="")


@app.route("/index_after_enter", methods=["GET", "POST"])
def index_after_enter():
    return render_template('index_after_enter.html')


@app.route("/catalog", methods=["GET", "POST"])
def catalog():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        goods = db_sess.query(Product).all()
        return render_template('catalog.html', goods=goods)
    else:
        return redirect("/")


@app.route("/product/<int:product_id>", methods=["GET", "POST"])
def product(product_id):
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        definite_product = db_sess.query(Product).filter(Product.product_id == product_id).first()

        return render_template('good_card.html', definite_product=definite_product)
    else:
        return redirect("/")


@app.route("/cabinet", methods=["GET", "POST"])
def cabinet():
    if current_user.is_authenticated:
        return render_template('cabinet.html')
    else:
        return redirect("/")


@app.route("/address", methods=["GET", "POST"])
def address():
    if current_user.is_authenticated:
        return render_template('address.html', asc_code=f"({current_user.phone_number}){current_user.name}")
    else:
        return redirect("/")


@app.route("/questions", methods=["GET", "POST"])
def questions():
    return render_template('questions.html')


@app.route("/parcels", methods=["GET", "POST"])
def parcels():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        user_orders = db_sess.query(UserProduct).filter(UserProduct.creator_id == current_user.id,
                                                        UserProduct.status_id != 5).all()
        return render_template('parcels.html', user_orders=user_orders)
    else:
        return redirect("/")


@app.route("/parcels/create", methods=["GET", "POST"])
def parcels_create():
    if current_user.is_authenticated:
        form = CreateProductForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            user_product = UserProduct(
            )
            user_product.product_name = form.product_name.data
            user_product.creator_id = current_user.id
            user_product.track_number = form.track_number.data

            db_sess.add(user_product)
            db_sess.commit()

            return redirect("/parcels")

        return render_template('create_order.html', form=form)
    else:
        return redirect("/")


@app.route("/parcels/archive", methods=["GET", "POST"])
def parcels_archive():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()

        user_orders = db_sess.query(UserProduct).filter(UserProduct.creator_id == current_user.id,
                                                        UserProduct.status_id == 5).all()
        return render_template('archive.html', user_orders=user_orders)
    else:
        return redirect("/")


@app.route("/parcels/<int:parcel_id>", methods=["GET", "POST"])
def parcels_track(parcel_id):
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        track_info = db_sess.query(UserProduct).filter(UserProduct.id == parcel_id).first()

        return render_template('parcel_track_template.html', track_info=track_info, track_status=track_info.status_id)
    else:
        return redirect("/")

@app.route('/user_profile', methods=["GET", "POST"])
@login_required
def user_profile():
    if current_user.is_authenticated:
        if request.method == "GET":
            pass
        else:
            abort(404)
        return render_template('cabinet.html')
    else:
        return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


def main():
    db_session.global_init("databases/amanat.db")

    app.run()


if __name__ == '__main__':
    main()
