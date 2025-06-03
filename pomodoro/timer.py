
---

### 🧠 `pomodoro/timer.py`

```python
import time
import argparse
import os
import sys

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def notify(title, message):
    try:
        if sys.platform == 'darwin':  # macOS
            os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")
        elif sys.platform == 'linux':
            os.system(f'notify-send "{title}" "{message}"')
        elif sys.platform == 'win32':
            from plyer import notification
            notification.notify(title=title, message=message)
    except:
        pass

def countdown(label, seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(f'{label}: {timer}', end='\r')
        time.sleep(1)
        seconds -= 1
    print(f'{label}: Done!           ')
    notify("Pomodoro Timer", f"{label} finished!")

def pomodoro_cycle(work_min, break_min, cycles):
    for i in range(1, cycles + 1):
        clear_terminal()
        print(f"🍅 Pomodoro Cycle {i}/{cycles}")
        countdown("Work", work_min * 60)
        if i < cycles:
            countdown("Break", break_min * 60)
        else:
            print("✅ All cycles complete!")
            notify("Pomodoro Timer", "All Pomodoro cycles completed!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Terminal Pomodoro Timer")
    parser.add_argument('--work', type=int, default=25, help='Work duration in minutes')
    parser.add_argument('--break', type=int, default=5, help='Break duration in minutes')
    parser.add_argument('--cycles', type=int, default=4, help='Number of Pomodoro cycles')

    args = parser.parse_args()

    pomodoro_cycle(args.work, args.break, args.cycles)
