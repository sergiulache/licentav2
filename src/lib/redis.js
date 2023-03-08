import Redis from 'ioredis';

const redis = new Redis({
	host: 'localhost',
	port: 6379
	// optional: add a password if your Redis instance requires authentication
	// password: 'your-redis-password'
});

// optional: handle Redis connection errors
redis.on('error', (err) => {
	console.error('Error connecting to Redis', err);
});

export default redis;
