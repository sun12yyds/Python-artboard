# Python artboard
# 一个好用，直接，大方的python画板程序！
# 基本
运行“画图1.py”即可体验python画板v1.1版本
# v1.1代码展示
```python
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
```
# v1.1代码功能说明
1.创建画布
```python
self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
self.canvas.pack()
```
创建一个白色背景的画布，宽度为800像素，高度为600像素。


2.工具栏
```python
self.toolbar = tk.Frame(self.root)
self.toolbar.pack()
```

创建一个工具栏，放置在画布的上方。


3.颜色选择按钮
```python
self.color_button = tk.Button(self.toolbar, text="选择颜色", command=self.choose_color)
self.color_button.pack(side=tk.LEFT)
```

创建一个按钮，用于选择绘图颜色。点击按钮时调用 方法。choose_color。

4.清除按钮
```python
self.clear_button = tk.Button(self.toolbar, text="清除画布", command=self.clear_canvas)
self.clear_button.pack(side=tk.LEFT)
```

5.颜色选择功能
```python
def choose_color(self):
    self.paint_color = askcolor(color=self.paint_color)[1]
```

6.清除画布功能
```python
def clear_canvas(self):
    self.canvas.delete("all")
```

7.绘图功能
```python
def paint(self, event):
    if self.old_x and self.old_y:
        self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, fill=self.paint_color, width=2)
    self.old_x = event.x
    self.old_y = event.y
```

8.重置画笔位置
```python
def reset(self, event):
    self.old_x = None
    self.old_y = None
```

# 欢迎贡献优化代码
# 屏幕截图
![logo](https://github.com/sun12yyds/Python-artboard/blob/main/ph/1.png)
![logo](https://github.com/sun12yyds/Python-artboard/blob/main/ph/2.png)
![logo](https://github.com/sun12yyds/Python-artboard/blob/main/ph/3.png)
![logo](https://github.com/sun12yyds/Python-artboard/blob/main/ph/4.png)

# 鸣谢
-[sunlightLT](github.com/sunlightLT)


  
