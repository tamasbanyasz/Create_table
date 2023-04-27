from flask import redirect, url_for, render_template, request, flash
from storedatas import app, db
from storedatas.models import Employee, User
from storedatas.forms import NewUserFrom


with app.app_context():
    db.create_all()
    db.session.commit()
    print(f'-- > {Employee.query.all()}')
    print(f'-- > {User.query.all()}')


@app.route('/')
@app.route('/home')
def home():
    employee_db = db.session.execute(db.select(Employee)).scalars()
    return render_template('workers.html', emploeyees=employee_db)


@app.route('/message_board')
def message_board():
    return redirect(url_for('home'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = NewUserFrom()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(name=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()

            flash('Register succes!')
            return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/workers/new', methods=['GET', 'POST'])
def workers():
    if request.method == 'POST':
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        date = request.form.get('date')
        current_worker = Employee(firstname=first_name, lastname=last_name, date=date)
        db.session.add(current_worker)
        db.session.commit()

        flash('Employee added!', 'succes')
        return redirect(url_for('home'))
    return render_template('create.html', title='New Workers register')
