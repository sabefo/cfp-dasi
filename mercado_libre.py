# coding=utf-8
import json
import pprint
import sys
sys.path.append('lib/')
from meli import Meli


class MercadoLibre():
    CLIENT_ID = 133597087
    TOKEN = "APP_USR-2376600932706705-032210-65f8df0830c4c8fec5bf30c42c479f6e-133597087"

    def __init__(self):
        super(MercadoLibre, self).__init__()
        self.meli = Meli(client_id=self.CLIENT_ID, client_secret="el secreto", access_token=self.TOKEN, refresh_token=self.TOKEN)
        params = {'access_token': self.meli.access_token}

    def searchProduct(self, query):
        path = "sites/MLU/search?q=" + query
        response = self.meli.get(path=path)

        products = json.loads(response.content)
        usd_products = [i for i in products['results'] if i['currency_id'] == 'USD']
        return usd_products

    def formatJSON(self, json):
        products = []
        for i in range(0, len(json)):
            productJSON = {}
            productJSON['link'] = json[i]['permalink']
            productJSON['price'] = json[i]['price']
            productJSON['reviews'] = json[i]['reviews']
            productJSON['photo'] = json[i]['thumbnail']
            productJSON['title'] = json[i]['title']
            products.append(productJSON)
        return products