from flask import render_template, request
from app import app
from app.forms import CodeForm
from flask import render_template, flash, redirect
import os
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    if request.method == "POST":
        print(request.form)
        f = open("file.py", "w")
        f.write(form.code.data)
        f.close()
        result = []
        result.append(os.system("pycodestyle --statistics file.py"))
        print(result)
        return redirect('/index')

    return render_template('game.html', form=form)



