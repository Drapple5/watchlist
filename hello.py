from flask import Flask,redirect,url_for,render_template
movies = [
{'title':'Dead Poets Society','year':'1989'},
{'title':'My Neighbor Totoro','year':'1988'},
{'title':'A Perfect World','year':'1933'},
{'title':'Leon','year':'1994'},
{'title':'Mahjong','year':'1996'},
{'title':'Swallowtail Butterfly','year':'1996'},
{'title':'King of Comedy','year':'1999'},
{'title':'Devils on the Doorstep','year':'1999'},
{'title':'WALL-E','year':'2008'},
{'title':'The Pork of Music','year':'2012'},
]
# movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'},
# ]

app = Flask(__name__)
@app.route('/')
def Hello( ):
    return ' <h1>儿童节</h1><p>6.1</p><h2>圣诞节</h2><p>12.25</p><h3>万圣节</h3><p>不知道</p> '

@app.route('/greet')
def greet():
    return 'αβγδεζηθικλμνξοπρστυφχψω'

@app.route('/totoro')
def totoro():
    return'<h1>龙猫</h1><img src="http://Helloflask.com/totoro.gif">'


@app.route('/已注册')
def yizhuce():
    return'<h1>会员你好</h1>'
@app.route('/未注册')
def weizhuce():
    return redirect(url_for('qingzhuce'))
@app.route('/请注册11')
def qingzhuce():
    return'<h1>请输入必要信息</h1>'

@app.route('/user/<int:age>')
def user(age):
    if age<18:
        return "不好意思这儿是个18禁网站"
    if age>=18:
        return "欢迎呀"
@app.route('/<name>')
def index(name):
    return render_template('index.html',name=name,movies=movies)
