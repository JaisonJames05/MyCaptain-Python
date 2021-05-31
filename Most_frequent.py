W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    d = dict(sorted(d.items(),key=lambda x: x[1], reverse=True))
    return d
print(most_frequent(W))