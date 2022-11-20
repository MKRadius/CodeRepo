#Exercise 13.1
from flask import Flask, Response
from math import sqrt
import json

app = Flask(__name__)
@app.route("/prime_number/<number>")

def prime_number(number):
    try:

        inputNumber = int(number)
        primeStatus = True

        if (inputNumber == 0 or inputNumber == 1) or (inputNumber < 0):
            response = {
                "Number": inputNumber,
                "isPrime": False
            }
        else: 
            for i in range(2, int(sqrt(inputNumber)) + 1):
                if inputNumber % i == 0:
                    primeStatus = False
                    break

            response = {
                "Number": inputNumber,
                "isPrime": primeStatus
            }

        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")

        return http_response

    except ValueError:
        response = {
            "message": "Invalid number",
            "status": 400
        }
        
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")

        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }

    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")

    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
    


#Exercise 13.2
import mysql.connector
from flask import Flask, Response
import json


connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

app = Flask(__name__)

@app.route("/airport/<icao_code>")
def airport(icao_code):
    try:
        sql = "select name, municipality from airport where ident ='" + icao_code + "'"

        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        response = {
            "ICAO": icao_code,
            "Name": result[0][0],
            "Location": result[0][1]
        }

        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")

        return http_response
    except:
        response = {
            "message": "Invalid ICAO code",
            "status": 400
        }

        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")

        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }

    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=400, mimetype="application/json")

    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
