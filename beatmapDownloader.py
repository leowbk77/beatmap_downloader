'''
    Já faz o serviço
    Pode melhorar usando request assincrono
'''

import requests
from requests.exceptions import HTTPError
import os

def request(beatmap):
    try:
        filename = f'{beatmap}'
        print('======================================')
        print(f'Realizando download do {beatmap}:\n')
        with requests.get(f'https://beatconnect.io/b/{beatmap}', stream=True) as request:
            if request.ok:
                if "content-disposition" in request.headers:
                    content_disposition = request.headers["content-disposition"]
                    filename = content_disposition.split("filename=")[1]
                    filename = filename[1:-2]
                with open(filename, 'wb') as file:
                    for chunk in request.iter_content(chunk_size=10 * 1024):
                        file.write(chunk)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'Beatmap: {filename} downloaded')

def find_beatmaps(folder):
    dirList = os.listdir(folder)
    beatmaps = []
    for dir in dirList:
        name = dir.split()
        beatmaps.append(name[0])
    return beatmaps

def save_list(beatmaps):
    with open('list.txt', 'wt') as listFile:
        listFile.write('\n'.join(beatmaps))

def read_from(list):
    beatIdList = []
    with open(list, 'r') as listFile:
        for beatID in listFile:
            beatIdList.append(beatID)
    return beatIdList

def fix(list):
    fixedList = []
    with open(list, 'r') as listFile:
        for beatmap in listFile:
            beatId = beatmap.split()
            fixedList.append(beatId[0])
    with open('fixedList.txt', 'wt') as fixedListFile:
        fixedListFile.write('\n'.join(fixedList))
    return 'done!'

def menu():
    print('building!')

# download
beatmaps = find_beatmaps(".\Songs")
for beatmap in beatmaps:
    request(beatmap)
print('download concluido.')

''' SALVAR A LISTA
save_list(beatmaps)
'''
''' FIX LISTA
print(fix('lista.txt'))
'''