import pytz
import datetime
country='Turkey'
tz_to_display=pytz.timezone(country)
local_time=  datetime.datetime.now(tz=tz_to_display)
print("the time in {} is {}".format(country,local_time))
print("UTC is{}".format(datetime.datetime.utcnow()))


# for x in sorted(pytz.country_names):
#     print(x+ ':'+pytz.country_names[x])
# 


for x in sorted(pytz.country_names):
    print('{}:{}:{}'.format(x,pytz.country_names[x],pytz.country_timezones.get(x)))
    if x in pytz.common_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display=pytz.timezone(zone)
            local_time=datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone,local_time))
    else:
        print("\t\t No time Zone defined")


