# Reading Ifs & Loops

# a
string = "hello"
length = 0
for char in string:
  length += 1
print(string, "length is", length)


# b
mmm = 4
for i in range(10):
  if i % 3 == 0:
    mmm += i
print(mmm)


# c
list = [2, 6, -3, 5]
total = 0
for x in list:
  if x > 0:
    total = total + x

print(total)


# d
x = 0
for j in range(-5,6):
  if j >= 0:
    if j % 2 == 0:
      x += j
    else:
      x -= j
  else:
    if j % 5 == 0:
      x *= -1 * j
    x += j
print(x)