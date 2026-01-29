from flask import Flask, jsonify
app = Flask(__name__)
members = [
    {"name": "maryann","days_left": 10},
    {"name": "john","days_left": 8},
    {"name": "marion","days_left": -6},
]
def get_members():
    results=[]
    for member in members:
        if member["days_left"] >0:
           status = "active"
    else:
        status = "expired"
        results.append({
            "name": member["name"],
            "status": status
        })   

    return jsonfy(results) 
if __name__=="__main__":
    app.run(debug=True) 

