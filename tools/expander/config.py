import re
from typing import *
from pathlib import Path
from common import *
from subprocess import check_output

def get_gcc_version() -> str:
    output = check_output(['gcc', '--version']).decode('utf-8')
    match = re.search(r'gcc \(GCC\) (\d+.\d.\d)', output)
    assert(match)
    return match.group(1)

# (bits/stdc++.h が存在するような)system include dir
system_include_dir = Path("/usr/include/c++/{}/x86_64-pc-linux-gnu/".format(get_gcc_version()))  # type:Path

# ダミーヘッダーの生成先
dummy_include_dir = script_root_dir / "dummy_headers"  # type:Path

# ダミーヘッダー生成元となるヘッダー
header_source_paths = [
    system_include_dir / "bits/stdc++.h",
    system_include_dir / "bits/extc++.h",
]  # type:List[Path]

# 展開コマンドに用いるコンパイラ
compiler_for_expander = "g++"
