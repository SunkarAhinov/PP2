def s(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(s('python_exercises'))