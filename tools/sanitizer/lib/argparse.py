import argparse
from os.path import abspath


def parse_args(dirs):
    parser = argparse.ArgumentParser(
        description='Rdmo catalog sanitizer replacing accidentally used uris',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-i', '--input_folder', default=dirs['input'],
        help='folder to work in, default: ' + dirs['input']
    )
    parser.add_argument(
        '-o', '--output_folder', default=dirs['output'],
        help='folder to work in, default: ' + dirs['output']
    )
    parser.add_argument(
        '-u', '--new_uri', default=None,
        help='new uri, will be generated if not given'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true', default=False,
        help='debug mode, quickly prints what would have happened, ' +
        'does not write any data'
    )
    args = parser.parse_args()
    args.input_folder = abspath(args.input_folder)
    args.output_folder = abspath(args.output_folder)
    return args
