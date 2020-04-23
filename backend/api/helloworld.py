from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from serviceApplication import hello

bluePrint = Blueprint('helloWorld', __name__)
helloTest = hello.hello()



@bluePrint.route('/helloWorld',methods=('GET',))
def createMessage():
    return jsonify(helloTest.returnData())

@bluePrint.route('/helloWorldTest',methods=('GET',))
def createMessage2():
    return jsonify(helloTest.returnSomeThing())
