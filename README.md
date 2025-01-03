# Auto Screen Capture

This program automatically takes screenshots when specific events occur on your Mac:
- Mouse clicks
- Enter key presses

## Setup

1. Make sure you have Python 3.x installed on your system
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the program:
```bash
python screen_capture.py
```

2. The program will start monitoring for events and save screenshots to the `screenshots` directory
3. Each screenshot will be saved with a timestamp in the filename
4. To stop the program, press Ctrl+C

## Note
- You may need to grant screen recording permissions to your terminal/IDE when running the program for the first time
- Screenshots are saved in PNG format
- The program adds a small delay (0.1s) before taking each screenshot to ensure the captured change is included 