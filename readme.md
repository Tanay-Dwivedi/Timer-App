# Timer app

This code uses the `Streamlit` library to create a simple timer application. Users can set a timer using a time input widget, and the code simulates the timer's progress by updating a progress bar and status in 1% increments.

[Link](https://timely.streamlit.app/)

-----

## Installation

```
pip install streamlit
```
Firstly you have to install the `streamlit` module to your python script for running the program.

-----

## Code Break:

```python
# Import the Streamlit library and alias it as sl
import streamlit as sl
```
This line imports the Streamlit library and assigns the alias "sl" for ease of use.

```python
# Import the time library and alias it as t
import time as t
```
This line imports the time library and assigns the alias "t" for ease of use.

```python
# Import the time class from the datetime module
from datetime import time
```
This line specifically imports the `time` class from the `datetime` module.

```python
# Define a function named time_converter that converts a time value in the format "mm:ss:ms" to seconds
def time_converter(value):
    # Split the input value into minutes, seconds, and milliseconds
    m, s, ms = value.split(":")
    # Convert minutes and seconds to seconds, add milliseconds, and return the total time in seconds
    time_sec = int(m) * 60 + int(s) + int(ms) / 1000
    return time_sec
```
This block defines a function named `time_converter` that takes a time value in the format "mm:ss:ms" and converts it into seconds.

```python
# Create a time input widget in Streamlit, labeled "Set timer," with an initial value of midnight (00:00:00)
time_value = sl.time_input("Set timer", value=time(0, 0, 0))
```
This line creates a Streamlit time input widget labeled "Set timer" with an initial value set to midnight (00:00:00).

```python
# Check if the selected time is midnight (00:00:00)
if str(time_value) == "00:00:00":
    # If it is, display a message asking the user to set the timer
    sl.write("Please set timer")
```
This block checks if the selected time is midnight and, if true, displays a message asking the user to set the timer.

```python
else:
    # If a non-midnight time is selected, convert it to seconds using the time_converter function
    sec = time_converter(str(time_value))
    # Create a progress bar widget in Streamlit with an initial value of 0
    progress_bar = sl.progress(0)
    # Create an empty widget in Streamlit to display the progress status
    progress_status = sl.empty()
    # Loop through 100 iterations to simulate the progress of a timer
    for i in range(100):
        # Calculate the percentage value for the progress bar based on the total time
        percentage_value = sec / 100
        # Update the progress bar by increasing its value by 1%
        progress_bar.progress(i + 1)
        # Display the current progress status as a percentage
        progress_status.write(str(i + 1) + "%")
        # Pause the execution for a fraction of the total time to simulate a timer
        t.sleep(percentage_value)
```
This block executes when a user selects a time other than `00:00`. It converts the selected time to seconds, then creates a Streamlit progress bar and an empty widget for progress status. It then simulates the progress of a timer by updating the progress bar and status in a loop, pausing execution to mimic the passing of time.

-----