# 딕셔너리는 키를 이용해 데이터에 접근
# 아래에서는 age와 address가 key
user = {}
user['age'] = 25
user['address'] = 'seoul'

print(user)
print(user['age'])
print(user.get('age')) # 키가 없어도 에러가 생기지 않아 권장한다.
user['age'] = 90
print(user.get('age'))