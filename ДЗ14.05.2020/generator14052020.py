def my_gen():
    counter = 0
    while counter < 100:
        yield counter
        counter += 1
for i in my_gen():
    print(i)
    if i%3==0:
        print("Василий")

#Решил ограничить генератор до 100, что бы программа не шла бесконечно, но принцип работы понятен.