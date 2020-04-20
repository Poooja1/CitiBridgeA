from django.shortcuts import render

def home(request):
	import requests
	import json
	try:
		url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"

		querystring = {"region":"IN","lang":"en","symbols":"HDFCBANK.NS%2CHDFCBANK.BO%2CASIANPAINT.NS%2CASIANPAINT.BO%2CINFY.NS%2CINFY.BO%2CRELIANCE.NS%2CRELIANCE.BO%2CADANIPORTS.NS%2CADANIPORTS.BO%2CAXISBANK.NS%2CAXISBANK.BO"}


		headers = {
		'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
		'x-rapidapi-key': "d0a1ba6076mshd0c6e42ebaac929p13a2a7jsn121693117d09"
		}






		response = json.loads((requests.request("GET", url, headers=headers, params=querystring)).content)
		

	except Exception as e:
		response="Error"

	return render(request,'home.html',{'api': response})
	# return render(request,'home.html',{})

def about(request):
	return render(request,'about.html',{})


