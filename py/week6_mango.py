

graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': [],
}


def search(name):
    queue = []
    queue += graph[name]
    searched = set()
    while queue:
        person = queue.pop(0)
        if person in searched:
            continue
        if is_seller(person):
            print("%s is a mango seller!" % person)
            return
        searched.add(person)
        queue += graph[person]
    print("There is no mango seller")
    return False


def is_seller(person):
    return person[-1].lower() == 'm'


if __name__ == '__main__':
    search('you')
