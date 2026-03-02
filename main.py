from flask import Flask, url_for

app = Flask(__name__)
text = """Человечество вырастает из детства.

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!""".split('\n')


@app.route('/')
def g():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    a = [str(i) for i in text]
    return '</br>'.join(a)


@app.route('/image_mars')
def image_mars():
    return f'''
           <h1>Жди нас, Марс!</h1>
           <img src="{url_for('static', filename='img/MARS.png')}"
           alt="здесь должна была быть картинка, но не нашлась">
           <h5>Вот она какая, красная планета.</h5>'''


@app.route('/choice/<choicePlanet>')
def choice(choicePlanet):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <h1>Мое предложение: {choicePlanet}</h1>
                    <h5>Эта планета близка к земле;</h5>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-success" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                    <div class="alert alert-primary" role="alert">
                    На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-warning" role="alert">
                    На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-dark" role="alert">
                    На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-danger" role="alert">
                    Наконец, она просто красива!
                    </div>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
          <link rel="stylesheet" href="static/css/style.css">
           <h1>Жди нас, Марс!</h1>
           <img src="{url_for('static', filename='img/MARS.png')}"
           
           alt="здесь должна была быть картинка, но не нашлась">
           <div class="alert alert-success" role="alert">
                      Человечество вырастет из из детства.
                    </div>
                    <div class="alert alert-primary" role="alert">
                    Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-warning" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-dark" role="alert">
                    И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                    Присоединяйся!
                    </div>
        '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
