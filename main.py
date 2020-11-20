import requests
from flask import Flask
from flask_restful import Api, Resource,reqparse,inputs
from flask import request
from flask import jsonify
import json
from datetime import datetime,date

app = Flask(__name__)
api = Api(app)

class ProcessPayment(Resource) :

	def post(self,) :       
				
		parser = reqparse.RequestParser()
		parser.add_argument('CreditCardNumber',
							type=self.valid_credit_card_number,
							required=True)
						
		parser.add_argument('CardHolder',
							type=str,
							required=True,
							help='This field is required!')
						
		parser.add_argument('ExpirationDate',
							type=self.validate_expirydate,
							required=True)
						
		parser.add_argument('SecurityCode',
							type=self.validate_security_code,
							required=True)
						
		parser.add_argument('Amount',
							type=self.validate_amount,
							required=True)

		data_payload = parser.parse_args()
		amount=float(data_payload['Amount'])
		
		if amount<=20.00:
			print("Use Cheap Payment Gateway ")
			if True:
				try:
					return {"status" : 201, "message" : "Success"}
				except:
					return {"status" : 500, "message" : "Internal Server Error"}
			else:
				try:
					return {"status": 400, "message": "Invalid request"}
				except:
					return {"status" : 500, "message" : "Internal Server Error"}
		elif 500>amount>20 :
			print("Use Expensive Payment Gateway if available or retry once with cheap payment gateway")
			if True:
				try:
					return {"status" : 201, "message" : "Success"}
				except:
					return {"status" : 500, "message" : "Internal Server Error"}
			else:
				try:
					return {"status": 400, "message": "Invalid request"}
				except:
					return {"status" : 500, "message" : "Internal Server Error"}
		else:
			print("retry 3 times with premium payment gateway if not processed")
			if True:
				try:
					return {"status" : 201, "message" : "Success"}
				except:
					return {"status" : 500, "message" : "Internal Server Error"}
			else:
				try:
					return {"status": 400, "message": "Invalid request"}
				except:
					return {"status" : 500, "message" : "Internal Server Error"}
		
						
	def valid_credit_card_number(self,value, name):

		if len(value) == 12 and value.isnumeric():
			return value
		else:
			raise ValueError("The parameter '{}' is not valid. You gave us the value: {}".format(name, value))


	def validate_security_code(self,value,name):

		if len(value) == 3 and value.isnumeric():
			return value
		else:
			raise ValueError("The parameter '{}' is not valid. You gave us the value: {}".format(name, value))

	def validate_amount(self,value,name):

		if float(value)>0:
			return value
		else:
			raise ValueError("The parameter '{}' is not valid. You gave us the value: {}".format(name, value))

		
	def validate_expirydate(self,value,name):

		selected_date=datetime.strptime(value, "%Y-%m-%d").date()
		if selected_date<date.today():
			
			raise ValueError("The parameter '{}' is not valid. You gave us the value: {}".format(name, value))
		else:
			return value
		
		
api.add_resource(ProcessPayment, "/process_payment/")


if __name__ == "__main__" :

	app.run(host="0.0.0.0",debug=False, port=6000)
			


