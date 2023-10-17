import requests


response = requests.get('https://www.naver.com') # 웹사이트에 리퀘스트를 보냄. 리퀘스트의 결과가 response에 저장

print(response)
print(response.status_code) # 응답 코드 보여주기 200이면 성공!
print(response.text) # 응답 결과를 텍스트로 보여줌.