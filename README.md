### Download from Google Drive with Synchronous Multithreading Approach

---

**Requirements:**
- Google Drive Account with one directory marked as shared.
- [API key to access Google Drive APIs.](https://developers.google.com/drive/api/v3/enable-drive-api)
- getfilelistpy third-party library to list files in Google Drive shared directory.
- gdown third-party library that allows to download files from Google Drive

Place your own API secrets in the form of one that in the ./secrets/google_secrets.json (closed one)

Json Credentials structure:

````
{ "api_key": "your_api_key",
  "id" : "shared_folder_id",
  "fields": "files(name, id, webContentLink)"}
````

---
Before run: 
```
$ python3 pip install -r requirements.txt
```
