from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/help')
def help():
    return 'Textes for help!'

@app.route("/calc",methods=['GET'])
def calc():
    if request.method == "GET":
        if request.args.get('a') == None:
            a = 0
        else:
            a = int(request.args.get('a'))
        if request.args.get('b') == None:
            b = 0
        else:
            b = int(request.args.get('b'))
        c = a + b

    return f"{a}+{b}={c}"

@app.route("/quiz",methods=['GET'])
def quiz():
    if request.method == "GET":
        if request.args.get('n') == None:
            n = 0
        else:
            n = int(request.args.get('n'))
    # Створюємо список зі структурою
    answer=''
    quiz_arr=[]
    quiz_arr.append({"question_arr":["Яка середня заробітна плата Python-розробника в Україні (червень, 2023)?"],"title_arr":["Зарплата розробника на Python"],"a1_arr":["$1200"],"a2_arr":["$2100"],"a3_arr":["$2700"],"a4_arr":["$3200"],"answer_arr":["$2700"],"n_right_answer_arr":["3"],"total_n":"4"})
    quiz_arr.append({"question_arr":["Яка середня заробітна плата JavaScript-розробника в Україні (червень, 2023)?"],"title_arr":["Зарплата розробника на JacaScript"],"a1_arr":["$1000"],"a2_arr":["$1500"],"a3_arr":["$2000"],"a4_arr":["$2500"],"answer_arr":["$2500"],"n_right_answer_arr":["4"],"total_n":"4"})
    quiz_arr.append({"question_arr":["Яка доля розробників в Україні пише на Python (червень, 2023)?"],"title_arr":["Доля розробників на Python"],"a1_arr":["10,2"],"a2_arr":["13,4"],"a3_arr":["15,2"],"a4_arr":["21,6"],"answer_arr":["13,4"],"n_right_answer_arr":["2"],"total_n":"4"})
    quiz_arr.append({"question_arr":["Яка доля розробників в Україні пише на JavaScript?"],"title_arr":["Доля розробників на JavaScript"],"a1_arr":["10,5"],"a2_arr":["19,1"],"a3_arr":["22,7"],"a4_arr":["32,1"],"answer_arr":["19,1"],"n_right_answer_arr":["2"],"total_n":"4"})


    if n<len(quiz_arr):
        answer = quiz_arr[n]
    else:
        answer="Over"

    return answer    


