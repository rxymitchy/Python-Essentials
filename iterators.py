#Lists, sets, dictionaries,tuples, strings are iterable objects
#uses iter() & next()

print("tuple iterator:")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# #using for loop
# for x in mytuple:
#   print(x) 

#STRINGS  
print("sring iterators: ")
mystr = "banana"
#mysit = iter(mystr)
for x in mystr:
  print(x) 

print("Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc")
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration

myclass = MyNumbers()

for x in myclass:
    print(x)