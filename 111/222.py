from PIL import Image
im = Image.open('D://test.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

import sys

print(sys.path)

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __sizeof__(self) -> int:
        return super().__sizeof__()

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))