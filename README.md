# 📥 YouTube Video/Audio Downloader (Command-Line)

A simple and efficient command-line based YouTube downloader using `yt-dlp`.

---

## ⚙️ Features

- 🔗 Accepts YouTube video URLs or search queries
- 🎵 Option to download audio only (MP3)
- 📽️ Option to download best available video (MP4)
- 📂 Custom download directory
- 🧠 Auto-detects type (audio/video) based on input
- 💻 No GUI — pure command-line speed and simplicity

---

## 🔧 How to Use

1. **Install Requirements**
   ```bash
   pip install yt-dlp
   ```

2. **Run the script**
   ```bash
   python yt_downloader.py
   ```

3. **Follow the prompts**:
   - Paste YouTube link or search query
   - Choose download type: audio/video
   - Set your download location

---

## 🛠 Build `.exe` with Custom Icon

If you want to create a `.exe` version of this script with a **custom icon**:

### ✅ Requirements:
- Python 3.x
- PyInstaller
- `.ico` file for icon

### 🔨 Build Command:
```bash
pyinstaller --onefile --icon=icon.ico yt_downloader.py
```

- Output will be inside the `dist/` folder
---

## 👨‍💻 For Developers

If you'd like to view or modify the source code:

- Download the `yt_downloader.py` file
- Customize it to fit your needs
- Recompile to `.exe` using the steps above

You're free to tweak it and extend its functionality however you want!

---
## 🧊 Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the powerful backend

## 📄 License
