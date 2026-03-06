import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # 隨機選擇正面或反面
        result = random.choice(['正面', '反面'])
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)