# RSTP Viewer

## Introduction

RSTP Viewer is a simple tool that allows you to view multiple RTSP (Real-Time Streaming Protocol) streams simultaneously. This tool is configured using a `.env` file, providing an easy and customizable way to manage multiple camera feeds.

## Getting Started

### Prerequisites

Before using RSTP Viewer app, you must install required dependencies:

- [python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

- requirements.txt

  ```bash
  pip install -r requirements.txt
  ```

### Installation

1. Clone the RSTP Viewer repository to your local machine:

   ```bash
   git clone https://github.com/brunolemos06/RSTP-viewer.git
   cd RSTP-viewer
    ```
2. Create a .env file in the project root and configure it with your camera names and RTSP URLs:

   ```bash
    NAMES=CAM1,CAM2
    RTSP_URLS=rtsp://example1,rtsp://example2
    ```

3. Save the .env file.

4. Run the app:

   ```bash
   python3 main.py
   ```

## Configuration

The configuration is done through the .env file. Open the .env file and modify the following variables:

- `NAMES`: Names of the cameras. The names must be separated by commas.
- `RTSP_URLS`: RTSP URLs of the cameras. The URLs must be separated by commas.

## Troubleshooting

If you are having trouble running the app, try the following:

- Check if the RTSP URLs are correct.
- Check if the RTSP URLs are accessible in your network.
- Verify that the .env file is correctly configured.
