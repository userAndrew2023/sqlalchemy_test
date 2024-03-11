import requests

print(requests.get('http://127.0.0.1/api/jobs').json())
print(requests.get('http://127.0.0.1/api/jobs/1').json())
print(requests.get('http://127.0.0.1/api/jobs/-1').json())
print(requests.get('http://127.0.0.1/api/jobs/ss').json())
# 200
print(requests.delete('http://127.0.0.1/api/jobs/3').json())
# 400
print(requests.delete('http://127.0.0.1/api/jobs/ss').json())
# 404
print(requests.delete('http://127.0.0.1/api/jobs/1').json())
