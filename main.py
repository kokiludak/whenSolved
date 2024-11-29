import tkinter
import requests
import json

def RequestUserInfo(user):
    ratingHistory = requests.get("https://codeforces.com/api/user.rating?handle=" + user)
    userSubmissions = requests.get("https://codeforces.com/api/user.status?handle=" + user)
    return (ratingHistory, userSubmissions)


if __name__ == "__main__":
    print("Enter username: ")
    user = input()
    (ratingBytes, userSubmissionsBytes) = RequestUserInfo(user)
    ratingHistoryString = ratingBytes.content.decode('utf8').replace("'", '"')
    userSubmissionsString = userSubmissionsBytes.content.decode('utf8').replace("'", '"')
    output = open("test.txt", "a")
    output.write(ratingHistoryString)