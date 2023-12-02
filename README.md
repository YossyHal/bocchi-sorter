## venv

```sh
# 1. 仮想環境を作成
pyenv install 3.10.13
pyenv local   3.10.13
python -m venv .venv

# 2. 仮想環境をアクティベート
source .venv/bin/activate

# 3. pipを最新版に更新
python -m pip install --upgrade pip setuptools

# 4. mecabをインストール
sudo apt install mecab libmecab-dev mecab-ipadic-utf8

# 5. ライブラリをインストール
python -m pip install oseti
python -m pip install requests
python -m pip install lxml
```
