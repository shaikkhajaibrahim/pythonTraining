import time

ticks = time.time()
print("Number of ticks since January 1 1970",ticks)
# epoch

print(time.localtime())

# formatted time

localtime=time.asctime(time.localtime(ticks))


print("Local Current Time",localtime)

print(time.timezone)
print(time.tzname)