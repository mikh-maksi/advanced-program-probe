@app.route("/quiz",methods=['GET'])
def quiz():
    if request.method == "GET":
        if request.args.get('n') == None:
            n = 0
        else:
            n = int(request.args.get('n'))
    # Створюємо пустий список
    answer=''
    quiz_arr=[]
    quiz_arr.append("Питання 1")
    quiz_arr.append("Питання 2")
    quiz_arr.append("Питання 3")
    quiz_arr.append("Питання 4")

    if n<len(quiz_arr):
        answer = quiz_arr[n]
    else:
        answer="Over"

    return answer    