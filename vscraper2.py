#!/usr/bin/env python3
"""
VScraper - Video Download Script
A utility for safely downloading videos using yt-dlp with proper filename handling
and conda environment management.
Author: John Engates
License: MIT
"""
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
        # Use yt-dlp with options to restrict filename length and handle special characters
        subprocess.run([
            'yt-dlp',
            '-o', '%(title).100B-%(id)s.%(ext)s',  # Limit title to 100 chars + video ID
            '--restrict-filenames',  # Replace special chars with underscore
            '--no-part',  # Don't use .part files
            '--no-mtime',  # Don't use modification time
            url
        ], check=True)
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
    """
    This function is kept for reference but no longer used directly
    as we're handling filename safety through yt-dlp options
    """
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
    
    parser = argparse.ArgumentParser(
        description='Download videos using yt-dlp with safe filename handling'
    )
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
        print(f"\nDownloading: {url}")
        if download_video(url):
            successful += 1
            print(f"Successfully downloaded: {url}")
        else:
            failed += 1
            print(f"Failed to download: {url}")
    
    print(f"\nDownload complete. Successfully downloaded: {successful}, Failed: {failed}")

if __name__ == "__main__":
    main()