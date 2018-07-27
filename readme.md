## 概要
  - NFCカードリーダーを買ったは良いが、USBに接続した後どう使ったらよいかわからず試作
  - dockerコンテナを起動するだけでNFC カードリーダーがスタンバイ状態になり、接触したカードの情報と取得時刻をコンテナに保存する
  - 保存したデータはコンテナを破棄してもボリュームとして保持される（リセットするなら`docker-compose -d`）
  - PCにNFCカードリーダーを接続してカード情報を取得することをテーマにしたサンプルアプリ(タイムカードやドアロック代わりに使えるかも)
  - ※ docker および docker-compose の使い方は理解しているものとする

## 環境構築(確認済のもの)
  - Docker version 18.03.1-ce
  - docker-compose version 1.6.2
  - 仮想環境から docker を利用する場合、ホストPCのUSB機器を認識できる状況であること(lsusb コマンドで ACR-122U が確認できること)
  - ACR-122U-A2(https://www.amazon.co.jp/gp/product/B017LPCFH2) で動作確認済だが、nfcpyライブラリが対応しているデバイスなら他のものでも良い？

## 利用方法
  - `docker-compose -d` した時点でデバイスのアクセスランプがグリーンになり、NFCカードのタッチを受け付ける（接触→離れた時点で音が鳴る）
  - `docker exec -it nfc_db mysql -proot -ppass` でコンテナ内のDBにアクセス、`SELECT * FROM attendance.stamp;` で保存したデータを確認できる

  - サンプルパスに手を加えて保存先のDBを変更する、情報をAPIに送信して別の勤怠管理アプリで利用するなど
