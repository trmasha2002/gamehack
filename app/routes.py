from flask import render_template, request
from app import app
from app.forms import CodeForm
from flask import render_template, flash, redirect
import sys
import os
import json
import subprocess
from contextlib import redirect_stdout
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    if request.method == "POST":
        f = open("file.py", "w")
        print(form.code.data,file=f)
        f.close()
        command = "pycodestyle --statistics file.py"
        pipe = os.popen(command)
        result = pipe.readlines()
        result_main = dict()
        result_main["arr"] = result
        o = open("output.json", "w")
        result = json.dumps(result_main)
        o.write(result)
        #result = subprocess.check_output(["pycodestyle", '--statistics', 'file.py'])
        #result = os.system("pycodestyle --statistics file.py")
        #print(result)
        #result = json.dumps(result)
        return result

    return render_template('game.html', form=form)



