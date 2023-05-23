import datetime


class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg
        self.log_error()

    def log_error(self):
        timestamp = datetime.datetime.now().strftime('%Y-%m%d %H:%M:%S')
        exception_type = type(self).__name__
        log_message = f'[{timestamp}] [{exception_type}] {self.msg}'

        with open('logs_error.txt', 'a') as file:
            file.write(log_message + '\n')


try:
    raise CustomException('An arror occured!')
except CustomException as e:
    print('Exception caught: ', e)
