from flask import Flask, render_template, jsonify, request
import sys
import processor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())
    #return render_template('hello', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']
        print(the_question, file=sys.stderr)

        response = processor.chatbot_response(the_question)
        print(response, file=sys.stdout)

    return jsonify({"response": response })



if __name__ == '__main__':
    #app.run(host='0.0.0.0', port='5000', debug=True)
    app.run(host="0.0.0.0")



