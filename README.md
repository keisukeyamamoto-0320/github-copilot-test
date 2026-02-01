# github-copilot-test

シンプルなWeb APIシステム / Simple Web API System

## 概要 / Overview

PythonとFlaskを使用したシンプルなWeb APIシステムです。
A simple Web API system using Python and Flask.

## セットアップ / Setup

1. 依存関係をインストール / Install dependencies:
```bash
pip install -r requirements.txt
```

2. アプリケーションを起動 / Run the application:
```bash
python app.py
```

サーバーは `http://localhost:5000` で起動します。
The server will start at `http://localhost:5000`.

### 環境変数 / Environment Variables

- `FLASK_DEBUG`: デバッグモードの有効/無効 (デフォルト: True) / Enable/disable debug mode (default: True)
- `FLASK_HOST`: バインドするホスト (デフォルト: 127.0.0.1) / Host to bind to (default: 127.0.0.1)
- `FLASK_PORT`: ポート番号 (デフォルト: 5000) / Port number (default: 5000)

**注意**: 本番環境では `FLASK_DEBUG=False` を設定してください。
**WARNING**: Set `FLASK_DEBUG=False` in production environments.

例 / Example:
```bash
FLASK_DEBUG=False FLASK_HOST=0.0.0.0 FLASK_PORT=8080 python app.py
```

## API エンドポイント / API Endpoints

- `GET /` - ウェルカムメッセージとエンドポイント一覧 / Welcome message and endpoint list
- `GET /items` - 全アイテムを取得 / Get all items
- `GET /items/<id>` - 指定IDのアイテムを取得 / Get item by ID
- `POST /items` - 新しいアイテムを作成 / Create new item
  - Request body: `{"name": "item name", "description": "optional description"}`
- `DELETE /items/<id>` - 指定IDのアイテムを削除 / Delete item by ID

## 使用例 / Usage Examples

### アイテムを作成 / Create an item:
```bash
curl -X POST http://localhost:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Sample Item", "description": "This is a test item"}'
```

### 全アイテムを取得 / Get all items:
```bash
curl http://localhost:5000/items
```

### 特定のアイテムを取得 / Get a specific item:
```bash
curl http://localhost:5000/items/1
```

### アイテムを削除 / Delete an item:
```bash
curl -X DELETE http://localhost:5000/items/1
```