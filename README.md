# Sansan × HubSpot 連携 - サンプルコード

## 動作環境

- Python 3+

## 事前準備

1, [Requests](http://docs.python-requests.org/en/master/)ライブラリのインストール

    $ pip install requests

2, main.pyファイルにてAPIキーを指定

    sansan_api_key = 'ea1...'
    hubspot_api_key = '6ba...'

## 実行方法

ターミナル（コマンドプロンプト）より下記のコマンドにて実行ください。

1, 名刺データの取得

    $ python main.py get

2, SansanとHubSpotのデータ同期（Sansan名刺データ × HubSpotコンタクト）

    $ python main.py sync


## ライセンス

This software is licensed under the MIT License.
