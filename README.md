# VScraper2

A Python script for safely downloading videos using yt-dlp. Key features:
- Handles long filenames safely on macOS
- Enforces correct conda environment usage
- Simple command line interface for single or batch downloads
- Forces MP4 output format
- Restricts filenames for maximum compatibility

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
python vscraper2.py "https://www.example.com/video-url"
```

### Multiple URLs
To download multiple videos directly:
```bash
python vscraper2.py "https://www.example.com/video1" "https://www.example.com/video2"
```

### Batch Download
To download multiple videos from a text file:
```bash
python vscraper2.py -f "urls.txt"
```
The text file should contain one URL per line.

### Options
- `-f`, `--file`: Path to text file containing URLs (one per line)
- `-h`, `--help`: Display help message and usage information

## Examples
```bash
# Display help and usage information
python vscraper2.py --help

# Download a single video
python vscraper2.py "https://www.example.com/video-url"
```
