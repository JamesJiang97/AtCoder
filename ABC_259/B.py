import math


a, b, d = map(int, input().split())

d = d*math.pi/180

cosd = math.cos(d)

sind = math.sin(d)

ad = a*cosd - b*sind

bd = a*sind + b*cosd

print(str(ad) + ' ' + str(bd))