import streamlit as sl
import time as t
from datetime import time

sl.set_page_config(
    page_title="Timer App",
    page_icon="⌚"
)

def time_converter(value):
    m, s, ms = value.split(":")
    time_sec = int(m) * 60 + int(s) + int(ms) / 1000
    return time_sec


time_value = sl.time_input("Set timer", value=time(0, 0, 0))

if str(time_value) == "00:00:00":
    sl.write("Please set timer")
else:
    sec = time_converter(str(time_value))
    progress_bar = sl.progress(0)
    progress_status = sl.empty()
    for i in range(100):
        perentage_value = sec / 100
        progress_bar.progress(i + 1)
        progress_status.write(str(i + 1) + "%")
        t.sleep(perentage_value)
