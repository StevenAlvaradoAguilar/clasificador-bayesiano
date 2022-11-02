from flask import Flask, render_template
import Bayes
app=Flask(__name__)

@app.route('/')
def index():
    bayes = Bayes
    bayes.sacarProbabilidadPrevia("https://www.espn.com/","deportes","sexual")

    universo = bayes.universo_G
    cat1=bayes.cat1_G
    cant1=bayes.cant1_G
    cat2=bayes.cat2_G
    cant2=bayes.cant2_G
    otro= bayes.otro_G
    percent1= cant1/universo*100
    percent2= cant2/universo*100
    percent3= otro/universo*100
    data={
        'titulo':'Clasificador Bayesiano',
        'text': 'Results',
        'universo':universo,
        'categoria1':cat1,
        'cantidad1':cant1,
        'categoria2':cat2,
        'cantidad2':cant2,
        'otro':otro,
        'percent1':percent1,
        'percent2':percent2,
        'percent3':percent3,
    }
    return render_template('index.html', data=data)

@app.route('/categoria/<categoria>')
def categoria(categoria):

    data={
        'titulo':'Categoria',
        'categoria':categoria
    }
    return render_template('categoria.html',data=data)





if __name__ == '__main__':
    app.run(debug=True, port = 5000)