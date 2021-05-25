import argparse


class BaseOptions(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
        self.parser.add_argument("-c", "--client",      default="s3",               help="Client to connect to e.g. s3"                     )
        self.parser.add_argument("-b", "--bucket",      default="ml.charisma.ai",   help="Bucked to be tranfered to"                        )
        self.parser.add_argument("-t", "--tranfer",     default="/home",            help="File/s to tansfer"                                )
        self.parser.add_argument("-tt", "--tranferTo",  default="test",             help="Folder to tansfer"                                )

    def __call__(self):
        self.args = self.parser.parse_args()
        return self.args

    def print_options(self):
        message = ''
        message += '---------------------------------- Options --------------------------------\n'
        for k, v in sorted(vars(self.args).items()):
            message += '{:>35} : {:<35} \n'.format(str(k), str(v))
        message += '---------------------------------- End ------------------------------------'
        print(message)
        return message

if __name__ == '__main__':
    obj = BaseOptions()
    args = obj()
    obj.print_options()