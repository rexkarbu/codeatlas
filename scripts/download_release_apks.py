import os
import sys
import time
import urllib.request

DEST_DIR = r"C:\Users\Dimdim\.gemini\antigravity-ide\brain\46ec7035-1b4f-4791-9793-da903bdf6cc0\scratch\verify_releases"
os.makedirs(DEST_DIR, exist_ok=True)

URLS = {
    "v1.0.0": "https://github.com/rexkarbu/codeatlas/releases/download/v1.0.0/CodeAtlas.apk",
    "v1.0.1": "https://github.com/rexkarbu/codeatlas/releases/download/v1.0.1/CodeAtlas.apk",
}

def download_file(tag, url):
    dest_path = os.path.join(DEST_DIR, f"CodeAtlas_{tag}.apk")
    print(f"[{tag}] Downloading from {url} to {dest_path}...")
    
    # Try downloading with retry
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            )
            with urllib.request.urlopen(req, timeout=120) as resp, open(dest_path, "wb") as out:
                total_size = int(resp.headers.get("content-length", 0))
                downloaded = 0
                block_size = 1024 * 1024
                start_time = time.time()
                while True:
                    chunk = resp.read(block_size)
                    if not chunk:
                        break
                    out.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        pct = (downloaded / total_size) * 100
                        mb = downloaded / (1024 * 1024)
                        tot_mb = total_size / (1024 * 1024)
                        print(f"[{tag}] {mb:.1f}MB / {tot_mb:.1f}MB ({pct:.1f}%)", end="\r", flush=True)
                elapsed = time.time() - start_time
                print(f"\n[{tag}] Downloaded {downloaded} bytes in {elapsed:.1f}s.")
                if total_size > 0 and downloaded < total_size:
                    raise IOError(f"Incomplete download: {downloaded} < {total_size}")
                return dest_path
        except Exception as e:
            print(f"\n[{tag}] Attempt {attempt} failed: {e}")
            time.sleep(3)
    raise RuntimeError(f"Failed to download {tag} after 3 attempts")

if __name__ == "__main__":
    for tag, url in URLS.items():
        download_file(tag, url)
    print("\nAll downloads finished successfully!")
