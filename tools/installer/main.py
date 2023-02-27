#!/usr/bin/env python3
from typing import *
import pathlib
import re

script_root_dir = pathlib.Path(__file__).parent  # Path
workspace_dir = script_root_dir.parent.parent.resolve()  # Path


def create_fish_config():
    algolib_path = workspace_dir / "algolib"  # Path
    acl_path = workspace_dir / "ac-library"  # Path
    src_config_path = script_root_dir / "oj.fish"  # Path
    dst_config_path = pathlib.Path("/home/sho/.config/fish/conf.d/oj.fish")  # Path
    dst_config_path.touch()
    with open(src_config_path, "r") as src:
        lines = src.readlines()  # List[str]
    with open(dst_config_path, "w") as dst:
        for line in lines:
            if re.match(r"set ALGOLIB_PATH", line):
                line = "set ALGOLIB_PATH {}\n".format(algolib_path)
            elif re.match(r"set ACL_PATH", line):
                line = "set ACL_PATH {}\n".format(acl_path)
            dst.write(line)


if __name__ == "__main__":
    create_fish_config()
