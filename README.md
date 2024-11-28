# VScraper

A Python script for safely downloading videos using yt-dlp. Key features:
- Handles long filenames safely on macOS
- Enforces correct conda environment usage
- Simple command line interface for single or batch downloads

## Prerequisites

- Python 3.x
- Anaconda or Miniconda installed
- Internet connection
- yt-dlp (installed via conda environment)

## Setup

1. First, create and activate the conda environment:
   ```bash
   conda create -n myenv python=3.9
   conda activate myenv
   ```

2. Install required packages:
   ```bash
   conda install -c conda-forge yt-dlp
   ```

## Usage

### Single URL Download
To download a single video:
```bash
python vscraper.py "https://www.example.com/video-url"
```

### Multiple URLs
To download multiple videos directly:
```bash
python vscraper.py "https://www.example.com/video1" "https://www.example.com/video2"
```

### Batch Download
To download multiple videos from a text file:
```bash
python vscraper.py -f "urls.txt"
```
The text file should contain one URL per line.

### Options
- `-f`, `--file`: Path to text file containing URLs (one per line)
