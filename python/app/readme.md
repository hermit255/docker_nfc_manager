## 環境構築
  ### パッケージリストの更新
    - apt-get update
  ### NFCカードリーダー(USB)ドライバ
    - apt-get -y install libusb-1.0-0-dev
  ### Python 2.7
    - apt-get -y install python2.7
  ### パッケージマネージャ pip のインストールまたは更新 + 必要パッケージの導入
    - curl -kL https://bootstrap.pypa.io/get-pip.py | python
    - pip install --upgrade pip
    - pip install nfcpy mysql-connector-python
## 設定
    - config_sample.py を config.py にリネームして、自己環境のDB設定に合わせる
    - read_uid.py の最終行でカードを接触→離脱したとき save_to_database() するようにしているが、save_to_text() にすればdb設定も不要になり、ソースフォルダに output.txt として出力される
## 設定後
    - `sudo python run.py` （sudoでないとデバイスへのアクセスができず失敗する）
    - 停止は ctrl+c
- マネージメント用のwebサーバを立てる
- 特定リクエストの送信時にnfcを起動
- 起動後、マネージメントページにリダイレクト
- 起動後はnfcタッチ後に指定urlへpostを投げる
- 仮想のwebアプリで受信、保存する
