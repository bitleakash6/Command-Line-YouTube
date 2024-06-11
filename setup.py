import os
import platform

def install_linux():
    distro_name = os.popen("sed -n -e '/^ID=/p' /etc/os-release").read()[3:-1].strip()
    debian_based = ['debian', 'ubuntu', 'linuxmint', 'popos', 'zorin', 'elementary']
    arch_based = ["manjaro", 'arch', 'endeavouros']
    
    if distro_name in debian_based:
        os.system("sudo apt install -y mpv python3-pip")
    elif 'fedora' in distro_name:
        os.system("sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
        os.system("sudo dnf install -y mpv mpv-libs python3-pip")
    elif distro_name in arch_based:
        os.system("sudo pacman -S --noconfirm python-pip mpv")
    else:
        print("Please install the following dependencies manually:")
        print("1. python3-pip")
        print("2. mpv")
    
    os.system("pip3 install youtube-search-python pytube yt-dlp mysql-connector-python")

def install_windows():
    os.system("pip install requests youtube-search-python pytube yt-dlp mysql-connector-python py7zr")
    
    print("Downloading mpv....")
    url = "https://sourceforge.net/projects/mpv-player-windows/files/64bit-v3/mpv-x86_64-v3-20221002-git-2207236.7z/download"
    response = requests.get(url)
    with open("mpv.7z", "wb") as file:
        file.write(response.content)
    
    print("Extracting downloaded files....")
    os.system("py7zr x mpv.7z")
    os.system("del mpv.7z")

def install():
    osname = platform.system()
    if osname == "Linux":
        install_linux()
    elif osname == "Windows":
        install_windows()
    else:
        print(f"OS {osname} not supported.")

if __name__ == "__main__":
    install()
