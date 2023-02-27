# oj-environment
競プロ用のコンテスト環境

## 内容物
- ライブラリ
  - [algolib](https://github.com/pachicobue/algolib)
  - [ac-library](https://github.com/atcoder/ac-library)
- ツール群
  - expander
    - 提出用ファイルを展開する
  - installer
    - 初期設定用

## 初期設定
1. submoduleを初期化
    ```sh
    $ git submodule update --init
    ```
2. fishのC++コンパイル用設定をinstall
   1. コンパイル周りのconfigを `~/.config/fish/conf.d` にコピー
        ```sh
        $ python3 tools/installer/main.py
        ```
   2. fishを再起動すると`dg++,fg++`などのアイリアス関数が使える
3. vscode-extensionをインストール
   1. vsixファイルを生成
        ```sh
        $ cd vscode-extensions/vscode-oj-input-picker
        $ npx vsce package
        ```
   2. vscodeの「VSIXからインストール」で拡張機能をインストール

## submodule を更新する
```sh
$ git submodule update --remote --merge
```
