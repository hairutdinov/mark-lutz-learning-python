import sys
class FormatError(Exception):
    log_file = 'format_error.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def log_error(self):
        with open(self.log_file, 'a') as file:
            file.write(self.message() + '\n')
    def message(self):
        return 'Error at: {file} {line}'.format(file=self.file, line=self.line)
try:
    raise FormatError(42, file='spam.txt')
except FormatError:
    e = sys.exc_info()[1]
    e.log_error()
    # print(e.message())