import os
import yt_dlp
import keyboard
import time
import vlc

# Define download directory
download_folder = os.path.join(os.path.expanduser("~"), "Desktop", "music")
os.makedirs(download_folder, exist_ok=True)

# Function to download and play music
def download_and_play(song_name):
    print(f"🔍 Searching for: {song_name} ...")
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best audio quality
        'noplaylist': True,  # Avoid downloading playlists
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save format
        'quiet': True,  # Hide extra logs
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            filename = ydl.prepare_filename(info['entries'][0])
            song_title = info['entries'][0]['title']
            print(f"✅ Found: {song_title}")
            print(f"⬇️ Finished downloading ({os.path.getsize(filename) / (1024 * 1024):.2f} MB)...\n")
            return filename, song_title
        except Exception as e:
            print(f"❌ Error: {e}")
            return None, None

# Loop for continuous input
while True:
    song_name = input("\n🎵 Enter Song Name or URL: >  ").strip()
    if not song_name:
        continue

    file_path, song_title = download_and_play(song_name)
    if not file_path:
        continue
    
    # Initialize VLC player
    player = vlc.MediaPlayer(file_path)
    player.play()
    time.sleep(1)  # Give it time to start
    
    print(f"\n🎶 **Now Playing:** ⟪ {song_title} ⟫ 🎶\n")
    
    print("🎧 **Hotkeys** 🎧\n")
    print("🎵 Shift+1 → Pause / Resume")
    print("🔉 Shift+2 → Volume Down")
    print("🔊 Shift+3 → Volume Up")
    print("⏪ Shift+4 → Rewind 5 sec")
    print("⏩ Shift+6 → Forward 5 sec")
    print("⏭️ Shift+5 → Stop & Next\n")
    
    # Control music with hotkeys
    while True:
        if keyboard.is_pressed("shift+1"):  # Pause/Resume
            if player.is_playing():
                player.pause()
            else:
                player.play()
            time.sleep(0.5)
        
        if keyboard.is_pressed("shift+2"):  # Volume Down
            vol = max(player.audio_get_volume() - 10, 0)
            player.audio_set_volume(vol)
            time.sleep(0.5)
        
        if keyboard.is_pressed("shift+3"):  # Volume Up
            vol = min(player.audio_get_volume() + 10, 100)
            player.audio_set_volume(vol)
            time.sleep(0.5)

        if keyboard.is_pressed("shift+4"):  # Rewind 5 seconds
            current_time = player.get_time()
            player.set_time(max(current_time - 5000, 0))
            print(f"⏪ Rewinded: -5 sec")
            time.sleep(0.5)

        if keyboard.is_pressed("shift+6"):  # Forward 5 seconds
            current_time = player.get_time()
            player.set_time(min(current_time + 5000, player.get_length()))
            print(f"⏩ Forwarded: +5 sec")
            time.sleep(0.5)
        
        if keyboard.is_pressed("shift+5"):  # Stop and ask for next song
            player.stop()
            break
        
        # **Loop the song if it ends**
        if player.get_state() == vlc.State.Ended:
            player.stop()  # Stop current playback
            player = vlc.MediaPlayer(file_path)  # Reload the song
            player.play()  # Play it again
            print(f"\n🔁 **Looping:** ⟪ {song_title} ⟫ 🎶")
            time.sleep(1)
