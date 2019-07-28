import redis


r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.set('name', 'chenpeiyuan')
print(r.get('name'))

r.hset('dic_name', 'a1', 'sdf')
r.hset('dic_name', 'a1', 2)
r.hset('dic_name', 'b1', 'b2')
print(r.hvals('dic_name'))

r.lpush('list_name', 8, 9, 10)
print(r.llen('list_name'))

r.sadd('set_name', 'aa', 'bb')
print(r.smembers('set_name'))

r.zadd('zset_name', {'a1': 10, 'b2': 5})

