import tkinter
import requests


def RequestUserInfo(user):
    ratingHistory = requests.get("https://codeforces.com/api/user.rating?" + user)
    userSubmisisons = requests.get("https://codeforces.com/user.status?" + user)
    