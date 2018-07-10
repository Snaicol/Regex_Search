import os

class Search:
    def __init__(self, txt2search, choiceext):
        self.__directory = os.getcwd()
        self.__directoryfiles = os.listdir(self.__directory)
        self.__filestxt = []
        self.__name = ''
        self.__ext = ''
        self.__txt2search = txt2search
        self.__choiceext = choiceext
        self.__file = ''
        self.__text = []

    def __filesearch(self):
        for i in self.__directoryfiles:
            self.__name, self.__ext = os.path.splitext(i)
            if self.__ext == self.__choiceext:
                self.__filestxt.append(i)

    def __textfilesearch(self):
        for j in self.__filestxt:
            with open(j, 'r') as self.__file:
                for num, line in enumerate(self.__file, 1):
                    if self.__txt2search in line:
                        print('Found at line: ' + str(num) + ' in file ' + str(j))

    def main(self):
        self.__filesearch()
        self.__textfilesearch()

def main():
    print('Supported file -> txt, xml')
    choiceext = input('Insert file extension: ')
    if choiceext[0] != '.':
        choiceext = '.' + choiceext

    txt2search = input('Insert text to search: ')
    search = Search(txt2search, choiceext)
    search.main()

if __name__ == '__main__':
    main()



