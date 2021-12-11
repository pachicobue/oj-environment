import re
from logging import getLogger, Logger
from typing import *
from pathlib import Path
from config import *

_logger = getLogger(__name__)  # type:Logger
_header_names = []  # type:List[str]


def create_dummy_headers() -> None:
    for path in header_source_paths:
        _collect_header_names(path)
    for filename in _header_names:
        _create_dummy_header(filename)


def _collect_header_names(filepath: Path) -> None:
    if not filepath.exists():
        _logger.error('{} does not exist.'.format(filepath))
        return
    include_pattern = re.compile(r'#include <(.*)>')
    with open(filepath) as f:
        for line in f:
            match = include_pattern.match(line)
            if match:
                _header_names.append(match[1])


def _create_dummy_header(filename: str) -> None:
    dummy_file_path = dummy_include_dir / filename
    dummy_file_dir = dummy_file_path.parent
    dummy_file_dir.mkdir(parents=True, exist_ok=True)
    pathlib.Path.touch(dummy_file_path, exist_ok=True)
    with open(dummy_file_path, mode='w') as f:
        f.write('#pragma INCLUDE <{}>'.format(filename))
    _logger.debug('dummy header {} created.'.format(dummy_file_path))
