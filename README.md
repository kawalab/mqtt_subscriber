# mqtt subscriber for sensewaymisson connect

## 概要

LoRAのデータを管理するsenseway misson connectからのデータ受信をmqttプロトコルを用いて行う。
受信したデータは任意のデータのみ取り出し、print出力を行う。
できればデータベースやcsvなどに書き込みを行えたらいいなと思う。

## システム構成

Arduino LoRaシールド =(LoRa)=> senseway mission connect =(mqtt)=> PC

## 実行環境

### python3.x系

動作確認等は行っていないが3.7.3で構築を行っているのでその近辺のバージョンは
確実に動く。

### pip

* paho-mqtt

MQTTをpythonで動かすのに使用するライブラリ。

``` $pip install paho-mqtt ```

でインストール可能。

## 参考URL
1. {Qiita Markdown 書き方 まとめ - Qiita}[https://qiita.com/shizuma/items/8616bbe3ebe8ab0b6ca1]