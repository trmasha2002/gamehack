from flask import render_template
from app import app
from app.forms import CodeForm
from flask import render_template, flash, redirect
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    if form.validate_on_submit():
        f = open("file.txt", "w")
        f.write(form.code.data)
        return redirect('/index')
    return render_template('base.html', title="Code In", form=form)

