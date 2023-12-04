# import redis
# from redis.sentinel import Sentinel
# sentinel = Sentinel([('10.0.1.230', 26379),
#                      ('10.0.1.209',26379),
#                      ('10.0.1.56',26379)],
#                    sentinel_kwargs={'password': 'test@123'},
#                    socket_timeout=0.1)
# # you will need to handle yourself the connection to pass again the password
# # and avoid AuthenticationError at redis queries
# host, port = sentinel.discover_master('mymaster')
# redis_client = redis.StrictRedis(
#             host=host,
#             port=port,
#             password= 'test@123'
#         )

import datetime
import time
import redis
import redis.sentinel

sentinel = redis.sentinel.Sentinel(
    sentinels=[('aa5a07165a1d844c58e040f0e67b2edb-922594e05d12f077.elb.us-east-1.amazonaws.com/redisone', 26379),
                     ('aa5a07165a1d844c58e040f0e67b2edb-922594e05d12f077.elb.us-east-1.amazonaws.com/redisone',26379),
                     ('aa5a07165a1d844c58e040f0e67b2edb-922594e05d12f077.elb.us-east-1.amazonaws.com/redisone',26379)],
                     socket_timeout=10,
    sentinel_kwargs={'password': 'test@123'},
    password='test@123',
)

while True:
    try:
        master = sentinel.discover_master('mymaster')
        # master.set('foo', 'bar')
        # result = master.get('foo')
        print(datetime.datetime.now(), 'ok:', master)
    except Exception as ex:
        print(datetime.datetime.now(), 'error:', ex)