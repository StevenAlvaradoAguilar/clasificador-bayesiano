from flask import Flask, render_template, request
import Bayes
import funcionespostgres
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
    percent1= int(cant1/universo*100)
    percent2= int(cant2/universo*100)
    percent3= 100-(percent1+percent2)
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

    # lista para las urls clasificadas como deportes
    list1 = funcionespostgres.obtenerURLS()[0]

    # lista para las urls clasificadas como sexual
    list2 = funcionespostgres.obtenerURLS()[1]
   
    listUrls=[]
    if categoria=='deportes':
        listUrls = list1
    else:
        listUrls= list2

    data={
        'titulo':'Categoria',
        'categoria':categoria,
        'listUrls':listUrls
    }
    return render_template('categoria.html',data=data)

@app.route('/palabras/<categoria>/<url>')
def palabras(categoria, url):
    listPalabras = funcionespostgres.obtenerPalabras(url)
    
    data={
        'titulo':'Palabras',
        'categoria':categoria,
        'url':url,
        'listPalabras':listPalabras
    }
    return render_template('palabras.html',data=data)

@app.errorhandler(404)
def page_not_found(error):
    data={
        'titulo':'Not Found',
    }
    return render_template("404.html", data=data), 404


def query_string():
    listPalabras = funcionespostgres.obtenerPalabras(request.args.get('url'))
    data={
        'titulo':'Palabras',
        'categoria': request.args.get('categoria'),
        'url':request.args.get('url'),
        'listPalabras': listPalabras
    }

    return render_template('palabras.html',data=data)

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.run(debug=True, port = 5000)