# YTCLI - YouTube Command Line Interface

A simple and efficient CLI tool to search, play, and manage YouTube playlists and videos directly from the terminal. YTCLI utilizes `mpv` and `yt-dlp` to provide seamless YouTube integration without requiring API keys.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Advantages](#advantages)
- [Tools, Technologies, and Platforms](#tools-technologies-and-platforms)
- [Future Improvements](#future-improvements)
- [Challenges](#challenges)
- [Contributing](#contributing)
- [License](#license)

## Features
- Add and delete YouTube playlists
- Automatically update playlists when changed on YouTube
- Search and play YouTube videos
- Support for audio-only mode and regular mode for both playlists and searches
- Works on Windows and Linux
- Minimal system requirements

## Demo
Check out the demo [here](https://streamable.com/t52l7k).

## Dependencies
All dependencies will be automatically installed during setup. Note: On Windows, `mpv` will be a standalone executable in the working directory.

## Installation

### Prerequisites
- Python 3.x
- MySQL Server

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ytcli.git
    cd ytcli
    ```

2. Set up the MySQL database:
    ```sql
    CREATE DATABASE ytcli_db;
    CREATE USER 'ytcli_user'@'localhost' IDENTIFIED BY 'yourpassword';
    GRANT ALL PRIVILEGES ON ytcli_db.* TO 'ytcli_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

3. Modify the MySQL configuration in `ytcli.py`:
    ```python
    # Update the following lines with your MySQL credentials
    db_config = {
        'user': 'ytcli_user',
        'password': 'yourpassword',
        'host': '127.0.0.1',
        'database': 'ytcli_db'
    }
    ```

4. Run the setup script:
    ```sh
    python setup.py
    ```

## Usage
1. Start the application:
    ```sh
    python ytcli.py
    ```

2. Follow the menu prompts to:
   - Start a playlist
   - Add a new playlist
   - Delete an existing playlist
   - Search and play YouTube videos

## Modules

### Playlist Management
- **Add Playlist:** Add a new YouTube playlist to the database.
- **Delete Playlist:** Remove an existing playlist from the database.
- **Update Playlist:** Automatically update playlists when changes are detected on YouTube.
- **Fetch Playlist:** Retrieve playlists from the MySQL database.

### Video Search and Playback
- **Search for Videos:** Search YouTube videos using keywords.
- **Play Video:** Play selected videos in audio-only mode or regular mode using `mpv`.

### Database Management
- **Store Playlists:** Store playlist information in MySQL.
- **Retrieve Playlists:** Retrieve stored playlists for playback.

## Advantages
- **No API Key Required:** Accessible to anyone without the need for registration.
- **Lightweight:** Minimal system requirements make it easy to use on various devices, including IoT and mobile devices.
- **Efficient:** Consumes less internet bandwidth compared to traditional YouTube applications.
- **Productivity Boost:** Allows developers to enjoy YouTube content while working in the terminal.

## Tools, Technologies, and Platforms

### Tools and Technologies
- **Programming Language:** Python
- **Media Player:** `mpv`
- **YouTube Downloader:** `yt-dlp`
- **Database:** MySQL
- **Python Libraries:** `mysql-connector-python`, `youtube-search-python`, `pytube`

### Platforms
- Windows
- Linux

## Future Improvements
- Enhanced search capabilities with more filters and options.
- User authentication to manage personal playlists.
- Simple GUI for users who prefer graphical interfaces.
- Optimizing the tool for macOS and Raspberry Pi.

## Challenges
- Ensuring cross-platform compatibility.
- Automating dependency installation for different operating systems.
- Efficient database integration with MySQL for playlist management.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
