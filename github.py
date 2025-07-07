import requests
from typing import Any


def get_latest_github_release(url: str) -> Any:
    response = requests.get(f"https://api.github.com/repos/{url}/releases")
    result = response.json()

    return result[0]

def get_github_tarball_url(release_result: Any) -> str:
    return release_result["tarball_url"]

def download_file(url: str, dest: str) -> None:
    response = requests.get(url, stream=True)
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)

def download_latest_tarball(url: str, dest: str) -> None:
    release = get_latest_github_release(url)
    zstd_url = get_github_tarball_url(release)
    download_file(zstd_url, dest)