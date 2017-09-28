#coding=utf-8

'a web app demo'

__author__ = "Wilson"


'''
Web应用的本质就是：

-浏览器发送一个HTTP请求；

-服务器收到请求，生成一个HTML文档；

-服务器把HTML文档作为HTTP响应的Body发送给浏览器；

-浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。


最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML


我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI：Web Server Gateway Interface

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：
'''

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello web!</h1>']


'''
Web框架

flask
'''
from flask import Flask
from flask import request

app = Flask(__name__)


#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    #需要从request读取表单内容
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()