"""usage my_ls.py [-h] dir suffix

List the files in a given directory with a given suffix.

positional arguments:
   dir      Directory
   suffix   File suffix (e.g. py, sh)

optional arguments:
   -h, --help show this help message 
"""

import argparse
import glob 

def main(args):
    """Run the program."""
    files = glob.glob(f'{args.dir}/*.{args.suffix}')
    print(args.h)
    for f in sorted(files):
        print(f)
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', type = str, help = 'Directory')
    parser.add_argument('suffix', type = str, help = 'File suffix (e.g. py, sh)')
            
    args = parser.parse_args()
    main(args)