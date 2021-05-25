import boto3

from options import BaseOptions




if __name__ == '__main__':
    obj = BaseOptions()
    args = obj()
    obj.print_options()


    pass