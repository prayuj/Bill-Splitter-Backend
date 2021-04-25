from flask import Flask
from flask import jsonify
from flask import Markup
from flask import jsonify
from flask import request
import json

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST', "GET"])
def test():
    if request.method == 'POST':
        print(request.get_json())
        recieved_dict = request.get_json()
        def getContribution(data):
            contri = {}
            for index in range(len(data['people'])):
                person = data['people'][index]
                contri[person] = 0
                for item in data['items']:
                    item_contribution = item['price']*(item['contri'][index]/100)
                    item_contribution *= (100+float(item['tax'])+float(data['taxes']))/100
                    contri[person]+= item_contribution

                contri[person] = round(contri[person])                     

            return contri
            
        return jsonify(getContribution(recieved_dict))
    else:
        return '<h1>Hello</h1>'
if __name__ == '__main__':
   app.run()


