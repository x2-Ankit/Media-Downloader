import os
import yt_dlp

# 📂 Set the download folder on the Desktop
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "Music & Video")
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def get_best_formats(url):
    """Fetch best audio and top 3 video formats."""
    ydl_opts = {"quiet": True, "no_warnings": True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get("formats", [])

        best_audio = None
        best_video = []

        for fmt in formats:
            if fmt.get("acodec") != "none" and fmt.get("vcodec") == "none":  # 🎵 Audio only
                if not best_audio or (fmt.get("abr") and (best_audio.get("abr") or 0) < fmt["abr"]):
                    best_audio = fmt

            if fmt.get("vcodec") != "none" and fmt.get("acodec") == "none":  # 🎥 Video only
                if len(best_video) < 3:
                    best_video.append(fmt)
                else:
                    min_res = min(best_video, key=lambda x: x["height"])
                    if fmt["height"] > min_res["height"]:
                        best_video.remove(min_res)
                        best_video.append(fmt)

        best_video.sort(key=lambda x: x["height"], reverse=True)

        return best_audio, best_video, info.get("title", "Unknown Title")

def format_size(size):
    """Convert bytes to MB or GB."""
    if size is None:
        return "Unknown"
    size_mb = size / (1024 * 1024)
    return f"{size_mb:.2f} MB" if size_mb < 1024 else f"{size_mb / 1024:.2f} GB"

def download_video(url, format_id, title):
    """Download video and merge with best audio."""
    ydl_opts = {
        "format": f"{format_id}+bestaudio",
        "outtmpl": os.path.join(DOWNLOAD_PATH, f"{title}.mp4"),
        "quiet": True,
        "no_warnings": True,
        "merge_output_format": "mp4",
    }

    print(f"\n⏳ Downloading '{title}'... 🎬")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ Download complete 🎧")

def download_audio(url, format_id, title):
    """Download best quality audio."""
    ydl_opts = {
        "format": format_id,
        "outtmpl": os.path.join(DOWNLOAD_PATH, f"{title}.mp3"),
        "quiet": True,
        "no_warnings": True,
    }

    print(f"\n⏳ Downloading '{title}' (Audio Only) 🎵...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ Download complete 🎧")

if __name__ == "__main__":
    print("\n🎬 Video & Audio Downloader 🎬")
    print("🚀 Supports: YouTube, Instagram, Facebook, Twitter, etc.\n")

    while True:
        url = input("\n🔗 Enter video URL : > ").strip()
        if url.lower() == "exit":
            print("\n👋 Exiting... Have a great day!\n")
            break

        try:
            best_audio, best_video, title = get_best_formats(url)

            print(f"\n🎥 Available Options for {title}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            if best_audio:
                print(f"🎵 [A] Audio Only  {best_audio['abr']} kbps ({best_audio['ext']}) - {format_size(best_audio.get('filesize'))}")

            for i, vid in enumerate(best_video, start=1):
                print(f"📽️ [{i}] **{vid['height']}p** - {vid['ext']} - {vid['fps']} FPS - {format_size(vid.get('filesize'))}")

            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            choice = input("\n🎯 Select : >  ").strip().upper()

            if choice == "A" and best_audio:
                download_audio(url, best_audio["format_id"], title)
            elif choice in ["1", "2", "3"] and len(best_video) >= int(choice):
                download_video(url, best_video[int(choice) - 1]["format_id"], title)
            else:
                print("\n⚠ **Invalid selection!** Please enter a valid option.")

        except Exception as e:
            print(f"\n❌ Error ❌{e}")
