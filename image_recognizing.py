import datetime
import pprint
import time
from collections import namedtuple

from document_structure import Model
from threading import Thread
from functools import reduce

import requests
import json

AUTORIZATION_URL = 'https://id.entera.pro/api/v1/login'
MAIN_URL = 'https://app.entera.pro/api/v1/'
LOGIN = 'transit010@mail.ru'
LOGIN = 'dinam@list.ru'
# LOGIN = 'qabba@list.ru '
PASSWORD = '357495'
PASSWORD = '12345678'
# PASSWORD = '762543'
SPACE_ID = '3025bc8d-9e7f-4d63-8567-83fd041b8fa0'
SPACE_ID = 'c20d2182-db9f-43f3-82bc-79d65a5a7f46'
# SPACE_ID = '5d3af6d1-daa1-4bad-8f58-c3cc28ce093c'


class Entera:

    def __init__(self, login: str = LOGIN, password: str = PASSWORD):
        self.login = login
        self.password = password
        self.sess = None
        self.docs = None

    def start(self):
        self.sess = requests.Session()
        headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        data = json.dumps({"login": self.login, "password": self.password})
        res = self.sess.post(AUTORIZATION_URL, data=data, headers=headers)
        return res.text

    # def checking(self, task_id:str):
    #     thread = Thread(target=self._check_task, args=(task_id,))
    #     thread.start()

    def check_task(self, task_id: str):
        suffix = 'recognitionTasks/'

        while True:
            res = self.sess.get(''.join([MAIN_URL, suffix, task_id]))
            task = Model(**res.json())
            state = task.recognitionTask.state
            print(str(datetime.datetime.now()) + " --- " + state)
            if state == 'RECOGNIZED':
                self.docs = task.recognitionTask.documents
                break
            elif state == 'ERROR':
                print('ERROR!')
                break
            time.sleep(20)

        return f"Выполнена задача: {task_id}\n"

    @staticmethod
    def _get_doc_type(doc: str):
        dic = {
            "UTD": "УПД",
            "TORG12": "ТОРГ-12",
            "VAT_INVOICE": "Счёт-фактура",
            "OFFER": "Счёт",
            "CERTIFICATE": "Акт",
            "TTN": "Товарно-транспортная накладная",
            "DELIVERY_ORDER": "Накладная",
            "RECEIPT": "Чек",
            "NONSTANDARD": "Нестандартный",
            "UNKNOWN": "Не поддерживается приложением"}
        return dic.get(doc, None)

    def parse_doc(self):
        doc_items = []
        for item in self.docs[0].items:
            doc_item = namedtuple('Lepeshki', 'name price quantity amount')
            doc_item.name, doc_item.price, doc_item.quantity, doc_item.amount = \
            item.recognizedName, item.recognizedPrice, item.recognizedQuantity, item.recognizedAmount
            doc_items.append(doc_item)

        if self._get_doc_type(self.docs[0].type) and self.docs[0].date:
            header = self._get_doc_type(self.docs[0].type) + ' от ' + self.docs[0].date + '\n'

        count = sum([item.quantity for item in doc_items])
        amount = sum([item.amount for item in doc_items])
        footer = f'ИТОГО: {count} шт. на {amount} руб.'

        txt = ''
        for item in doc_items:
            txt += '--'.join((str(item.name), str(item.price), str(item.quantity), str(item.amount))) + '\n'
        txt = header + txt + footer

        return txt

    def send_photo(self, file_path: str):
        suffix = 'recognitionTasks'
        params = {'spaceId': SPACE_ID}
        files = {'file': open(file_path,'rb')}
        res = self.sess.post(url=''.join([MAIN_URL, suffix]), params=params, files=files)

        with open('last_task_id.txt', 'w', encoding='utf-8') as fil:
            json.dump(json.loads(res.text), fil, indent=4)

        pprint.pprint(json.loads(res.text))
        if res.status_code == 200:
            task = Model(**res.json())
            self.check_task(task.recognitionTask.id)
        else:
            print(res.text)
            return


if __name__ == '__main__':
    entera = Entera()
    entera.start()
    print(entera.check_task('ac4eceda-5742-494d-aabc-7af23572e763'))

    text = entera.parse_doc()

    print(text)


# doc.send_photo('photo_2022-12-11_12-43-55.jpg')

