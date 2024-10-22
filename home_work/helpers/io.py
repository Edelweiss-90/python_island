import datetime

FILE_LOG = 'test.log'


def logger(message_, error_type, line, code, file=FILE_LOG):
    time = datetime.datetime.now()
    fd = open(file, 'at', encoding="utf-8")
    error = f"{error_type}: {time}: {code}: {line}: {__file__}: {message_} "
    fd.write(error + '\n')
    fd.close()
