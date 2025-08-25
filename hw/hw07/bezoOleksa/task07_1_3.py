def analyze(string):
    return {l: string.count(l) for l in set(string)}
