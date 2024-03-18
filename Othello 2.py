"""Assignment: Othello 2
Created on 4 june 2021
Author: Jelmer Haverkate"""

# This program reads the time spend thinking by the two players from input in milliseconds
# and prints the time spend thinking by the human player in format hh:mm:ss.

MILLISECONDS_PER_SECOND = 1000

MILLISECONDS_PER_MINUTE = 1000 * 60

MILLISECONDS_PER_HOUR = 1000 * 60 * 60

black_player_thinking_time = int(input("Enter the time the black player thought: "))

white_player_thinking_time = int(input("Enter the time the white player thought: "))

if black_player_thinking_time > white_player_thinking_time:
    human_thinking_time_in_ms = black_player_thinking_time
else:
    human_thinking_time_in_ms = white_player_thinking_time

hourly_thinking_time = int(human_thinking_time_in_ms/MILLISECONDS_PER_HOUR)

minutes_thinking_time = int((human_thinking_time_in_ms % MILLISECONDS_PER_HOUR)/MILLISECONDS_PER_MINUTE)

seconds_thinking_time = int((human_thinking_time_in_ms % MILLISECONDS_PER_MINUTE)/MILLISECONDS_PER_SECOND)

print("The time the human player has spent thinking is: %02d:%02d:%02d." %
      (hourly_thinking_time, minutes_thinking_time, seconds_thinking_time))
