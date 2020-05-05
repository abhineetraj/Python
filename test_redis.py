import redis

r = redis.Redis(
    host='google-redis-001.mpulse.io',
    port=6379, 
    db=6)

r.set('foo', 'bar')
value = r.get('foo')
print(value)
