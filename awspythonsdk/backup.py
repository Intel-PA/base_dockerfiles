import os

import logging
import boto3
from botocore.exceptions import ClientError
import argparse

class BaseOptions(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
        self.parser.add_argument("-c", "--client",      default="s3",               help="Client to connect to e.g. s3"                     )
        self.parser.add_argument("-t", "--tranfer",     default="/home",            help="File/s to tansfer"                                )
        self.parser.add_argument("-tt", "--tranferTo",  default="test",             help="Folder to tansfer"                                )
        self.parser.add_argument("-b", "--bucket",      default="ml.charisma.ai",   help="Bucked to be tranfered to"                        )


    def __call__(self):
        self.args = self.parser.parse_args()
        return self.args

    def print_options(self):
        message = ''
        message += '---------------------------------- Options --------------------------------\n'
        for k, v in sorted(vars(self.args).items()):
            message += '{:>25} : {:<25} \n'.format(str(k), str(v))
        message += '---------------------------------- End ------------------------------------'
        print(message)
        return message


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def getFiles(dir):
    fileList = os.listdir(dir)
    file_dir = []
    
    for file in fileList:
        file_dir.append(os.path.join(dir, file))

    return file_dir

def uploadDirectory(path, bucketname, foldername=None):
        for root,dirs,files in os.walk(path):
            for file in files:
                path = os.path.join(root,file)
                
                if foldername == None:
                    savePath = file
                else:
                    savePath = os.path.join(foldername, file)
                    
                saveDir = os.path.join(foldername)
                s3.upload_file(os.path.join(root,file),bucketname,savePath)


if __name__ == "__main__":
    obj = BaseOptions()
    args = obj()
    obj.print_options()

    s3 = boto3.client(args.client)
    uploadDirectory(args.tranfer, args.bucket, args.tranferTo)
