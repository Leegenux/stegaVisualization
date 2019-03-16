# About the Project

It's a demonstration about how simplest steganography technique works and what you can do to detect this stuff.

Basically, the `payload.txt`'s content is loaded onto the carrier: `Lenna_orig.png`. The system gives a `payload-filled.png` as well as results retrieved from different bits of the RGB channels.

# Code Execution

Start a terminal at current project directory, first run `source env/bin/activate`. Then `python LSB_map.py` 

# Result

Compare one output with another, and take a closer look at "result_red_1.png". The unique texture shows something different.

