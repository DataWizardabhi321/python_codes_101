#simply know   as   generators  and  iterators   in python generators  allow us    to create iterators  in  a  simple way
def  countdown(n):
    while n >0:
        yield n
        n -=1
for num  in  countdown(5):
    print(num)