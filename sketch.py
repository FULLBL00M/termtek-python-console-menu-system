import time
import random

def print_text_humanistic(text: str) -> None:
    """Print text character by character with humanistic variations in speed."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(0.01, 0.025))

print_text_humanistic("Hello, world!")