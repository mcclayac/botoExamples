import textwrap

__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/24/17'
__revision__ = '$'
__revision_date__ = '$'



import argparse
import textwrap
parser = argparse.ArgumentParser()
# parser = argparse.ArgumentParser(description='This is a sample Script with arguements',
#                                  epilog="BigManSoftware Copyright 2017")
# formatter_class=argparse.RawDescriptionHelpFormatter,
parser = argparse.ArgumentParser(
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                description=textwrap.dedent('''\
                                This is a sample Script with arguements
                                I will make this very long so that I get 
                                at least 3 lines worth
                                ----------------------
                                    Indent 1
                                    Indent 1
                                
                                '''),
                                 epilog='''
        BigManSoftware Copyright 2017 - BigmanSoftware
        Developed by : Tony McClay
        Date: 7/24/2017 
        All Rights reserved''')

parser.add_argument("requiredArcguemnt", help="This is the first required arguement")
parser.add_argument("squared", help="This number will be sqaured", type=int)
parser.add_argument("--anOptional", help="an Optional argument")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-i", "--integer", type=int, choices=[0, 1, 2], default=0,
                    help="Optional Integer")
args = parser.parse_args()


print( args)
programName = parser.prog
print("ProgramName : " + programName)

# print(args.requiredArcguemnt)
squared = args.squared
print(squared**2)


req1 = args.requiredArcguemnt
print("req1 = " + req1)

if args.anOptional:
    print("anOptional turned on :" + args.anOptional)

verbose = args.verbose
print(type(verbose))

bolVerbose = bool(verbose)
if bolVerbose:
    print("verbose turned on :")
else:
    print("verbose turned off :")

if args.integer == 0 :
    print("Opyional Integer is 0")
else:
    print("Opyional Integer is NOT 0")
    print("Opyional Integer : " + str(args.integer))



# description='''This is a sample Script with arguements
# I will make this very long so that I get
# at least 3 lines worth''',

