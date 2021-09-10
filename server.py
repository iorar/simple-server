from flask import Flask,jsonify,make_response,abort,request,render_template
import os


# 初期設定
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


# API実装
@app.route('/getData/', methods=['GET'])
def get_Weather():

    greeting = "Hello, Internet!"

    return make_response(greeting)

# 初期ページ
@app.route('/')
def index():
    # トップページを表示
    return render_template('index.html')

# サービス起動
if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)