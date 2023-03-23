import json

def my_decorator(func):
    
    def wrapper(fname):
        if fname.endswith('.json'):
            return func()
        else:
            return "Is not Json"
    return wrapper

@my_decorator
def toDict(fname):
    data = open(fname, 'r').read()
    return json.loads(data)

print(toDict('data.csv'))
# is not json file
