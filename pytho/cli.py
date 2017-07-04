import argparse
import logging
import sys


from .poetry import (validate_ltvb, validate_lbvb,
                     validate_ltvb_2v, validate_lbvb_2v)


def main():
    stcs = sys.stdin.read()
    argp = argparse.ArgumentParser()
    argp.add_argument('-v', '--verbose', action='store_true', default=False)
    args = argp.parse_args()
    logging.basicConfig(level=logging.WARNING)
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if validate_ltvb(stcs):
        print('Đây là bài thơ thất ngôn tứ tuyệt theo luật trắc vần bằng')
    elif validate_lbvb(stcs):
        print('Đây là bài thơ thất ngôn tứ tuyệt theo luật bằng vần bằng')
    elif validate_ltvb_2v(stcs):
        print('Đây là bài thơ thất ngôn tứ tuyệt theo luật trắc vần bằng 2 vần')  # NOQA
    elif validate_lbvb_2v(stcs):
        print('Đây là bài thơ thất ngôn tứ tuyệt theo luật bằng vần bằng 2 vần')  # NOQA
    else:
        print('Không xác định')


if __name__ == "__main__":
    main()
