import redis

redis_cli = redis.Redis(host="localhost", port=6379)
redis_cli.publish("article", 123)