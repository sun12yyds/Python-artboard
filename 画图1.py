import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简单画板程序")

        # 创建一个画布
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack()

        # 创建工具栏
        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack()

        # 创建颜色选择按钮
        self.color_button = tk.Button(self.toolbar, text="选择颜色", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        # 创建清除按钮
        self.clear_button = tk.Button(self.toolbar, text="清除画布", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)

        self.paint_color = "black"

        # 绑定鼠标事件
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # 设置画笔初始位置
        self.old_x = None
        self.old_y = None

    def choose_color(self):
        self.paint_color = askcolor(color=self.paint_color)[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, fill=self.paint_color, width=2)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()