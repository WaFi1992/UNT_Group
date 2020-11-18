from flask import abort, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from bookapp.forms import RegistrationForm, LoginForm, PostForm
from bookapp.models import User, Posts
from bookapp import app, db, bcrypt
from bookapp.scrape import getBookDetails



@app.route('/')
@app.route('/home')
def index():
    posts = Posts.query.all()
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data.lower(), password=hashed_password, email=form.email.data.lower(),
                    major=form.major.data, payment_profile=form.payment_profile.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Please log in', category='Success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash(f'Login failed, please check email and password')
    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title="Account")

@app.route('/post/new', methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        data = getBookDetails(form.isbn.data)
        post = Posts(isbn=form.isbn.data, condition=form.condition.data, price=form.price.data, major=form.major.data, author=current_user, title=data['title'], publisher=data['publisher'], writers=data['author'], image_ref=data['imgCover'])
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created.", "success")
        return redirect('/home')
    return render_template('create_post.html', title="New Post", form=form, legend='New Post')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Posts.query.get_or_404(post_id)
    return render_template('post.html', title=Posts.title, post=post)



@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.condition = form.condition.data
        db.session.commit()
        flash("Your post was updated successfully!", "success")
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.isbn.data = post.isbn
        form.price.data = post.price
        form.major.data = post.major
        form.condition.data = post.condition
    return render_template('create_post.html', title="Update Post", form=form)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Posts.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted", "success")
    return redirect('/home')