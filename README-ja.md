# Aphrodite FastAPI Scaffold

[English](README.md) | [简体中文](README-zh.md) | [日本語](README-ja)

Aphrodite は、[Fastapi-skeleton](https://github.com/kaxiluo/fastapi-skeleton)
をベースに開発されたテンプレートプロジェクトで、開発者がフレームワークの使用フローを迅速に理解し、深く学ぶことを目的としています。このプロジェクトは、一般的な開発シーンを網羅した包括的なサンプルコードと設定を提供し、学習と実践をサポートします。さらに、Aphrodite
にはコンテナーデプロイメントテンプレートも含まれており、現代のクラウド環境でプロジェクトを簡単にデプロイおよび管理できるようになっており、開発者がアプリケーションを効率的に構築および公開する手助けをします。

## 技術スタック

| 技術                                                     | 説明                                                  |
|--------------------------------------------------------|-----------------------------------------------------|
| [APScheduler](https://github.com/agronholm/APScheduer) | Python の定期タスクスケジューラー、バックグラウンドジョブのスケジュールをサポート        |
| [FastAPI](https://fastapi.tiangolo.com/)               | 高性能な Web フレームワーク、非同期操作をサポートし、API を迅速に構築             |
| [JOSE](https://github.com/python-jose/jose)            | JSON Web トークン (JWT) を処理するための Python ライブラリ           |
| [Loguru](https://github.com/Delgan/loguru)             | シンプルな Python ロギングライブラリ、使いやすいログ記録とフォーマットのサポート        |
| [Peewee](http://docs.peewee-orm.com/en/latest/)        | シンプルな Python ORM フレームワーク、複数のデータベース操作をサポート           |
| [Starlette](https://www.starlette.io/)                 | Web アプリケーションを構築するための高性能なフレームワーク、FastAPI のコア部分       |
| [Uvicorn](https://www.uvicorn.org/)                    | 高性能な ASGI サーバー、非同期 Python アプリケーションの実行をサポート          |
| [psycopg2](https://github.com/psycopg/psycopg2)        | PostgreSQL データベースアダプター、Python と PostgreSQL の接続をサポート |
| [Passlib](https://passlib.readthedocs.io/en/stable/)   | パスワード暗号化ライブラリ、複数のハッシュアルゴリズムと暗号化方式をサポート              |
| [Pydantic](https://pydantic-docs.helpmanual.io/)       | データ検証と解析ライブラリ、Python の型注釈に基づく検証と解析を行う               |
| [Python-JOSE](https://github.com/mpdavis/python-jose)  | JSON Web トークン (JWT) の生成と解析を行うライブラリ、暗号化サポート          |
| [Redis-py](https://github.com/andymccurdy/redis-py)    | Python クライアントライブラリ、Redis データベースの操作と接続               |

## 特徴

- **ユーザー認証と認可**：基本的なユーザーログインと権限付与機能を提供します。
- **分散ロック**：Redisをベースにした分散ロックを実装し、分散環境下でのリソースの安全性を確保します。
- **ミドルウェアサポート**：認証、リクエストログ、CORS処理など、よく使われるミドルウェアを内蔵しています。
- **統一された出力フォーマット**：簡単に使えるAPI Resultの統一出力方式を提供し、APIのレスポンスフォーマットを標準化して、インターフェースの一貫性を向上させます。
- **APIモジュール設計**：モジュール化されたAPI設計をサポートし、拡張と保守が容易です。
- **Swaggerドキュメント統合**：APIドキュメントを自動生成し、フロントエンド開発とテストを容易にします。

## ディレクトリ構造

```
.
├── app/                  # アプリケーションのコアコード
├── bin/                  # 実行可能スクリプト
├── bootsrap/             # ブートファイル
├── database/             # データベース関連
├── deploy/               # デプロイ関連ファイル
├── docs/                 # プロジェクトドキュメント
├── routes/               # ルートファイル
├── storage/              # ファイルストレージ
├── tests/                # テストファイル
└── README.md             # プロジェクト説明
```

## 本地运行

```bash
# 1. プロジェクトのコードリポジトリをクローン
git clone https://github.com/lniche/aphrodite-py.git
cd aphrodite-py

# 2. 設定ファイルの準備
cd config
mv .env.example .env

# 3. 依存関係のインストール
# Python 環境がインストールされていることを確認してください。conda の使用を推奨します。
pip install -r requirements.txt

# 4. データベースの初期化
database/migrations/V1.0.0__initial_schema.sql

# 5. サービスの起動
uvicorn main:app
```

## リポジトリの活動

![Alt](https://repobeats.axiom.co/api/embed/57c3b523ffb088038484a6b3883890a2615b3fa5.svg "Repobeats analytics image")

## ライセンス

このプロジェクトは MIT ライセンスに従っています。

## 感謝の意

すべてのコントリビューターとサポーターに感謝します。皆さんのご支援が私たちにとって非常に重要です！
