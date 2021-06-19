from flask import Flask,jsonify,request

app = Flask(__name__)

data=[
    {
        'id':1,
        'name':u'Abhishek',
        'contact': u'9880011446',
        'done': False
    },
    {
        'id':2,
        'name':u'Alka',
        'contact': u'9731218914',
        'done': False
    }
]


@app.route("/add-contact",methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "please provide the data"
        },400)

    contact = {
        'id' : data[-1]['id']+1,
        'title' : request.json['title'],
        'description' : request.json.get('contact',""),
        'done' : False
    }

    data.append(contact)
    return jsonify({
        "status" : "Success !!",
        "message" : "Contact added successfully !!"
    })

@app.route("/get-contact")
def get_contact() :
    return jsonify({
        "data" : data
    })

if (__name__ == "__main__"):
    app.run(debug=True)