from flask import Flask, render_template, request

# 서버 앱 생성
app = Flask(__name__)

# url 세팅 - 라우터 설정
# @데코레이터 : 함수를 감싼다. 감싼 코드부터 실행되게끔 한다.
@app.route('/')
def index():
    # return "<h1>인덱스 페이지</h1>"
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/framework')
def framework():
    return render_template("framework.html")

@app.route('/form')
def form():
    res = request.args.get('keyword') #args : arguments 입력인자. 매개변수를 입력할 때 사용하는 말
    print(res) #args : arguments 입력인자. 매개변수를 입력할 때 사용하는 말
    return render_template("form.html")

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True) # 서버 가동
