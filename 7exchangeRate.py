import requests
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter

#cc = CurrencyConverter()
#print(cc.currencies)


cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1, 'USD','KRW'))


#kr.investing.com/currencies/usd-krw을 크롤링하여 사용
def get_exchage_rate(target1, target2) :
    headers = {
        'User-Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text/html; charset=utf-8'
    }

    response = requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test' : 'instrument-price-last'})
    print(containers.text)

#get_exchage_rate('usd','krw')
