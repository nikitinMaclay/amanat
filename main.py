import datetime

from flask import Flask, render_template, redirect, request, make_response, abort, jsonify

from data import db_session
from data.users import User

from flask_login import LoginManager, login_user, logout_user, login_required, current_user


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
    return render_template('index.html')


@app.route("/index_after_enter", methods=["GET", "POST"])
def index_after_enter():
    return render_template('index_after_enter.html')


@app.route("/address", methods=["GET", "POST"])
def address():
    print(1)
    return render_template('address.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/user_profile', methods=["GET", "POST"])
@login_required
def user_profile():
    if request.method == "GET":
        pass
    else:
        abort(404)
    return render_template('cabinet.html')


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
