#接下来，我们要注册一个处理函数，这个函数是处理某个请求的处理函数，Flask官方把它叫做视图函数（view funciton），你可以理解为“请求处理函数”。
from flask import Flask
app = Flask(__name__)

name = 'Qingzhi Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

from flask import Flask, render_template
# ...
#所谓的“注册”，就是给这个函数戴上一个装饰器帽子。我们使用  app.route()  装饰器来为这个函数绑定对应的 URL，当用户在浏览器访问这个 URL 的时候，就会触发这个函数，获取返回值，并把返回值显示到浏览器窗口：
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)