import sys
import getopt
from modules import awsInventory


def main(argv):

    aws_profile = ''
    aws_scope = ''

    short_opts = ""
    long_opts = ["aws-profile=", "aws-scope="]

    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)
    except getopt.error as err:
        print (str(err))
        sys.exit()

    for option, value in opts:
        if option in ('--aws-profile'):
            aws_profile = value
        elif option == "--aws-scope":
            aws_scope = value        

    if "ec2" in aws_scope.split(","):
        ec2 = awsInventory.ec2()
        ec2.aws_profile = aws_profile
        print(ec2.inventory())

    if "eks" in aws_scope.split(","):
        eks = awsInventory.eks()
        eks.file = sys.argv[1]
        print(eks.inventory())    


if __name__ == "__main__":
	main(sys.argv[1:])
