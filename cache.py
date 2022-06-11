from functools import cache

@cache
def generate():
    print('Generating X')
    return 'X'

print(generate())
# 2回目以降の呼出しはキャッシュされたものが返る
print(generate())
print(generate())
