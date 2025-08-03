# livecoding

### ソフトウェア
- Anaconda3 https://www.anaconda.com/products/distribution
- FoxDot（ライブコーディング環境）
- SuperCollider（音響合成ソフト）https://supercollider.github.io/download

### 環境構築
1. Anaconda3初期化
```
source /Users/fukazawa/anaconda3/bin/activate
conda init zsh
```

2. Python環境（py310）有効化
```
conda activate py310
```

3. FoxDotインストール
```
pip install FoxDot
```

4. Quarkインストール
```
// SuperCollider
Quarks.install("FoxDot")
```

5. FoxDotサーバ起動
```
// SuperCollider
FoxDot.start
```

6. FoxDot起動
```
python -m FoxDot
```
