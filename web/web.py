import requests

res = requests.get('https://jsonmock.hackerrank.com/api/articles?page=1')
data = res.json()
print(data['page'])
print(data['per_page'])
print(data['total'])
print(data['total_pages'])

data_arr = data['data']

for real_data in data_arr:
    # real_data = v.json()
    print(real_data['title'])
    print(real_data['url'])
    print(real_data['author'])
    print(real_data['num_comments'])
    print(real_data['story_id'])
    print(real_data['story_title'])
    print(real_data['story_url'])
    print(real_data['parent_id'])
    print(real_data['created_at'])
    # print(real_data['dfd']) -> 없는 key값이면 keyError가 뜬다.
    print('====================================================================================================')
