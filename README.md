🎬 Media Downloader 🚀  

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)  
[![PyInstaller](https://img.shields.io/badge/PyInstaller-5.0+-green.svg)](https://pyinstaller.org/)  

A **powerful Python-based YouTube Downloader** with support for **audio (MP3)**, **video (MP4)**, and **batch downloads**.  

---

## **📥 For End Users (EXE)**  
### **Download & Run**  
1. Download the latest **`Media Downloader.exe`** from Above.  
2. Double-click to run (no installation needed).  
3. Follow the on-screen menu to download videos/audio.  

**Features for EXE Users:**  
✅ Simple CL interface  
✅ Downloads to `Desktop/Downloads` automatically  
✅ Supports **URLs** and **song name searches**  
✅ Batch download multiple links  

---

## **👨‍💻 For Developers (Source Code)**  
### **Prerequisites**  
- Python 3.7+  
- `yt-dlp` (included in `requirements.txt`)  

### **Setup**  
1. **Clone the repo**:  
   ```sh
   git clone https://github.com/x2-Ankit/Downloader.git
   cd Downloader
   ```

2. **Install dependencies**:  
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the script**:  
   ```sh
   python downloader.py
   ```

### **🔧 Rebuild EXE with PyInstaller**  
```sh
pyinstaller --onefile --windowed --icon=icon.ico downloader.py
```
*(Outputs to `dist/` folder)*  

---

## **✨ Key Features**  
- **Smart Format Selection**: Auto-detects best audio/video quality.  
- **Batch Processing**: Download multiple URLs/songs at once.  
- **Progress Tracking**: Real-time download status.  
- **Cross-Platform**: Works on Windows, macOS, Linux (EXE for Windows only).  

---

## **🛠️ Usage Guide**  
### **Single Download**  
1. Choose `1. Enter URL` → Paste YouTube link.  
2. Select format:  
   - `A` for MP3 audio  
   - `1/2/3` for video resolutions  

### **Batch Mode**  
1. Choose `2. Batch download` → Enter multiple URLs/song names (one per line).  
2. Press **Enter twice** to start.  

### **Open Download Folder**  
- Use option `3` to quickly access downloaded files.  

---

## **📜 License**  
MIT © [x2-Ankit](https://github.com/x2-Ankit)  

---

## **📸 Preview**  
![image](https://github.com/user-attachments/assets/d688af3e-e5d7-4c81-b6d8-b3ab86c37e4b)



---

### **Need Help?**  
- **Report Bugs**: [Open an Issue](https://github.com/x2-Ankit/Downloader/issues)  
- **Contribute**: PRs welcome!  

🔗 **Repo Link**: [https://github.com/x2-Ankit/Downloader](https://github.com/x2-Ankit/Downloader)  

---

### **Notes for Developers**  
- The script handles **PyInstaller paths** via `resource_path()`.  
- Uses **threaded downloads** (`ThreadPoolExecutor`) for batch mode.  
- Outputs are saved to `~/Desktop/Downloads/`.  

---

**Let me know if you'd like to add:**  
- A troubleshooting section  
- More detailed developer docs (e.g., modifying formats)  
- Credits for dependencies (e.g., `yt-dlp`)  

🚀 Happy downloading!
