import argparse
from os.path import abspath


def parse_args(dirs):
    default_uri_prefix = 'https://rdmorganiser.github.io/terms'
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
        '-f', '--old_uri_prefix', default=default_uri_prefix,
        help='old uri to find and be replaced, default: ' + default_uri_prefix
    )
    parser.add_argument(
        '-n', '--new_uri_prefix', default=None,
        help='new uri replacing the old one, if not given generated'
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
