# handlers.py
from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('blad/404.html') , 404 #łapie bład 404 przechwytuje w locie 
    
