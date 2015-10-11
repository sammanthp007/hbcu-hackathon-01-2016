from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib2
import requests

 


# Create your views here.
_PAYER_ID = '560f0207f8d8770df0efa643'
#{u'rewards': 31593, u'customer_id': u'560f0205f8d8770df0ef9a99', u'type': u'Checking', u'_id': u'560f0207f8d8770df0efa643', u'balance': 11633, u'nickname': u"Dr.'s Account"}
reimagine_api_key = 'key=73773e58efaba48db97f6f32c3f89f51'
all_clients_api = 'http://api.reimaginebanking.com/accounts?'
transfer_api = 'http://api.reimaginebanking.com/accounts/%s/transfers?'
user_name = '277roshan'


def index_view(request):
	return render(request, 'gringotts/base.html',{"key":"73773e58efaba48db97f6f32c3f89f51"})


def all_clients_view(request):
	page = urllib2.urlopen(all_clients_api + reimagine_api_key) 
	page = page.read()
	page = json.loads(page.decode())
	print (page)
	return HttpResponse(page)
	# return render(request, 'gringotts/index.html', {'items' : page[0]})


def transfer(request):
	if request.POST:
		payee_id = request.POST['id']
		amount = int(request.POST['money'])
		

		payload = {
		"medium":"balance",
		"amount":amount,
		"payee_id":payee_id,
		}
		url = 'http://api.reimaginebanking.com/accounts/%s/transfers?%s'%(_PAYER_ID, reimagine_api_key)
		#url = 'http://api.reimaginebanking.com/customers/{}/accounts?{}'.format(person_id,reimagine_api_key)	
		response = requests.post( 
			url, 
			data=json.dumps(payload),
			headers={'content-type':'application/json'},
			)
		if response.status_code == 201:
			print True
			print('transferred')
			transfers_url = 'http://api.reimaginebanking.com/accounts/%s/transfers?%s'%(_PAYER_ID, reimagine_api_key)
			page = urllib2.urlopen(transfers_url) 
			page = page.read()
			page = json.loads(page.decode())
			payee = urllib2.urlopen('http://api.reimaginebanking.com/accounts?key=73773e58efaba48db97f6f32c3f89f51') 
			payee = payee.read()
			payee = json.loads(payee.decode())

	
			payee_dict = {}
			for i in payee:
				payee_dict[i['_id']] = i['nickname']
			
			print payee_dict
		
			payee_pass_list= []
			for i in page:
				payee_pass_list.append((i["payee_id"],i["amount"]))
			
			print payee_pass_list
			final_list=[]
			for i in payee_pass_list:
				final_list.append((payee_dict[i[0]],i[1]))
			print final_list
			final_list = final_list[-1::-1]


			page = urllib2.urlopen(all_clients_api + reimagine_api_key) 
			page = page.read()
			page = json.loads(page.decode())
			for i in page:
			
			return render(request, 'gringotts/base.html',{"payee_pass_list":final_list,"balance":balance_list})
			
			
		else:
			print 'Not yet'
	pass

		


# http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
# page = urllib2.urlopen(data)
# page_read = page.read()
# page = json.loads(page_read)
#http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
