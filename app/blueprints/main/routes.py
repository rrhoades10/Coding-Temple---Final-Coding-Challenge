from flask import render_template, request, redirect, url_for, flash 
from .import bp as main
from flask_login import login_required



@main.route('/', methods=['GET'])
@login_required
def index():
    
    
    context = {
        
    }
    return render_template('main/index.html', **context)