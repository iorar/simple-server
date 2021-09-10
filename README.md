# Simple greeting Server

　このサーバーは起動すると「Hello!」と言います。かわいいですね。

## 導入

全てのファイルを適当なディレクトリにcloneしてください。
Dockerfileを指定してコンテナをビルドしてください。

## 使い方

 1. Docker でコンテナをビルドします。
 2. server.pyを実行します。 コマンド: ```python server.py```
 3. サーバーから確認する場合は<http://localhost:80>にアクセスしてください。
 4. 外部から確認する場合は<http://yourdomain.example>にアクセスしてください。これはあなたが取得しているドメインに読み替えてください。
 5. 停止する場合はコンテナを停止してください。

必要があればserver.pyとstatic/hello.jsのポート指定部分を書き換えてください。
