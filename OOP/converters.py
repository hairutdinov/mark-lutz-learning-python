from streams import Processor


class Uppercase(Processor):
    def converter(self, data:str):
        return data.upper()

if __name__ == '__main__':
    import sys
    obj = Uppercase(open('trispam.txt'), sys.stdout)
    obj.process()
