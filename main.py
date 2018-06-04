# -*- coding: utf-8 -*-
import sys
import requests

sansan_api_key = '{your_sansan_api_key}'
hubspot_api_key = '{your_hubspot_api_key}'

def get_cards():
    url = 'https://api.sansan.com/v1.2/bizCards/'
    headers = { 'X-Sansan-Api-Key' : sansan_api_key }

    payload = { 'registeredFrom' : '2018-05-01T00:00:00+09:00',
                'registeredTo' : '2018-05-10T00:00:00+09:00' }

    r = requests.get(url, headers=headers, params=payload)
    return r.json().get('data', [])


def sync_to_hubspot(email, record):
    url = f"https://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/{email}/?hapikey={hubspot_api_key}"

    obj = {
        'properties' : [
            {
              "property": "lastname",
              "value": record.get('lastName')
            },
            {
              "property": "firstname",
              "value": record.get('firstName')
            },
            {
              "property": "company",
              "value": record.get('companyName')
            },
            {
              "property": "phone",
              "value": record.get('tel')
            }
        ]
    }

    r = requests.post(url, json=obj)
    print(r)


def get():
    data = get_cards()
    print(data)


def sync():
    data = get_cards()

    for record in data:
        sync_to_hubspot(record.get('email'), record)


if __name__ == "__main__":
    func = sys.argv[1]
    eval(func)()
