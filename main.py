import os
import sys
import yt_dlp
from concurrent.futures import ThreadPoolExecutor, as_completed

# Handle resource path for bundled executable
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Set download path on Desktop
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "Downloads")
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def format_size(size):
    """Convert bytes to MB or GB."""
    if size is None:
        return "Unknown"
    size_mb = size / (1024 * 1024)
    return f"{size_mb:.2f} MB" if size_mb < 1024 else f"{size_mb / 1024:.2f} GB"

def get_best_formats(url):
    """Fetch best audio and top 3 video formats with optimized format filtering."""
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": False,
        "simulate": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get("formats", [])
            
            # Pre-filter formats to reduce processing
            audio_formats = [f for f in formats if f.get("acodec") != "none" and f.get("vcodec") == "none"]
            video_formats = [f for f in formats if f.get("vcodec") != "none" and f.get("acodec") == "none"]
            
            # Get best audio
            best_audio = max(audio_formats, key=lambda x: x.get("abr", 0), default=None)
            
            # Get top 3 videos by resolution
            best_video = sorted(
                video_formats,
                key=lambda x: (x.get("height", 0), x.get("fps", 0)),
                reverse=True
            )[:3]
            
            return best_audio, best_video, info.get("title", "Unknown Title")
    except Exception as e:
        print(f"❌ Error processing {url}: {str(e)}")
        return None, None, None

def download_audio(url, format_id, title):
    try:
        ydl_opts = {
            "format": format_id,
            "outtmpl": os.path.join(DOWNLOAD_PATH, f"{title}.mp3"),
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
            "socket_timeout": 30,
            "postprocessors": [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        print(f"\n⏳ Downloading '{title}' (Audio Only) 🎵...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Audio download complete 🎧")
    except Exception as e:
        print(f"❌ Error downloading audio: {str(e)}")

def download_video(url, format_id, title):
    try:
        ydl_opts = {
            "format": f"{format_id}+bestaudio",
            "outtmpl": os.path.join(DOWNLOAD_PATH, f"{title}.mp4"),
            "quiet": True,
            "no_warnings": True,
            "merge_output_format": "mp4",
            "noprogress": True,
            "socket_timeout": 30,
        }
        print(f"\n⏳ Downloading '{title}'... 🎬")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Video download complete 🎬")
    except Exception as e:
        print(f"❌ Error downloading video: {str(e)}")

def download_by_search(song_name):
    print(f"🔍 Searching for: {song_name} ...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s'),
        'quiet': True,
        'socket_timeout': 30,
        'noprogress': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            filename = ydl.prepare_filename(info['entries'][0])
            song_title = info['entries'][0]['title']
            print(f"✅ Downloaded: {song_title} ({format_size(os.path.getsize(filename))})")
    except Exception as e:
        print(f"❌ Error downloading '{song_name}': {e}")

def batch_download(items):
    """Process multiple downloads in parallel with thread pool"""
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for i, item in enumerate(items, 1):
            print(f"\n🎶 [{i}/{len(items)}] Processing: {item}")
            futures.append(executor.submit(download_by_search, item))
        
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"❌ Error in batch download: {e}")

def menu():
    print("\n🎬 YouTube Downloader 🎬")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("1. 🔗 Enter URL")
    print("2. 🎵 Batch download (Multiple URLs/Song Names)")
    print("3. 📂 Open download folder")
    print("4. ❌ Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # Check if running as executable
    if getattr(sys, 'frozen', False):
        try:
            if not os.path.exists(DOWNLOAD_PATH):
                os.makedirs(DOWNLOAD_PATH)
        except Exception as e:
            print(f"Error creating download folder: {e}")
    
    while True:
        clear_screen()
        menu()
        choice = input("\n🎯 Choose option [1/2/3/4]: ").strip()

        if choice == "1":
            clear_screen()
            url = input("\n🔗 Enter YouTube URL: ").strip()
            if not url:
                input("⚠️ Please enter a valid URL. Press Enter to continue...")
                continue
            
            best_audio, best_video, title = get_best_formats(url)
            if not title:
                input("\n⚠️ Error processing URL. Press Enter to continue...")
                continue
                
            clear_screen()
            print(f"\n🎥 Available Options for: {title}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            if best_audio:
                print(f"🎵 [A] Audio Only (MP3) {best_audio['abr']} kbps - {format_size(best_audio.get('filesize'))}")
            for i, vid in enumerate(best_video, start=1):
                print(f"📽️ [{i}] {vid['height']}p {vid['ext'].upper()} - {vid['fps']} FPS - {format_size(vid.get('filesize'))}")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            sel = input("\n🎯 Select format [A/1/2/3] or [M] to go back: ").strip().upper()
            if sel == "A" and best_audio:
                download_audio(url, best_audio["format_id"], title)
            elif sel in ["1", "2", "3"] and len(best_video) >= int(sel):
                download_video(url, best_video[int(sel) - 1]["format_id"], title)
            elif sel == "M":
                continue
            else:
                print("\n⚠️ Invalid selection.")
            input("\nPress Enter to continue...")

        elif choice == "2":
            clear_screen()
            print("\n🎵 Enter multiple YouTube URLs or song names (one per line).")
            print("Press Enter twice to start downloading.\n")
            input_lines = []
            while True:
                line = input()
                if line.strip() == "":
                    if input_lines:
                        break
                    else:
                        print("⚠️ Please enter at least one URL/song name")
                        continue
                input_lines.append(line.strip())

            clear_screen()
            batch_download(input_lines)
            input("\n✅ All downloads completed. Press Enter to continue...")

        elif choice == "3":
            try:
                os.startfile(DOWNLOAD_PATH) if os.name == 'nt' else os.system(f'open "{DOWNLOAD_PATH}"')
            except Exception as e:
                print(f"❌ Error opening folder: {e}")
                input("Press Enter to continue...")

        elif choice == "4":
            print("\n👋 Exiting... Thank you for using YouTube Downloader!")
            break

        else:
            input("⚠️ Invalid input. Please enter 1, 2, 3 or 4. Press Enter to continue...")                                                 