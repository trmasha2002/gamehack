from flask import render_template, request
from app import app
from app.forms import CodeForm
from flask import render_template, flash, redirect
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    if request.method == "POST":
        print(request.form)
        f = open("file.py", "w")
        print(form.code.data)
        f.write(form.code.data)
        return redirect('/index')

    return render_template('game.html', form=form)



