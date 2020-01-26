from flask import render_template, request
from app import app
from app.forms import CodeForm
from flask import render_template, flash, redirect, jsonify
import sys
import os
import json
import subprocess
from contextlib import redirect_stdout
@app.route('/index',methods=['GET', 'POST'])
def index():
    form = CodeForm()
    # if request.method == "POST":
    #     f = open("file.py", "w")
    #     print(form.code.data,file=f)
    #     f.close()
    #     command = "pycodestyle --statistics file.py"
    #     pipe = os.popen(command)
    #     result = pipe.readlines()
    #     return jsonify({'result':result})
    return render_template('game.html', form=form)




@app.route('/check', methods=['POST'])
def check():
    form = CodeForm()
    f = open("file.py", "w")
    print(form.code.data, file=f)
    f.close()
    command = "pycodestyle --statistics file.py"
    pipe = os.popen(command)
    result = pipe.readlines()
    return jsonify({'result': result})
