#model -db
#View - user view on page - v djange controller
#templates u djangi dlya user view page
#controller - svyaz view i model


from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Dimon'
    return render_template('index.html' , n = name)



#{'/' : 'index'} slovap v korne flask , ssilka na kornevoy index '/' view.index
#dikorator na ntgo ukazivaet app.route('/') i govorit chto delat c functions print hello world
