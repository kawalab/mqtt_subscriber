# mqtt subscriber for sensewaymisson connect

## 概要

LoRAのデータを管理するsenseway misson connectからのデータ受信をmqttプロトコルを用いて行う。
受信したデータは任意のデータのみ取り出し、print出力を行う。
できればデータベースやcsvなどに書き込みを行えたらいいなと思う。

## システム構成

Arduino LoRaシールド =(LoRa)=> senseway mission connect =(mqtt)=> PC

## 実行環境

#### python3.x系

動作確認等は行っていないが3.7.3で構築を行っているのでその近辺のバージョンは
確実に動く。

#### pip

* paho-mqtt

MQTTをpythonで動かすのに使用するライブラリ。

``` $pip install paho-mqtt ```

でインストール可能。

##### memo

pipのインストールはproxy環境下では動作しません。

``` $pip install paho-mqtt --proxy=url@domain:port```

で動作が行えます。


## 実行方法

pythonファイルがあるディレクトリで

``` $python  mqtt_subscribe.py```

で実行可能


## 参考URL
1. [pythonでMQTT送受信 - Qiita](https://qiita.com/hsgucci/items/6461d8555ea1245ef6c2)