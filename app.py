#!/usr/bin/env python3
"""
シンプルなWeb APIシステム
Simple Web API System
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# データストア（メモリ内）
items = []
item_id_counter = 0


@app.route('/', methods=['GET'])
def index():
    """APIのルート - ウェルカムメッセージを返す"""
    return jsonify({
        'message': 'Welcome to Simple Web API',
        'endpoints': {
            'GET /': 'This welcome message',
            'GET /items': 'Get all items',
            'GET /items/<id>': 'Get item by ID',
            'POST /items': 'Create new item (requires JSON body with "name" field)',
            'DELETE /items/<id>': 'Delete item by ID'
        }
    })


@app.route('/items', methods=['GET'])
def get_items():
    """全アイテムを取得"""
    return jsonify({
        'items': items,
        'count': len(items)
    })


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """指定されたIDのアイテムを取得"""
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404


@app.route('/items', methods=['POST'])
def create_item():
    """新しいアイテムを作成"""
    global item_id_counter
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Bad request - name field is required'}), 400
    
    item_id_counter += 1
    new_item = {
        'id': item_id_counter,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """指定されたIDのアイテムを削除"""
    global items
    # アイテムが存在するか確認
    item_exists = any(item['id'] == item_id for item in items)
    if not item_exists:
        return jsonify({'error': 'Item not found'}), 404
    
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'})


if __name__ == '__main__':
    # デバッグモードは開発環境のみで使用してください
    # Debug mode should only be used in development environment
    app.run(debug=True, host='0.0.0.0', port=5000)
