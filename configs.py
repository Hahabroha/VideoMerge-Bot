# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID", "25435105"),
    API_HASH = os.environ.get("API_HASH", "011126265844f2d7cc7dc1a024f6bc78"),
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6719790386:AAFG0oodPLwcBQYh1FOsBbw89WFYem5E_U4"),
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001963382900"),
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002061802105"),
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", 50f4c1400aa4d1a21075),
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "LYwP8KKdpRcRK63"),
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://TEACHER:TEACHER@cluster0.rw02bgj.mongodb.net/?retryWrites=true&w=majority)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 6459102722))

    START_TEXT = """
Hi Unkil, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @AbirHasan2005
"""
    CAPTION = "Video Merged by @{}\n\nMade by @AbirHasan2005"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
