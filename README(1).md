# GE Video 🎬

A simple movie management system developed in Python as an academic project.

## 📌 About the Project

**GE Video** is a Python-based movie management platform designed to simulate the basic functionality of a streaming/movie management service.

The system allows users to create accounts, log in, interact with movies, create playlists and manage their favorite videos. It also includes an administrative system for managing the platform and viewing statistics.

The project was developed as part of the **Fundamentos de Algoritmos** course.

## 🚀 Features

### 👤 User Features

- User registration
- User login
- Movie browsing
- Like movies
- Add movies to favorites
- Create and manage playlists
- Add movies to playlists

### 🔐 Administrator Features

- Administrator login
- Add new videos
- Delete videos
- Manage available videos
- Consult registered users
- View platform statistics
- Display the Top 5 most-liked videos
- View the total number of users
- View the total number of videos

## 🛠️ Technologies

- **Python**
- **JSON**
- File-based data persistence

## 📂 Project Structure

```text
GE-Video/
│
├── main.py
├── usuarios.py
├── videos.py
├── sistema.py
├── dados.json
└── README.md
```

### Files

| File | Description |
|------|-------------|
| `main.py` | Main program and user interface |
| `usuarios.py` | User-related functionality |
| `videos.py` | Video management and video-related functions |
| `sistema.py` | System and administrative functionality |
| `dados.json` | Local data storage |
| `README.md` | Project documentation |

## 💾 Data Storage

The system uses a local `dados.json` file to store information about users and videos.

This approach allows the application to persist data between executions without requiring an external database.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/arrudaa77/ge.video.git
```

### 2. Navigate to the project directory

```bash
cd GE-Video
```

### 3. Run the application

```bash
python main.py
```

## 🎯 Project Goals

The main goals of this project were to practice:

- Python programming
- Algorithmic thinking
- Functions and modular programming
- Data structures
- File manipulation
- JSON data persistence
- User interaction
- Basic software organization

## 📚 Academic Project

This project was developed for educational purposes as part of the **Fundamentos de Algoritmos** course.

It focuses on applying programming fundamentals to the development of a functional application.

## 👨‍💻 Author

**Enzo Arruda**

Computer Science student at **Centro Universitário FEI**.
