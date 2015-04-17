import requests
from xml.dom.minidom import parseString


from words import convert

URL = 'https://asr.yandex.net/asr_xml?uuid=01ae13cb744628b58fb536d496daa1e6&key=d6901ba8-5085-4001-b7c2-f92c2964109b&topic=notes&lang=ru-RU'


def call_api_recognize(file):
    files = {'audio': (file.name, file)}
    r = requests.post(URL,
                      files=files,
                      headers={'Content-Type': 'audio/x-mpeg-3'})
    if r.status_code != 200:
        raise Exception(r.text)

    return r.text


def extract_from_xml(xml):
    print xml
    xmldoc = parseString(xml.encode('utf-8'))
    root = xmldoc.firstChild
    success = root.attributes['success'].value

    if success == 0:
        raise Exception("Not recognized")

    for child in root.childNodes:
        if child.nodeName == 'variant':
            return child.firstChild.nodeValue

    return


def process_file(file):
    xml = call_api_recognize(file)
    words = extract_from_xml(xml)
    print words
    print convert(words)
    return convert(words)


f = open('data/5127.mp3', 'rb')
try:
    print process_file(f)
except Exception as e:
    print e.message