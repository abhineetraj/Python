import redis

r = redis.Redis(
    host='ms5stage-redis-001.mpulse.io',
    port=6379, 
    db=5)

r.set('foo', 'bar')
value = r.get('foo')
print(value)
