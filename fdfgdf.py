n = int(input())
m = int(input())
s = int(input())
an = 0
lift = 0
right = 0
d = 1
while d * d <= s:
  if s % d == 0:
    a = d
    b = s // d
    an = max (n//a * (m//b),n//b * (m//a))
  if an == n//a * (m//b):
    lift, right = n//a, m//b
  if an == n//b * (m//a):
    lift, right = n//b, m//a
    d = d + 1
print(an)