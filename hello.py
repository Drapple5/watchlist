from flask import Flask,redirect,url_for
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
#http://localhost:5000/%E8%AF%B7%E6%B3%A8%E5%86%8C11111
