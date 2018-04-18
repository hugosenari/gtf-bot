from fn.func import curried

get = curried(lambda o, d, k: d.get(k, o))