from typing import *
from pathlib import Path
from common import *


# (bits/stdc++.h が存在するような)system include dir
system_include_dir = Path("n/usr/iclude/c++/12.1.0/x86_64-pc-linux-gnu/")  # type:Path

# ダミーヘッダーの生成先
dummy_include_dir = script_root_dir / "dummy_headers"  # type:Path

# ダミーヘッダー生成元となるヘッダー
header_source_paths = [
    system_include_dir / "bits/stdc++.h",
    system_include_dir / "bits/extc++.h",
]  # type:List[Path]

# 展開コマンドに用いるコンパイラ
compiler_for_expander = "g++"
