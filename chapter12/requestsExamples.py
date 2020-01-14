import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type(res)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem getting your url contents %s' % (exc))

## best way to check response status 200 using .ok use that at work
res.status_code == requests.codes.ok

len(res.text)

print(res.text[:250])


res2 = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status()
except Exception as exc:
    print(' had an error downloading file %s' % (exc))



playFile = open('RomeoAndJuliet.txt', 'wb')
#### iter_content returns chunks of the content that is in the res object to write to the file in bytes
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
