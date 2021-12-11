#!/usr/bin/env python3
from argparse import ArgumentParser, Namespace
import logging
from logging import getLogger, basicConfig, Logger

from config import *
from expander import Expander
from create_dummy_headers import create_dummy_headers

_logger = getLogger()  # type:Logger


def expand(args: Namespace):
    _logger.info(('main.py'
                  ' source_filename={}\n'
                  ' --include_directories={}\n'
                  ' --definitions={}\n'
                  ' --log_level={}\n'
                  ' --save_to_clipboard={}\n'
                  ' --save-output={}').format(args.source_file_name,
                                              args.include_directories,
                                              args.definitions,
                                              args.log_level,
                                              args.save_to_clipboard,
                                              args.save_output))

    create_dummy_headers()
    include_directories = args.include_directories
    include_directories.append(str(dummy_include_dir))

    expander = Expander(args.source_file_name,
                        include_directories,
                        args.definitions)  # type:Expander
    expander.expand_include()
    expander.post_process(args.save_output, args.save_to_clipboard)


if __name__ == "__main__":
    parser = ArgumentParser(
        description='Expand \'#include "my/lib"\' from given source code.')
    parser.add_argument('source_file_name',
                        help='Name of source')
    parser.add_argument('-I', '--include_directories', nargs='*', default=[])
    parser.add_argument('-D', '--definitions', nargs='*', default=[])
    parser.add_argument('-L', '--log_level',
                        choices=['DEBUG', 'INFO',
                                 'WARNING', 'ERROR', 'CRITICAL'],
                        default='WARNING')
    parser.add_argument('--save_to_clipboard', action='store_true')
    parser.add_argument('--save_output', action='store_true')

    args = parser.parse_args()  # type:Namespace
    basicConfig(format='[{levelname}] {name}: {message}',
                level=getattr(logging, args.log_level),
                style='{')
    expand(args)
