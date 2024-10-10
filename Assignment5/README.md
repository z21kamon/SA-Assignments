# Service-Based Architecture

## Architecture

App uses 3 services: UserService for managing users sign up process, PostService for posting and LikeService for liking posts. `main.py` is a runner file which manages user I/O via command line interface.

## Database
Database is implemented using SQLite and Python built-in `sqlite3` library. It has `users` table which contains users' username, and `posts` table, which contains post author, id, content, timestamp and likes count.
