import unittest
from main import ProcessPayment
import json
import requests

class testclass(unittest.TestCase):

	def test_validation(self):
		data={
            "CreditCardNumber": "112233445566",
            "CardHolder": "mycool",
            "ExpirationDate":"2020-12-12",
            "SecurityCode":'123',
            "Amount":"25.00"
        }
		res = requests.post(url= "http://127.0.0.1:6000/process_payment/",data=data)

		self.assertEqual(200, res.status_code)

	def test_invalid_card_number(self):
		data={
            "CreditCardNumber": "1122334455edfg",
            "CardHolder": "mycool",
            "ExpirationDate":"2020-12-12",
            "SecurityCode":'123',
            "Amount":"25.00"
        }
		res = requests.post(url= "http://127.0.0.1:6000/process_payment/",data=data)

		self.assertEqual(400, res.status_code)

	def test_expiry_date(self):
		data={
            "CreditCardNumber": "1122334455edfg",
            "CardHolder": "mycool",
            "ExpirationDate":"2020-10-10",
            "SecurityCode":'123',
            "Amount":"25.00"
        }
		res = requests.post(url= "http://127.0.0.1:6000/process_payment/",data=data)

		self.assertEqual(400, res.status_code)

	def test_invalid_security_code(self):
		data={
            "CreditCardNumber": "1122334455edfg",
            "CardHolder": "mycool",
            "ExpirationDate":"2020-12-12",
            "SecurityCode":'1234345',
            "Amount":"25.00"
        }
		res = requests.post(url= "http://127.0.0.1:6000/process_payment/",data=data)

		self.assertEqual(400, res.status_code)

	def test_invalid_amount(self):
		data={
            "CreditCardNumber": "1122334455edfg",
            "CardHolder": "mycool",
            "ExpirationDate":"2020-12-12",
            "SecurityCode":'123',
            "Amount":"-25.00"
        }
		res = requests.post(url= "http://127.0.0.1:6000/process_payment/",data=data)

		self.assertEqual(400, res.status_code)



if __name__=="__main__":
	unittest.main()