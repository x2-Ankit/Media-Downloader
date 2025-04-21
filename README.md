# 🎬 Video & Audio Downloader

A simple Python-based downloader that allows you to download high-quality **audio** or **video** from YouTube and other platforms like Instagram, Facebook, Twitter, etc. It uses `yt_dlp` under the hood and provides the **best available formats**, with easy-to-follow CLI interaction.

---

## ⚙️ Features

- 📥 Download **audio only** (best quality)
- 📹 Download top 3 **video formats**
- 🎧 Merges video with best audio (for full video download)
- 💾 Saves files in a custom folder: `~/Desktop/Music & Video`
- 🌐 Supports multiple platforms
- 🧠 Automatically picks the best formats available
- 💡 Neatly shows file sizes and quality info

---

## 📦 Requirements

- Python 3.6 or higher
- [`yt_dlp`](https://github.com/yt-dlp/yt-dlp)

Install with pip:

```bash
pip install yt-dlp
```

---

## 🚀 How to Use

1. **Run the script**:

```bash
python downloader.py
```

2. **Paste the video URL** when prompted.

3. **Select an option**:
   - `A` → Download best audio only
   - `1`/`2`/`3` → Download one of the top 3 video formats with audio merged

4. **Exit anytime** by typing `exit`.

---

## 📁 Output Location

All downloaded files will be saved to:

```
~/Desktop/Music & Video
```

---

## 🧠 Format Selection Logic

- 🎵 **Best Audio**: Highest available audio bitrate (abr)
- 🎥 **Top 3 Videos**: Based on resolution (height) and FPS
- 📽️ Videos are merged with best available audio using `yt_dlp`

---

## 💻 Example Output

```
🎬 Video & Audio Downloader 🎬
🚀 Supports: YouTube, Instagram, Facebook, Twitter, etc.

🔗 Enter video URL : > https://youtube.com/...

🎥 Available Options for Some Cool Video
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎵 [A] Audio Only  160 kbps (m4a) - 4.83 MB
📽️ [1] 1080p - mp4 - 30 FPS - 23.54 MB
📽️ [2] 720p - mp4 - 30 FPS - 15.02 MB
📽️ [3] 480p - mp4 - 30 FPS - 8.45 MB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📌 Note

- If file size shows as `Unknown`, it may still be downloaded normally.
- All downloaded videos are saved as `.mp4`, and audios as `.mp3`.

---

## 🛠️ Author

**Ankit Tripathy / x2-Ankit**  

## 📄 License

This project is open source and available under the [MIT License]