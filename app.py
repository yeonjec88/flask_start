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

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == "GET": #GET방식 요청일 땐
        return render_template("form.html")
    elif request.method == "POST":#POST방식 요청일 땐
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')

        if num1 and num2:
            total = float(num1) + float(num2)
            print(total)
            data = {'num1': num1,'num2': num2, 'total': total}
            return render_template("form.html", data=data)

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True) # 서버 가동
