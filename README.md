# PythonのTurtle Graphicsで日本国旗描画プロジェクト

## プロジェクト内容
PythonのTurtle Graphicsライブラリを使用して日本国旗を描画するグラフィックスプロジェクトです。座標系の理解、図形描画、色の設定、塗りつぶし機能など、2Dグラフィックスプログラミングの基礎技術を学習することを目的として実装しました。

## プロジェクト構成

```
japanese-flag-turtle-graphics/
├── flag_drawer.py           # メインプログラム
├── requirements.txt         # 依存関係管理
├── README.md               # プロジェクト説明書
└── .gitignore              # Git除外ファイル設定
```

## 必要要件/開発環境
- **Python 3.6以上**
- **VSCode** (開発環境)
- **Git** (バージョン管理)

### 使用ライブラリ
- **turtle** 2Dグラフィックス描画（Python標準ライブラリ）

## 機能
- **キャンバス初期化** 描画ウィンドウの設定と背景色指定
- **座標系設定** 中央原点の数学座標系を採用
- **図形描画** circle()関数による正確な円形描画
- **色彩管理** 日本国旗公式カラーコード(#E60012)の適用
- **塗りつぶし処理** begin_fill()とend_fill()による図形塗りつぶし
- **比率計算** 日本国旗の正式な縦横比(2:3)に基づくサイズ調整
- **描画品質最適化** ペンサイズと描画速度の調整
- **ユーザーインタラクション** クリック終了機能

## 実行方法

### 1. リポジトリのクローン
```bash
git clone https://github.com/yourusername/japanese-flag-turtle-graphics.git
cd japanese-flag-turtle-graphics
```

### 2. 仮想環境の作成・アクティベート
**Windows**
```bash
python -m venv myenv
myenv\Scripts\activate
```

**macOS**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. プログラムの実行
```bash
python flag_drawer.py
```

実行後、800x600ピクセルのウィンドウが開き、中央に日本国旗の赤い円が描画されます。
ウィンドウをクリックすると終了します。

## 技術的特徴
* **オブジェクト指向設計** FlagDrawerクラスによる機能の整理
* **座標計算** 数学的な比率計算による正確な配置
* **グラフィックス制御** Turtle/Screenオブジェクトの適切な管理
* **標準ライブラリ活用** 外部依存なしの軽量実装

## 開発者
YuYu