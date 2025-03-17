# MindSpark - A Quiz App  

MindSpark is a quiz application where users can take quizzes based on their preferences and track their performance on a dedicated dashboard.  
Admins have full control to create, edit, and delete quizzes, as well as manage user accounts when necessary.


![MindSpark Screenshot](Mad2_Project\src\assets\img\ReadmeImg.png)


## Recommended Setup

[VSCode](https://code.visualstudio.com/) + Linux (required for running Celery).

## Customize Configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup (Frontend - Vue.js)

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

The Vue server will be running on:

**http://localhost:5174**


### Compile and Minify for Production


```sh
npm run build
```

---

## Backend Setup (Flask API)

Navigate to the **Flask backend directory**:

```sh
cd .\Mad2_Flask\
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Run the Flask server:

```sh
python app.py
```

The Flask server will be running on:

**http://localhost:5000**

---

Now your **Vue frontend** and **Flask backend** are set up correctly! 🚀

