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


@app.route('/one', methods=['GET', 'POST'])
def one():
    form = CodeForm()
    return render_template('game1.html', form=form)



@app.route('/two', methods=['GET', 'POST'])
def two():
    form = CodeForm()
    return render_template('game2.html', form=form)


@app.route('/three', methods=['GET', 'POST'])
def three():
    form = CodeForm()
    return render_template('game3.html', form=form)


@app.route('/four', methods=['GET', 'POST'])
def four():
    form = CodeForm()
    return render_template('game4.html', form=form)

@app.route('/five', methods=['GET', 'POST'])
def five():
    form = CodeForm()
    return render_template('game5.html', form=form)