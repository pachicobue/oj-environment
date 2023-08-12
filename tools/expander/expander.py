import subprocess
import re
from subprocess import Popen, PIPE
from pathlib import Path
from logging import getLogger, Logger
from typing import *
from config import *

_logger = getLogger(__name__)  # type:Logger


class Expander:
    def __init__(
        self, source_filename: str, include_dir_names: List[str], definitions: List[str], delete_comments: bool
    ):
        self.source_file_path = Path(source_filename).resolve()  # type:Path
        self.output_file_path = self.source_file_path.with_name(
            self.source_file_path.stem + "_submission" + self.source_file_path.suffix
        )
        self.tmp_file_path = self.source_file_path.with_name(
            self.source_file_path.stem + "_tmp" + self.source_file_path.suffix
        )
        _logger.debug("source_file_path: {}".format(self.source_file_path))
        _logger.debug("output_file_path: {}".format(self.output_file_path))
        _logger.debug("tmp_file_path: {}".format(self.tmp_file_path))

        self.include_directories = []  # type:List[Path]
        for dir_name in include_dir_names:
            include_path = Path(dir_name).resolve()
            self.include_directories.append(include_path)

        self.definitions = definitions  # type:List[str]
        self.delete_comments = delete_comments # type:bool

    def expand_include(self) -> None:
        commands = [
            compiler_for_expander,
            str(self.source_file_path),
            "-o",
            str(self.tmp_file_path),
            "-nostdinc",
            "-E",
            "-P",
        ]
        if not self.delete_comments:
            commands.append("-C")
        for macro in self.definitions:
            commands.append("-D")
            commands.append(macro)
        for directory in self.include_directories:
            print(directory);
            commands.append("-I")
            commands.append(str(directory))
        subprocess.run(commands, cwd=self.source_file_path.parent)

    def post_process(self, save_output: bool, save_to_clipboard: bool) -> None:
        output = self._beautify_output(open(str(self.tmp_file_path)).read())
        _logger.debug("output = \n{}".format(output))
        self.tmp_file_path.unlink()
        if save_output:
            with open(str(self.output_file_path), mode="w") as f:
                f.write(output)
        if save_to_clipboard:
            self._save_to_clipboard(output)

    def _beautify_output(self, source: str) -> str:
        headers = set()
        include_pattern = re.compile("#pragma INCLUDE <(.*)>")
        output = ""
        for line in source.splitlines():
            if re.match("^\s*$", line):
                continue
            match = include_pattern.match(line)
            if match:
                headers.add("#include <{}>".format(match[1]))
            else:
                output += line + "\n"
        return "\n".join(headers) + "\n" + output

    def _save_to_clipboard(self, output: str) -> None:
        p = Popen(['xsel', '-bi'], stdin=PIPE)
        p.communicate(input=output.encode('utf-8'))
