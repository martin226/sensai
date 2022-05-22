<div align="center">
    <img alt="Logo" src="docs/logo.png" width="100" />
</div>
<h1 align="center">
    Sensai
</h1>
<p align="center">
    The workout platform revolutionizing the way you workout with a built-in AI coach that changes how you exercise.
</p>

> _tldr;_ Sensai transforms how you workout by providing you with real-time suggestions and analytics, powered by advanced computer vision algorithms.

## How it Works

> Website -> Backend API -> AI Model -> Website

### Backend API and AI

- Flask webserver that handles authentication, image processing, and workouts
- JWT (Json Web Tokens) for authentication
- MongoDB as our database
- Mediapipe for finding (x, y) coordinates of body landmarks
- SocketIO for real-time data exchange with the client

### Website

- Built with NuxtJS and WindiCSS, and designed on Figma
- SocketIO for real-time data exchange with the server

## Project Setup

### Backend API and AI

```bash
cd backend
poetry install
FLASK_APP=backend FLASK_ENV=development poetry run flask run
```

### Website

```bash
cd website
yarn install
yarn dev
```
