# -*- coding: utf-8 -*-
import requests
import zipfile
import os

def download_data(url, folder_path=""):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    file_name = url.split("/")[-1]
    r = requests.get(url, stream=True)
    file_path = folder_path + file_name
    if os.path.exists(file_path):
        return file_path
    with open(file_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        return file_path
    return False


def unzip(file_path, target_path=None):
    zip_file = zipfile.ZipFile(file_path)
    if not target_path:
        target_path = os.path.dirname(file_path)
    zip_file.extractall(target_path)
    return target_path + "/" + zip_file.infolist()[0].filename.split("/")[0]


def unzip_download_data(url, folder_path=""):
    file_path = download_data(url, folder_path)
    return unzip(file_path)