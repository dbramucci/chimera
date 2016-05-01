
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])

def ourdata():
    if request.method == 'POST':
        our_data = str(request.data)
        my_list = our_data.split(":")
        print(my_list)

        return str(my_list)




if __name__ == "__main__":
    app.run(debug=True)
