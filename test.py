import requests

print(requests.get('http://127.0.0.1/api/jobs'))
print(requests.get('http://127.0.0.1/api/jobs/1'))
print(requests.get('http://127.0.0.1/api/jobs/-1'))
print(requests.get('http://127.0.0.1/api/jobs/ss'))
# 200
print(requests.delete('http://127.0.0.1/api/jobs/3'))
# 400
print(requests.delete('http://127.0.0.1/api/jobs/ss'))
# 404
print(requests.delete('http://127.0.0.1/api/jobs/1'))
