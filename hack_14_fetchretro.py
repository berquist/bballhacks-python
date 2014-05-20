import requests

baseurl = "http://www.retrosheet.org/"

for year in range(60, 92+1):
    for league in ["al", "nl"]:
        filename = ''.join(['19', str(year), league, '.zip'])
        url = ''.join([baseurl, '19', str(year), '/19', str(year), league, '.zip'])
        print("fetching {}\n".format(filename))
        req = requests.get(url)
        fh = open(filename, 'wb')
        fh.write(req.content)
        fh.close()      

league = "ml"
for year in range(00, 04+1):
    filename = ''.join(['200', str(year), league, '.zip'])
    url = ''.join([baseurl, '200', str(year), '/200', str(year), league, '.zip'])
    print("fetching {}\n".format(filename))
    req = requests.get(url)
    fh = open(filename, 'wb')
    fh.write(req.content)
    fh.close()
