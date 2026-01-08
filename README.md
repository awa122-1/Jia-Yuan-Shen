# Genshin Impact Security System（恶搞项目）

一个基于 **Python + Tkinter** 的恶搞窗口程序  
❌ 关不掉窗口  
😂 随机嘲讽文本  
⌨️ 隐藏快捷键强制退出  

> ⚠️ 本项目仅用于学习与娱乐，请勿用于`恶 意`用途

---

## ✨ 功能特点

- 使用 Tkinter 创建弹窗 GUI
- 禁止正常关闭窗口（点 ❌ 会生成更多窗口）
- 随机嘲讽文本（TAUNTS）
- 输入指定关键词才能关闭窗口
- 全局快捷键强制退出程序
- 支持 PyInstaller 打包（含 ico 图标）

---

## 🖥 运行环境

- Python **3.8+**
- Windows（使用了 `keyboard` 全局热键）

---

## 📦 依赖库

```bash
pip install keyboard

##cmd里

```bash
pyinstaller --noconsole --onefile --uac-admin --add-data "genshin.ico;." --version-file file_version_info.txt -i genshin.ico awa.py


声明：genshin.ico可有可无


