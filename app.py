from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    visitor_count = redis_client.incr('visitor_count')
    return f'This is the {visitor_count} visitor'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
