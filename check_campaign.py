import requests
import json
import pickle
import time
from datetime import datetime
import logging


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def update_tokens(accounts, refresh):
    tokens = []
    header = {'Host': 'target.my.com', 'Content-Type': 'application/x-www-form-urlencoded'}
    account = ['dBp0GGsdn2khbLCk','Gcwd3JCrhpkj8DQn','cCV7EfBVutwh1yzn','iVTXNguDBEhyR2G0','STBDrKKowc1aVQ1M','n5zvIiexebHHazsF']
    for ids in account:
        access_token_req = {
            "client_id": str(ids),
            "client_secret": str(accounts[ids]),
            "refresh_token": str(refresh[ids]),
            "grant_type": "refresh_token"
        }

        response = requests.post('https://target.my.com/api/v2/oauth2/token.json', data=access_token_req, headers=header)
        print(response.json())
        logging.info(str(response.json()))
        tokens.append(response.json()['access_token'])
    return tokens


today_time = datetime.today()
logging.basicConfig(filename="logs/sample.log", level=logging.INFO)


accounts = {'dBp0GGsdn2khbLCk': '9Ne68rhbu4e2TYuJHGlbDAAPNlOB75LfA4bJomJTy73Pbl9gDAoskXjjG81l2YPqDrVI4db7bD5vDzVc9pVoilel3JryZQl34VQCJcQWwXtXixoSKOLCGVMyppIOFCHCgAxblsXzJQcMJU7qyPgoH07kyhd7JU36WMMog6jGjoYrSsbMuz0GdYtDrv6W3lUtRGUYbxHVGP7MyqvyLjzTDbG3g5Fj6kUTofHfkocofMSRdbcTXnA',
            'Gcwd3JCrhpkj8DQn': '662kHNbGcUcUaRIXC5d0YnKylHfjb8oF9DSox7TEM3EciQ8CIMrmJrYWxZBYxriiPSpKsmMH99sc1PhZgOwmI6DWOvmWIzdd1Sqh0Yjj8nLyZqSGYmTLnG3qx1XbLBwbBq7uqzq6FVbfwbHWAfuwXRtIy9gfCiPAfX3wLcKvHwwwPHOxL992zq0mjbBK7Vs5PnQdT6FV60r9a5tZx4m3b1ehMx',
            'cCV7EfBVutwh1yzn': 'bhYXxt9RE2tsuzsDoEfCIhPzRJ4j4NEycbqvYMMINXP498p6hRxgZCVjc8lcHKETXS00PCIqb7sZCdAp27sI6tBwBQXxjCIEo78PArnf6JIN1SGUrWbuIpFKpCftkPL8o3JnpUG0qa2nUC00TqHX5ncZ305oRh7z6Opspe7QVAoWRoOE8a2zw8xjZmw7zIPIQ9bB2IGDrwuI84DsQLeygzi0zY0p6a9zeAmXe6Q5slV7KO6tLtH',
            'iVTXNguDBEhyR2G0': '1glZFtlmGyBlqecZ0XgVXvCq9u8sPKmV7N7j9Ry2mbRUiRNQTmwhP78wbYS8IqgIceplp6SmZWuYSFJLtSx24D2cSYMlCA9FICaKliz46ZsM1DoEwmgTGQOUV1W0bXzBPtrKtfbslHq30YavbqqxiLv907cGoxm7qSIT5J934h1sE2dmlLgXFlzuKaC4xEimHloXhBrOwO5atJede1HwI8',
            'STBDrKKowc1aVQ1M': 'dH2305LdNFVT45oz56akxP5wavQLQBLMu25UQyOn59myfy48FT9kgNNUX5JHY0KbAEu4d5excWtab9zjZU9qsOLJuTOKpYYmRe58XcWnAT8fJF3iGrBt2n93rybe4MUQVfxhGSRRmuO0GRoaDKd76eH4EXvp7GoXwf9LcnWVGUTyxu7C38EuysrOjQXdFkGqeGpQdmXvmLF6CX3dGWatq4QJaxUipYCptOQxJe737fzCJg2xOI',
            'n5zvIiexebHHazsF': 'NoETjJTbsmAyE752NUakv2bpExZii88W2U1wddWPywayBcj2sjDVMr4fzFyvY87HxWtt7tJMoUNPY6K6aI2U3PjjROJRisTbzQMbfLiogsuN70631Bb3VoBxsIbUIroICpPCAJBfJ1aGijYianGKfzVuwLDn1esiTFntX5Gm0dWPA6XjYenpCXfrMrLbONcU8I2MEDTg5mGzPsQgpdMekjA5gLtHSfxJokhoN8'}

refresh = {'dBp0GGsdn2khbLCk': '3leyQ3sJXj2cHzyXNegMnh6OMq1yJ9qWJn0MAPKLjlyTHmXq6xPhwKpVUFpEP58Y6LTf1HWdX4RRIb7ppCN0gbljadZUTSGBeWamd4B60Z8I2XVbQhYRMrYosAHIjlRnD6QAdVw2egHbpudLGLWpRCQkn9rZDZqcvUiHgdvQQcG6S3ORBFoNNBLIJp1o91oHpUYSx9kHCXfunp6BzCz7IvvTN0thU',
           'Gcwd3JCrhpkj8DQn': 'cn5qkCDOUrxhTJc4HJ2d3INW7cJXV24RLQPBtyif8MdZV86Zb0q3CEJB8KZ7WawY3f7uuiLOz2uvimebDSlCObA2quRmavEcyk9poOGh5eGh0Ux0H7BgQthaUP77NIa2O7QcG54Q7TUD9SoXmOOUTfbplB3LxToSvvUACoqZbk0S8hxL9aQPbmWCn9WEGCaCcT6j2h33elfnpPnNbB',
           'cCV7EfBVutwh1yzn': 'QgBD3s0ov4JF2nQalwmzcOAaej2gLEXWrbmZFByM6TkRTiYOFkeLJDFtuuobY7pVmvJZi7UTtSubLPyEIy8fUW0YgpN5ysEWzc3Qg7jPD9jw05bHYhyhrHIzVOgi58grlLFAYiw6p21cSYy8fjZuMOa8TmkwyYLqNQuGrrKs4sv44TixQ64RgqdG5KCUdYFPOR4F09ISmmA28Kg1vwUNr4Wlx1SpEGy9L4pSw6jPhhJoEIKgQiqLtdkYHyDA',
           'iVTXNguDBEhyR2G0': 'F2lymTLBRZS8RB5mWPj9QIKI5t1nY59vZXOwrKDkLOeQUUArhX7Nq5jUvig8qnXFPN3FPVS8P79wR7elzxsSMTR0bRPBWeU30Iaj5s712ceJJrEfgtDCZDRMhrL2Jx74KIV0X0jKNahLbGmvv9gxDjE0VK5lOPQL8MggUyvWaUGlIl1DlRnrJV9x2mBmMt742rCKjnY0xWRl2TgWm4fWXGdkYnkOzOhxldT2OyY7S',
           'STBDrKKowc1aVQ1M': 'CPhHyYJWN53nkXJDpsWAcWgncNY001Jzo2lcx0whC99TMCJHOudIToDa7H1XdjDOKRDarJlPeGrvL8sXs99n1pZwNGs0atWJzEr8wWK3eKBe1U9mVNvVKlchjdP5JQumg2LXGzZod1eC4YuB0349k3w3yHlxaHhCYQ33cCHDokPS425xqoDIDHe23sv073t6l19d3rLHR5QSgmgCnaN9b0EVpCo',
           'n5zvIiexebHHazsF': 'yDsvvP2PmUmvqHGcqUyvfoH3C18GgU5lu1qXB7Fn65YoqV5dCdqnwwPQvXvDc5crvzTfLLaO9NKWI3hHmEwXHn5O6XboKFNsnlVvNkWZF6Y0t23DbpKYwRPDUL26dQldohZmavmgEGVvlBmBlAcyXYE0MZABhoQnVj2JdhQXjnyRLYUvsDr1Wmv3qeySd57C7IC4kjxJHEBezWA7SS76sFo6j9g5I7TH2FEy'}

accounts_tokens = update_tokens(accounts, refresh)

clients = [[], [], [], [], [], []]

for token in range(len(accounts_tokens)):
    header = {'Host': 'target.my.com', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip,deflate,compress',
              'Authorization': 'Bearer '+str(accounts_tokens[token])}
    get_clients = requests.get('https://target.my.com/api/v1/clients.json', headers=header)
    for i in range(len(get_clients.json())):
        clients[token].append(get_clients.json()[i]['username'])


def update_client_tokens(ids_mail, mail_refresh):
    tokens = []
    header = {'Host': 'target.my.com', 'Content-Type': 'application/x-www-form-urlencoded'}
    for ids in ids_mail:
        for j in range(len(ids_mail[ids])):
            access_token_req = {
                "client_id": str(ids),
                "client_secret": str(accounts[ids]),
                "refresh_token": str(mail_refresh[ids_mail[ids][j]]),
                "grant_type": "refresh_token"
            }
            response = requests.post('https://target.my.com/api/v2/oauth2/token.json', data=access_token_req,
                                     headers=header)
            print(response.json())
            logging.info(str(response.json()))
            tokens.append(response.json()['access_token'])
    return tokens


ids_mail = load_obj("ids_mail")
mail_refresh = load_obj("mail_refresh")


def create_client_tokens(client_name, new_client):
    cl_tkn = []
    header = {'Host': 'target.my.com', 'Content-Type': 'application/x-www-form-urlencoded'}
    for client in new_client:
        access_token_req = {
            "client_id": str(client_name),
            "client_secret": str(accounts[client_name]),
            "agency_client_name": str(client),
            "grant_type": "agency_client_credentials"
        }
        response = requests.post('https://target.my.com/api/v2/oauth2/token.json', data=access_token_req, headers=header)
        print(response.json())
        logging.info(str(response.json()))
        cl_tkn.append(response.json()['refresh_token'])
    return cl_tkn


print(clients[5])


if clients[5] == ids_mail['n5zvIiexebHHazsF']:
    print("Client n5zvIiexebHHazsF is OK")
    logging.info("Client n5zvIiexebHHazsF is OK")
else:
    print("Client n5zvIiexebHHazsF is NOT OK")
    logging.info("Client n5zvIiexebHHazsF is NOT OK")
    new_client = []
    for elem in clients[5]:
        if elem not in ids_mail['n5zvIiexebHHazsF']:
            new_client.append(elem)
    ids_mail['n5zvIiexebHHazsF'] = clients[5]
    save_obj(ids_mail, 'ids_mail')
    refreshers = create_client_tokens('n5zvIiexebHHazsF', new_client)
    for i in range(len(new_client)):
        mail_refresh[new_client[i]] = refreshers[i]
    save_obj(mail_refresh, 'mail_refresh')
    ids_mail = load_obj("ids_mail")
    mail_refresh = load_obj("mail_refresh")


print(clients[4])


if clients[4] == ids_mail['STBDrKKowc1aVQ1M']:
    print("Client STBDrKKowc1aVQ1M is OK")
    logging.info("Client STBDrKKowc1aVQ1M is OK")
else:
    print("Client STBDrKKowc1aVQ1M is NOT OK")
    logging.info("Client STBDrKKowc1aVQ1M is NOT OK")
    new_client = []
    for elem in clients[4]:
        if elem not in ids_mail['STBDrKKowc1aVQ1M']:
            new_client.append(elem)
    ids_mail['STBDrKKowc1aVQ1M'] = clients[4]
    save_obj(ids_mail, 'ids_mail')
    refreshers = create_client_tokens('STBDrKKowc1aVQ1M', new_client)
    for i in range(len(new_client)):
        mail_refresh[new_client[i]] = refreshers[i]
    save_obj(mail_refresh, 'mail_refresh')
    ids_mail = load_obj("ids_mail")
    mail_refresh = load_obj("mail_refresh")


print(clients[3])


if clients[3] == ids_mail['iVTXNguDBEhyR2G0']:
    print("Client iVTXNguDBEhyR2G0 is OK")
    logging.info("Client iVTXNguDBEhyR2G0 is OK")
else:
    print("Client iVTXNguDBEhyR2G0 is NOT OK")
    logging.info("Client iVTXNguDBEhyR2G0 is NOT OK")
    new_client = []
    for elem in clients[3]:
        if elem not in ids_mail['iVTXNguDBEhyR2G0']:
            new_client.append(elem)
    ids_mail['iVTXNguDBEhyR2G0'] = clients[3]
    save_obj(ids_mail, 'ids_mail')
    refreshers = create_client_tokens('iVTXNguDBEhyR2G0', new_client)
    for i in range(len(new_client)):
        mail_refresh[new_client[i]] = refreshers[i]
    save_obj(mail_refresh, 'mail_refresh')
    ids_mail = load_obj("ids_mail")
    mail_refresh = load_obj("mail_refresh")


print(clients[2])


if clients[2] == ids_mail['cCV7EfBVutwh1yzn']:
    print("Client cCV7EfBVutwh1yzn is OK")
    logging.info("Client cCV7EfBVutwh1yzn is OK")
else:
    print("Client cCV7EfBVutwh1yzn is NOT OK")
    logging.info("Client cCV7EfBVutwh1yzn is NOT OK")
    new_client = []
    for elem in clients[2]:
        if elem not in ids_mail['cCV7EfBVutwh1yzn']:
            new_client.append(elem)
    ids_mail['cCV7EfBVutwh1yzn'] = clients[2]
    save_obj(ids_mail, 'ids_mail')
    refreshers = create_client_tokens('cCV7EfBVutwh1yzn', new_client)
    for i in range(len(new_client)):
        mail_refresh[new_client[i]] = refreshers[i]
    save_obj(mail_refresh, 'mail_refresh')
    ids_mail = load_obj("ids_mail")
    mail_refresh = load_obj("mail_refresh")


print(clients[1])


if clients[1] == ids_mail['Gcwd3JCrhpkj8DQn']:
    print("Client Gcwd3JCrhpkj8DQn is OK")
    logging.info("Client Gcwd3JCrhpkj8DQn is OK")
else:
    print("Client Gcwd3JCrhpkj8DQn is NOT OK")
    logging.info("Client Gcwd3JCrhpkj8DQn is NOT OK")
    new_client = []
    for elem in clients[1]:
        if elem not in ids_mail['Gcwd3JCrhpkj8DQn']:
            new_client.append(elem)
    ids_mail['Gcwd3JCrhpkj8DQn'] = clients[1]
    save_obj(ids_mail, 'ids_mail')
    refreshers = create_client_tokens('Gcwd3JCrhpkj8DQn', new_client)
    for i in range(len(new_client)):
        mail_refresh[new_client[i]] = refreshers[i]
    save_obj(mail_refresh, 'mail_refresh')
    ids_mail = load_obj("ids_mail")
    mail_refresh = load_obj("mail_refresh")


print(clients[0])


if clients[0] == ids_mail['dBp0GGsdn2khbLCk']:
    print("Client dBp0GGsdn2khbLCk is OK")
    logging.info("Client dBp0GGsdn2khbLCk is OK")
else:
    print("Client dBp0GGsdn2khbLCk is NOT OK")
    logging.info("Client dBp0GGsdn2khbLCk is NOT OK")
    new_client = []
    for elem in clients[0]:
        if elem not in ids_mail['dBp0GGsdn2khbLCk']:
            new_client.append(elem)
    ids_mail['dBp0GGsdn2khbLCk'] = clients[0]
    save_obj(ids_mail, 'ids_mail')
    refreshers = create_client_tokens('dBp0GGsdn2khbLCk', new_client)
    for i in range(len(new_client)):
        mail_refresh[new_client[i]] = refreshers[i]
    save_obj(mail_refresh, 'mail_refresh')
    ids_mail = load_obj("ids_mail")
    mail_refresh = load_obj("mail_refresh")


clients_accounts = {}
clients_refresh = {}
tokens = update_client_tokens(ids_mail,mail_refresh)

proxies = {
    'http': '154.117.191.114:60028',
    'https': '154.117.191.114:60028',
}


for token in tokens:
    header = {'Host': 'target.my.com', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip,deflate,compress',
              'Authorization': 'Bearer '+str(token)}
    response = requests.get('https://target.my.com/api/v1/campaigns.json', headers=header)
    campaigns = response.json()
    campaigns = sorted(campaigns, key=lambda x: x['status'])
    for i in range(len(campaigns)):
        print(len(campaigns))
        logging.info(len(campaigns))
        if str(campaigns[i]['status']) == 'active':
            date2_str = datetime.today().strftime("%d.%m.%Y")
            date2 = datetime.strptime(date2_str, '%d.%m.%Y')
            date1_str = ''
            date_list = str(campaigns[i]['created']).split('-')
            date_list[2] = date_list[2][0:2]
            date_list[2] = date_list[2] + "."
            date_list[1] = date_list[1] + "."
            date_list.reverse()
            for word in date_list:
                date1_str += word
            date1 = datetime.strptime(str(date1_str), '%d.%m.%Y')
            if (date2-date1).days <= 15:
                print("sleeping")
                logging.info("sleeping")
                time.sleep(30)
                response1 = requests.get('https://target.my.com/api/v1/campaigns/'+str(campaigns[i]['id'])+'.json',
                                         headers=header)
                print(response1.json())
                campaign = response1.json()
                if str(campaign['date_end']) == '' or str(campaign['budget_limit']) == '' or str(campaign['budget_limit']) == 0:
                    data = {'name': str('CHECK_')+str(campaign['name'].encode('utf-8')), 'status': 'blocked'}
                    edit_coms = requests.post('https://target.my.com/api/v1/campaigns/' + str(campaigns[i]['id'])
                                              + '.json', data=json.dumps(data), headers=header)
                    print(edit_coms.json())
                    telegram_chat = requests.post("https://api.telegram.org/bot759523145:AAEKxCONmNdMfsWBWAusKTvOsw_DB2Ok86M/sendMessage?chat_id=-1001478926327&text=" + str('CHECK_') + str(campaign['name'].encode('utf-8')), proxies=proxies)
                    telegram_me = requests.post("https://api.telegram.org/bot759523145:AAEKxCONmNdMfsWBWAusKTvOsw_DB2Ok86M/sendMessage?chat_id=195831781&text=" + str('CHECK_') + str(campaign['name'].encode('utf-8')), proxies=proxies)
                else:
                    print('campaign is OK')
                    logging.info('campaign is OK')

            else:
                print("more than 14")
                logging.info("more than 14")

        else:
            print(campaigns)
            logging.info(str(campaigns))
            print("Not active")
            logging.info("Not active")
            print('NEXT')
            logging.info('NEXT')
            break


print('started in' + str(today_time))
logging.info('started in' + str(today_time))
print('ended in (on next line)')
print(datetime.today())
logging.info('ended in ' + str(datetime.today()))

# 12:48
# 14:51

'''
started in 15:00
ended in (on next line)
2019-01-10 16:55:32.323252
'''

'''
started in 12:50
ended in (on next line)
2019-01-11 14:29:46.280032
'''