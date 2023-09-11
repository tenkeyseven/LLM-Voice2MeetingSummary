import os
import sys

def generate_clip(input_file, start_time, end_time, output_file):
    command = f"ffmpeg -i {input_file} -vn -acodec copy -ss {start_time} -to {end_time} {output_file}"
    os.system(command)

input_file = "full_meeting.wav"

# start_time = "00:00:00"
# end_time = "00:05:00"
# output_file = 'voice_clips/'+"clip_new.wav"

clips_info = [
    {
        "start_time": "00:00:00",
        "end_time": "00:9:37",
        "output_file": "speaker_one.wav"
    },
    {
        "start_time": "00:9:37",
        "end_time": "00:16:46",
        "output_file": "speaker_two.wav"
    },
    # ......   
    {
        "start_time": "00:16:46",
        "end_time": "00:22:11",
        "output_file": "speaker_nth.wav"
    }
]


for clip_info in clips_info:
    saved_path = 'voice_clips/'+ clip_info["output_file"]
    generate_clip(input_file, clip_info["start_time"], clip_info["end_time"],saved_path)

