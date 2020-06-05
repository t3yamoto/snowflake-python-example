# snowflake-python-example

Python ドライバで Snowflake に接続するサンプルコードです。

## 前提条件

* Python 3.8+
* Direnv

## インストール

```sh
git clone https://github.com/t3yamoto/snowflake-python-example.git
cd snowflake-python-example
cp .envrc.sample .envrc
direnv edit . # ユーザー等、自分の環境に書き換え
direnv allow
```

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 実行

```
python verify_installation.py # バージョン確認
python fetch_per_row.pyt # 1行ずつfetchするサンプル
python fetch_all.pyt # 全件fetchするサンプル
```

