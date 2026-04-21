***家計簿アプリ***
■vscode上で実行する場合
1.ターミナルで下記コマンドを実行
  >>> python -m app

■exeファイル化して実行する場合
1.pyinstallerのインストール
  >>> pip install pyinstaller
2.exe化コマンド
  >>> pyinstaller --onefile --noconsole --add-data "db;db" app.py
3.作成したexeファイルを実行する
  C:\Users\...\household_account\dist\app.exe