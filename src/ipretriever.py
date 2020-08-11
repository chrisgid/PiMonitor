import requests

url = 'https://api.ipify.org'

def getIp():
    r = requests.get(url)

    if (r.status_code == requests.codes.ok):
        return r.content.decode('UTF-8')
    else:
        return 'Unknown'
    

if __name__ == '__main__':
    getIp()