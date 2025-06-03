import turtle as tl


class FlagDrawer:
    """日本国旗描画クラス"""
    
    def __init__(self, canvas_width=800, canvas_height=600):
        """
        初期化メソッド
        
        Args:
            canvas_width (int): キャンバスの幅
            canvas_height (int): キャンバスの高さ
        """
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.turtle_obj = None
        self.screen_obj = None
        
    def setup_canvas(self):
        """
        描画キャンバスとTurtleオブジェクトの初期設定
        """
        # Screenオブジェクトの作成と設定
        self.screen_obj = tl.Screen()
        self.screen_obj.setup(width=self.canvas_width, height=self.canvas_height)
        self.screen_obj.bgcolor("white")
        self.screen_obj.title("日本国旗 - Turtle Graphics")
        
        # Turtleオブジェクトの作成と設定
        self.turtle_obj = tl.Turtle()
        self.turtle_obj.speed(3)
        self.turtle_obj.shape("turtle")
        
    def configure_screen_settings(self):
        """
        画面の詳細設定を行う
        """
        # ウィンドウの位置調整
        self.screen_obj.setup(width=self.canvas_width, 
                             height=self.canvas_height, 
                             startx=100, 
                             starty=100)
        
        # 座標系の設定
        self.screen_obj.setworldcoordinates(-400, -300, 400, 300)
        
        # アニメーション速度の調整
        self.screen_obj.tracer(1, 10)
        
    def configure_turtle_settings(self):
        """
        Turtleオブジェクトの詳細設定
        """
        # 描画速度の設定（1-10、10が最速）
        self.turtle_obj.speed(5)
        
        # ペンの初期設定
        self.turtle_obj.pensize(2)
        self.turtle_obj.color("red")
        
        # 初期位置の設定
        self.turtle_obj.penup()
        self.turtle_obj.home()  # 原点(0,0)に移動
        self.turtle_obj.pendown()
        
        # 亀の向きを北向き（上向き）に設定
        self.turtle_obj.setheading(90)
        
    def initialize_drawing_environment(self):
        """
        描画環境の完全な初期化
        """
        self.setup_canvas()
        self.configure_screen_settings()
        self.configure_turtle_settings()
        
        print("描画環境の初期化が完了しました")
        print(f"キャンバスサイズ: {self.canvas_width} x {self.canvas_height}")
        print("日本国旗の描画準備完了")
        
    def draw_circle_flag(self, radius=100):
        """日本国旗の赤い円を描画"""
        # 円の描画開始位置を設定
        self.turtle_obj.penup()
        self.turtle_obj.goto(0, -radius)  # 円の中心から半径分下に移動
        self.turtle_obj.pendown()
        
        # 塗りつぶしの色を設定
        self.turtle_obj.fillcolor("#E60012")  # 日本国旗の正式な赤色
        self.turtle_obj.pencolor("#E60012")
        
        # 塗りつぶし開始
        self.turtle_obj.begin_fill()
        
        # 円を描画
        self.turtle_obj.circle(radius)
        
        # 塗りつぶし終了
        self.turtle_obj.end_fill()
        
    def calculate_flag_proportions(self):
        """日本国旗の正式な比率に基づいてサイズを計算"""
        # 日本国旗の比率は縦2：横3
        flag_width = min(self.canvas_width * 0.7, 600)  # キャンバスの70%またはmax600px
        flag_height = flag_width * (2/3)  # 縦横比2:3
        
        # 円の直径は旗の縦の長さの3/5
        circle_diameter = flag_height * 0.6
        circle_radius = circle_diameter / 2
        
        return {
            'flag_width': flag_width,
            'flag_height': flag_height,
            'circle_radius': circle_radius
        }
        
    def center_drawing_position(self):
        """描画位置を画面中央に調整"""
        # 亀を中央の原点に移動
        self.turtle_obj.penup()
        self.turtle_obj.goto(0, 0)
        
        # 描画の向きをリセット
        self.turtle_obj.setheading(0)  # 右向きに設定
        
        print("描画位置を中央に設定しました")
        
    def draw_complete_flag(self):
        """完全な日本国旗を描画"""
        # 国旗の比率を計算
        proportions = self.calculate_flag_proportions()
        
        # 描画位置を調整
        self.center_drawing_position()
        
        # 赤い円を描画
        self.draw_circle_flag(radius=proportions['circle_radius'])
        
        # 描画完了メッセージ
        print(f"日本国旗の描画が完了しました")
        print(f"円の半径: {proportions['circle_radius']:.1f}px")
        
        # 亀を隠す
        self.turtle_obj.hideturtle()
        
    def configure_turtle_settings(self):
        """亀オブジェクトの設定"""
        # 描画速度を設定（1が最遅、10が最速）
        self.turtle_obj.speed(6)  # 少し速くして描画時間を短縮
        
        # ペンの設定
        self.turtle_obj.pensize(1)  # 細い線で輪郭をきれいに
        self.turtle_obj.color("red")
        
        # 開始位置を設定
        self.turtle_obj.penup()
        self.turtle_obj.home()  
        self.turtle_obj.pendown()
        
        # 亀の向きを右向きに設定
        self.turtle_obj.setheading(0)  # 円描画のため右向きに変更
        
def main():
    """メイン実行関数"""
    print("=== 日本国旗描画プロジェクト ===")
    # print("Turtle Graphicsライブラリを使用した国旗描画")
    
    # FlagDrawerオブジェクトの作成
    flag_drawer = FlagDrawer(canvas_width=800, canvas_height=600)
    
    # 描画環境の初期化
    flag_drawer.initialize_drawing_environment()
    
    # 日本国旗を描画
    flag_drawer.draw_complete_flag()
    
    # ウィンドウを開いたまま保持
    print("描画ウィンドウが開きました。ウィンドウをクリックして閉じてください。")
    flag_drawer.screen_obj.exitonclick()


if __name__ == "__main__":
    main()