from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#SERVIDOR WEB DE DESENVOLVIMENTO LINUX

#As aplicações Flask incluem um servidor um servidor web de desenvolvimento que pode ser iniciado com o comando flask run. Esse comando procura o nome do script Python que contém a instância da aplicação na variável de ambiente FLASK_APP.

#Para iniciar a aplicação hello.py da seção anterior, inicialmente certifique-se de que o ambiente virtual que você criou antes esteja ativado e tenha o Flask instalado. Para usuários de Linux e de macOS, inicie o servidor web assim:

""" export FLASK_APP=hello.py """
""" flask run """

""" Por Padrão ele ira exibir assim após o  'flask run':  

* Serving Flask app 'hello.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)"""

#Depois de iniciado, o servidor entra em um laço que aceita requisições e as atende. Esse laço continuará até que você parar a aplicação teclando Ctrl+C.

#Com o servidor executando, abra o seu navegador web e digite http://local-host:5000/ na barra de endereço.

#Se você digitar algo diferente após a URL de base, a aplicação não saberá lidar com isso e devolverá um código de erro 404 ao navegador - o conhecido erro que você obtém quando acessa uma página web inexistente.

#O servidor web oferecido pelo Flask tem como propósito ser usado somente para desenvolvimento e testes. Conheceremos os servidores web de produção mais a frente.

#O servidor web de desenvolvimento do Flask também pode ser iniciado em um programa chamando o método app.run(). Versões mais antigas do Flask que não tinham o comando flask exigiam que o servidor fosse iniciado por meio da execução do script principal da aplicação, o qual devia incluir o trecho de código a seguir no final:

if __name__ == '__main__':
    app.run()

#Embora o comando  flask run tenha tornado essa prática desnecessaria, o método   app.run() ainda pode ser conveniente em determindas ocasiões, por exemplo em testes de unidade, como veremos mais a frente.

#-----------------------------------------------------------#
#ROTAS DINÂMICAS

#A segunda versão do aplicação, acrescenta uma segunda rota que é dinâmica. Ao acessar o URL dinâmico em seu navegador, você verá uma saudação personalizada que inclui o nome fornecido no URL.

#EXEMPLO 2.2 - hello.py: aplicação Flask com uma rota dinâmica

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, {}</h1>'.format(name)

#Se vocÊ clonou o repositório Git da aplicação no GitHub, poderá agora executar  git checkout 2b  para fazer o chackout dessa versão da aplicação.

