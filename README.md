# AIサポーター

このリポジトリでは、AIによるチケット対応を行うDiscord Botのコードを提供しています。

## 機能概要

- 特定のカテゴリー内のチャンネルで送信されたメッセージを監視します。
- サポート対応を行うユーザーのロールを確認し、メッセージが送信されたチャンネルIDをデータベースに保存します。

## 必要な環境

- Python 3.x
- discord.py
- mysql-connector-python

## データベース構造

以下のようなテーブルをデータベースに作成してください。

```sql
CREATE TABLE saved_channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    channel_id BIGINT UNIQUE
);
```

## 設定
main.py内の以下の変数を適切に設定してください。
```
db_config: データベース接続情報
token: Discord Botのトークン
target_categories: 監視するカテゴリー名
required_roles: サポート対応を行うユーザーのロール名
```

## 実行方法
```bash
python main.py
```
このコマンドでBotを起動します。
