import redis
from redis.sentinel import Sentinel
sentinel = Sentinel([('aa5a07165a1d844c58e040f0e67b2edb-922594e05d12f077.elb.us-east-1.amazonaws.com/redisone', 26379),
                     ('aa5a07165a1d844c58e040f0e67b2edb-922594e05d12f077.elb.us-east-1.amazonaws.com/redistwo',26379),
                     ('aa5a07165a1d844c58e040f0e67b2edb-922594e05d12f077.elb.us-east-1.amazonaws.com/redisthree',26379)],
                   sentinel_kwargs={'password': 'test@123'})
# you will need to handle yourself the connection to pass again the password
# and avoid AuthenticationError at redis queries
host, port = sentinel.discover_master('mymaster')
redis_client = redis.StrictRedis(
            host=host,
            port=port,
            password= 'test@123'
        )