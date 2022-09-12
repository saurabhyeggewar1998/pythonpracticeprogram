import pytest
import requests
import random

token = "Bearer BQBOuXsIzaDj4L0rMg2FQoxbZT6WhWYex28o-REs5PB5SOhI-t25q7--fIp0tqWylLZT9zH11p2VnH6ZLP0VvouL3DtT08OjbEy0WP8sbPOsKqS5gtQbH-b4iraPbwUtAXgugiC20GYGasgKFHHivPuI4adibJeo1n8RNd_j616jAhm0lIQ2q1TW1rFxie3QKY1f2g56VX88NdTnA27tNFI4hpwHoOyxHg-moPnG9F_rXWtnWoO6JzogTlU"
user_id = '317v5jucqs74swivw6377z2k6f5q'
playlist_id ='1WbuJfTEjjSV2MdbP9Va4c'

track_id = '6XYQvYJzHjK5150Vl7NKfJ'

def test_Get_Current_Profile():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/me", headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>test_Get_Current_Profile>>>>>>>>>>>>>>>>>>>>>>>>")
def test_Get_UserProfile():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/users/" + user_id, headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Get_UserProfile>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_get_playlist():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/me/playlists", headers=header)
    print(resp)
    print(resp.text)
    a = resp.status_code
    assert a == 200, "Status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_create_playlist():
    num = random.random()
    header = {
        'Authorization': token
    }

    body = '{"name":"Bridgelabz CFP1","description":"New playlist description","public":false}'

    resp = requests.post("https://api.spotify.com/v1/users/" + user_id + "/playlists", headers=header,
                         data=body)
def test_Add_itemTo_playlist():
    header = {
        'Authorization': token
    }
    parameters = {
        "uris": "spotify:track:16LrVogeqYzGOfPXCzTVyU"
    }

    resp = requests.post("https://api.spotify.com/v1/playlists/0KtQ1oo4a89xIfZMFkIPs5/tracks", headers=header,
                         params=parameters)
    print(resp)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_Change_playlist_details():
    header = {
        'Authorization': token
    }
    body = '{"name":"Updated Playlist Name","description":"Updated playlist description","public":True}'
    resp = requests.put("https://api.spotify.com/v1/playlists/" + playlist_id, headers=header, data=body)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Change_playlist_details>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_GetUsersPlaylists():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/users/" + user_id + "/playlists", headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_GetUsersPlaylists>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_GetPlaylists():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/playlists/" + playlist_id, headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_search_for_items():
    header = {
        'Authorization': token
    }
    parameter = {
        "q": "deva shree ganesha",
        "type": "track"
    }
    resp = requests.get("https://api.spotify.com/v1/search", headers=header, params=parameter)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_search_for_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def test_getTrack():
    header = {
        'Authorization': token
    }

    resp = requests.get("https://api.spotify.com/v1/tracks/" + track_id, headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def test_getseveralTrack():
    header = {
        'Authorization': token
    }

    resp = requests.get("https://api.spotify.com/v1/tracks/" + track_id, headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# def test_update_playlist_items():
#     header = {
#         'Authorization': token
#     }
#     body = '{"range_start":3,"insert_before":2,"range_length":1}'
#     resp = requests.put("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", headers=header, data=body)
#     print(resp.text)
#     print(
#         ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_update_playlist_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# def test_delete_playlist_items():
#     header = {
#         'Authorization': token
#     }
#     body = {"uri": "spotify:user:317v5jucqs74swivw6377z2k6f5q"}
#     resp = requests.delete("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", headers=header, data=body)
#     print(resp.text)
#     print(
#         ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_delete_playlist_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")