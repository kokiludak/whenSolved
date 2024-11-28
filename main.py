import tkinter
import requests


def RequestUserInfo(user):
    ratingHistory = requests.get("https://codeforces.com/api/user.rating?handle=" + user)
    userSubmissions = requests.get("https://codeforces.com/api/user.status?handle=" + user)
    return (ratingHistory, userSubmissions)


if __name__ == "__main__":
    print("Enter username: ")
    user = input()
    (ratingHistory, userSubmissions) = RequestUserInfo(user)
    print(ratingHistory.content)
