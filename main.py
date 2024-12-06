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

    ratingHistoryJson = json.loads(ratingHistoryString)
    userSubmissionsJson = json.loads(userSubmissionsString)

    ratingHistory = ratingHistoryJson.get("result", [])
    userSubmissions = userSubmissionsJson.get("result", [])

    scanline = [(entry['ratingUpdateTimeSeconds'], entry['newRating']) for entry in ratingHistory  if 'ratingUpdateTimeSeconds' in entry and 'newRating' in entry]
    submissions = [
    (entry['creationTimeSeconds'], str(entry['problem']['contestId']) + entry['problem']['index'])
    for entry in userSubmissions
    if (
        'creationTimeSeconds' in entry and
        'problem' in entry and 
        'contestId' in entry['problem'] and 
        'index' in entry['problem'] and 
        entry.get('verdict') == 'OK'  # Filter by verdict
    )
    ]
    scanline.extend(submissions)
    scanline.sort()
    print(scanline)