#API Reference
-----------------------------
1. append(self, key, value)

        Appends the string value to the value at key. If key doesn't already exist, create it with a value of value. Returns the new length of the value at key.

2. bgrewriteaof(self)

        Tell the Redis server to rewrite the AOF file from data in memory.

3. bgsave(self)

        Tell the Redis server to save its data to disk. Unlike save(), this method is asynchronous and returns immediately.

4. blpop(self, keys, timeout=0)

        LPOP a value off of the first non-empty list named in the keys list.

        If none of the lists in keys has a value to LPOP, then block for timeout seconds, or until a value gets pushed on to one of the lists.

        If timeout is 0, then block indefinitely.

5. brpop(self, keys, timeout=0)

        RPOP a value off of the first non-empty list named in the keys list.

        If none of the lists in keys has a value to LPOP, then block for timeout seconds, or until a value gets pushed on to one of the lists.

        If timeout is 0, then block indefinitely.

6. dbsize(self)

        Returns the number of keys in the current database

7. decr(self, name, amount=1)

    Decrements the value of key by amount. If no key exists, the value will be initialized as 0 - amount

delete(self, *names)
Delete one or more keys specified by names

encode(self, value)
Encode value using the instance's charset

execute_command(self, *args, **options)
Sends the command to the redis server and returns it's response

exists(self, name)
Returns a boolean indicating whether key name exists

expire(self, name, time)
Set an expire flag on key name for time seconds

expireat(self, name, when)
Set an expire flag on key name. when can be represented as an integer indicating unix time or a Python datetime object.

flush(self, all_dbs=False)
flushall(self)
Delete all keys in all databases on the current host

flushdb(self)
Delete all keys in the current database

get(self, name)
Return the value at key name, or None of the key doesn't exist

get_connection(self, host, port, db, password, socket_timeout)
Returns a connection object

getset(self, name, value)
Set the value at key name to value if key doesn't exist Return the value at key name atomically

hdel(self, name, key)
Delete key from hash name

hexists(self, name, key)
Returns a boolean indicating if key exists within hash name

hget(self, name, key)
Return the value of key within the hash name

hgetall(self, name)
Return a Python dict of the hash's name/value pairs

hincrby(self, name, key, amount=1)
Increment the value of key in hash name by amount

hkeys(self, name)
Return the list of keys within hash name

hlen(self, name)
Return the number of elements in hash name

hmget(self, name, keys)
Returns a list of values ordered identically to keys

hmset(self, name, mapping)
Sets each key in the mapping dict to its corresponding value in the hash name

hset(self, name, key, value)
Set key to value within hash name Returns 1 if HSET created a new field, otherwise 0

hsetnx(self, name, key, value)
Set key to value within hash name if key does not exist. Returns 1 if HSETNX created a field, otherwise 0.

hvals(self, name)
Return the list of values within hash name

incr(self, name, amount=1)
Increments the value of key by amount. If no key exists, the value will be initialized as amount

info(self)
Returns a dictionary containing information about the Redis server

keys(self, pattern='*')
Returns a list of keys matching pattern

lastsave(self)
Return a Python datetime object representing the last time the Redis database was saved to disk

lindex(self, name, index)
Return the item from list name at position index

Negative indexes are supported and will return an item at the end of the list

listen(self)
Listen for messages on channels this client has been subscribed to

llen(self, name)
Return the length of the list name

lock(self, name, timeout=None, sleep=0.10000000000000001)
Return a new Lock object using key name that mimics the behavior of threading.Lock.

If specified, timeout indicates a maximum life for the lock. By default, it will remain locked until release() is called.

sleep indicates the amount of time to sleep per loop iteration when the lock is in blocking mode and another client is currently holding the lock.

lpop(self, name)
Remove and return the first item of the list name

lpush(self, name, value)
Push value onto the head of the list name

lrange(self, name, start, end)
Return a slice of the list name between position start and end

start and end can be negative numbers just like Python slicing notation

lrem(self, name, value, num=0)
Remove the first num occurrences of value from list name

If num is 0, then all occurrences will be removed

lset(self, name, index, value)
Set position of list name to value

ltrim(self, name, start, end)
Trim the list name, removing all values not within the slice between start and end

start and end can be negative numbers just like Python slicing notation

mget(self, keys, *args)
Returns a list of values ordered identically to keys

Passing *args to this method has been deprecated *
move(self, name, db)
Moves the key name to a different Redis database db

mset(self, mapping)
Sets each key in the mapping dict to its corresponding value

msetnx(self, mapping)
Sets each key in the mapping dict to its corresponding value if none of the keys are already set

parse_response(self, command_name, catch_errors=False, **options)
Parses a response from the Redis server

ping(self)
Ping the Redis server

pipeline(self, transaction=True)
Return a new pipeline object that can queue multiple commands for later execution. transaction indicates whether all commands should be executed atomically. Apart from multiple atomic operations, pipelines are useful for batch loading of data as they reduce the number of back and forth network operations between client and server.

pop(self, name, tail=False)
Pop and return the first or last element of list name

This method has been deprecated, use Redis.lpop or Redis.rpop instead.

psubscribe(self, patterns)
Subscribe to all channels matching any pattern in patterns

publish(self, channel, message)
Publish message on channel. Returns the number of subscribers the message was delivered to.

punsubscribe(self, patterns=[])
Unsubscribe from any channel matching any pattern in patterns. If empty, unsubscribe from all channels.

push(self, name, value, head=False)
Push value onto list name.

This method has been deprecated, use Redis.lpush or Redis.rpush instead.

randomkey(self)
Returns the name of a random key

rename(self, src, dst, **kwargs)
Rename key src to dst

The following flags have been deprecated *If preserve is True, rename the key only if the destination name doesn't already exist
renamenx(self, src, dst)
Rename key src to dst if dst doesn't already exist

rpop(self, name)
Remove and return the last item of the list name

rpoplpush(self, src, dst)
RPOP a value off of the src list and atomically LPUSH it on to the dst list. Returns the value.

rpush(self, name, value)
Push value onto the tail of the list name

sadd(self, name, value)
Add value to set name

save(self)
Tell the Redis server to save its data to disk, blocking until the save is complete

scard(self, name)
Return the number of elements in set name

sdiff(self, keys, *args)
Return the difference of sets specified by keys

sdiffstore(self, dest, keys, *args)
Store the difference of sets specified by keys into a new set named dest. Returns the number of keys in the new set.

select(self, db, host=None, port=None, password=None, socket_timeout=None)
Switch to a different Redis connection.

If the host and port aren't provided and there's an existing connection, use the existing connection's host and port instead.

Note this method actually replaces the underlying connection object prior to issuing the SELECT command. This makes sure we protect the thread-safe connections

set(self, name, value, **kwargs)
Set the value at key name to value

The following flags have been deprecated *If preserve is True, set the value only if key doesn't alreadyexistIf getset is True, set the value only if key doesn't already existand return the resulting value of key
setex(self, name, value, time)
Set the value of key name to value that expires in time seconds

setnx(self, name, value)
Set the value of key name to value if key doesn't exist

sinter(self, keys, *args)
Return the intersection of sets specified by keys

sinterstore(self, dest, keys, *args)
Store the intersection of sets specified by keys into a new set named dest. Returns the number of keys in the new set.

sismember(self, name, value)
Return a boolean indicating if value is a member of set name

smembers(self, name)
Return all members of the set name

smove(self, src, dst, value)
Move value from set src to set dst atomically

sort(self, name, start=None, num=None, by=None, get=None, desc=False, alpha=False, store=None)
Sort and return the list, set or sorted set at name.

start and num allow for paging through the sorted data

by allows using an external key to weight and sort the items. Use an "*" to indicate where in the key the item value is located

get allows for returning items from external keys rather than the sorted data itself. Use an "*" to indicate where int he key the item value is located

desc allows for reversing the sort

alpha allows for sorting lexicographically rather than numerically

store allows for storing the result of the sort into the key store

spop(self, name)
Remove and return a random member of set name

srandmember(self, name)
Return a random member of set name

srem(self, name, value)
Remove value from set name

subscribe(self, channels)
Subscribe to channels, waiting for messages to be published

substr(self, name, start, end=-1)
Return a substring of the string at key name. start and end are 0-based integers specifying the portion of the string to return.

sunion(self, keys, *args)
Return the union of sets specifiued by keys

sunionstore(self, dest, keys, *args)
Store the union of sets specified by keys into a new set named dest. Returns the number of keys in the new set.

ttl(self, name)
Returns the number of seconds until the key name will expire

type(self, name)
Returns the type of key name

unsubscribe(self, channels=[])
Unsubscribe from channels. If empty, unsubscribe from all channels

zadd(self, name, value, score)
Add member value with score score to sorted set name

zcard(self, name)
Return the number of elements in the sorted set name

zincr(self, key, member, value=1)
This has been deprecated, use zincrby instead

zincrby(self, name, value, amount=1)
Increment the score of value in sorted set name by amount

zinter(self, dest, keys, aggregate=None)
zinterstore(self, dest, keys, aggregate=None)
Intersect multiple sorted sets specified by keys into a new sorted set, dest. Scores in the destination will be aggregated based on the aggregate, or SUM if none is provided.

zrange(self, name, start, end, desc=False, withscores=False)
Return a range of values from sorted set name between start and end sorted in ascending order.

start and end can be negative, indicating the end of the range.

desc indicates to sort in descending order.

withscores indicates to return the scores along with the values. The return type is a list of (value, score) pairs

zrangebyscore(self, name, min, max, start=None, num=None, withscores=False)
Return a range of values from the sorted set name with scores between min and max.

If start and num are specified, then return a slice of the range.

withscores indicates to return the scores along with the values. The return type is a list of (value, score) pairs

zrank(self, name, value)
Returns a 0-based value indicating the rank of value in sorted set name

zrem(self, name, value)
Remove member value from sorted set name

zremrangebyrank(self, name, min, max)
Remove all elements in the sorted set name with ranks between min and max. Values are 0-based, ordered from smallest score to largest. Values can be negative indicating the highest scores. Returns the number of elements removed

zremrangebyscore(self, name, min, max)
Remove all elements in the sorted set name with scores between min and max. Returns the number of elements removed.

zrevrange(self, name, start, num, withscores=False)
Return a range of values from sorted set name between start and num sorted in descending order.

start and num can be negative, indicating the end of the range.

withscores indicates to return the scores along with the values as a dictionary of value => score

zrevrank(self, name, value)
Returns a 0-based value indicating the descending rank of value in sorted set name

zscore(self, name, value)
Return the score of element value in sorted set name

zunion(self, dest, keys, aggregate=None)
zunionstore(self, dest, keys, aggregate=None)