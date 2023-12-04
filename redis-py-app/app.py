import redis
from redis.sentinel import Sentinel
sentinel = Sentinel([('ae0181f6b69c249fe9b89d365ab10aaa-1367026668.us-east-1.elb.amazonaws.com', 26379),
                     ('aa12b520bca654523840d277225fb97c-400453335.us-east-1.elb.amazonaws.com',26379),
                     ('aeddf30b34e2c4a03be038e21129b311-60908045.us-east-1.elb.amazonaws.com',26379)],
                   sentinel_kwargs={'password': 'test@123'})
# you will need to handle yourself the connection to pass again the password
# and avoid AuthenticationError at redis queries
host, port = sentinel.discover_master('mymaster')
redis_client = redis.StrictRedis(
            host=host,
            port=port,
            password= 'test@123'
        )