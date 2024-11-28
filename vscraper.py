#!/usr/bin/env python3
import sys
import subprocess
import argparse
import os

def ensure_conda_env():
    # Check if running in the correct conda environment
    current_env = os.environ.get('CONDA_DEFAULT_ENV')
    if current_env != 'myenv':
        print("Error: This script must be run in the 'myenv' conda environment")
        print("Please activate it with: conda activate myenv")
        sys.exit(1)

def download_video(url):
    try:
        # Get the default filename that yt-dlp would use
        result = subprocess.run(['yt-dlp', '--get-filename', url], 
                              check=True, capture_output=True, text=True)
        original_filename = result.stdout.strip()
        
        # Generate a safe filename using our helper function
        safe_filename = generate_safe_filename(original_filename)
        
        # Download using the safe filename
        subprocess.run(['yt-dlp', '-o', safe_filename, url], check=True)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")
        return False
    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it in the conda environment")
        sys.exit(1)
    except OSError as e:
        print(f"System error while downloading {url}: {e}")
        return False

def generate_safe_filename(original_filename):
    base, ext = os.path.splitext(original_filename)
    
    # macOS safe limit (leaving some buffer space)
    MAX_LENGTH = 220  # 255 - buffer for safety
    
    if len(original_filename) <= MAX_LENGTH:
        return original_filename
    
    # Calculate how much we need to truncate the base name
    # Account for extension length and a separator
    available_space = MAX_LENGTH - len(ext)
    truncated_base = base[:available_space]
    
    return f"{truncated_base}{ext}"

def main():
    ensure_conda_env()
    
    parser = argparse.ArgumentParser(description='Download videos using yt-dlp')
    parser.add_argument('-f', '--file', help='Text file containing URLs (one per line)')
    parser.add_argument('urls', nargs='*', help='URLs to download')
    
    args = parser.parse_args()
    
    urls = []
    
    # Read URLs from file if specified
    if args.file:
        try:
            with open(args.file, 'r') as f:
                urls.extend(line.strip() for line in f if line.strip())
        except FileNotFoundError:
            print(f"Error: File {args.file} not found")
            sys.exit(1)
    
    # Add URLs from command line arguments
    urls.extend(args.urls)
    
    if not urls:
        print("Error: No URLs provided. Use -h for help")
        sys.exit(1)
    
    # Download each video sequentially
    successful = 0
    failed = 0
    for url in urls:
        print(f"Downloading: {url}")
        if download_video(url):
            successful += 1
        else:
            failed += 1
            
    print(f"\nDownload complete. Successfully downloaded: {successful}, Failed: {failed}")

if __name__ == "__main__":
    main()
