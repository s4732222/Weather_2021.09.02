import time

seconds=time.time()

result =time.localtime(seconds)

year           = result.tm_year
month          = result.tm_mon
day            = result.tm_mday
hour           = result.tm_hour
minutes        = result.tm_min
seconds        = result.tm_sec
accumulate_day = result.tm_yday

print(type(accumulate_day))

    
print(year ,month ,day ,hour ,minutes ,seconds ,accumulate_day)

#print(result)