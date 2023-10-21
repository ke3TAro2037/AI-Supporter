import discord
from discord.ext import commands
import mysql.connector

db_config = {
    'host': 'データベースのホスト名',
    'user': 'データベースのユーザー名',
    'password': 'データベースのパスワード',
    'database': 'データベース名',
}

# BOTのトークンを取得します
token = 'Discord-BOTのトークン'

# BOTのインスタンスを生成
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# 応答するチャンネルがあるカテゴリーを指定します
target_categories = ['テキストチャンネル', 'tickets']
# サポート側ロールを定義
required_roles = ["運営", "管理者"]


@bot.event
async def on_message(message):

  # 自分自身へのメッセージには反応しないようにします
  if message.author == bot.user:
    return

  # メッセージが送信されたチャンネルを取得します
  channel = message.channel

  # チャンネルがカテゴリーに所属していて、そのカテゴリー名が目標のカテゴリー名と一致する場合にのみ「あ」とリプライします
  if isinstance(channel, discord.TextChannel) and channel.category:
    if channel.category.name in target_categories:
      # ユーザーのロールを取得
      member = message.author

      # いずれかの特定のロールを持つユーザー
      has_required_role = any(role in [r.name for r in member.roles] for role in required_roles)
      
      if has_required_role:
        # チャンネルのアクセス権限を削除
        # MariaDBに接続
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()

        # MariaDBのテーブルから保存されたチャンネルIDを取得
        channel_id = message.channel.id
        db_cursor.execute('INSERT INTO saved_channels (channel_id) VALUES (%s)', (channel_id,))
        db_connection.commit()

        # MariaDBの接続を閉じる
        db_cursor.close()
        db_connection.close()
        return
        
      else:
        
        # MariaDBに接続
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()
        
bot.run(token)
