# Emotion Detection Project

This project aims to detect emotions in videos using DeepFace for facial recognition and emotion classification. Video processing is handled asynchronously using Celery and Redis.

## Features

- Upload videos for emotion analysis
- Asynchronous video processing
- Display progress bar during upload and processing
- Display analysis results in a pie chart

## Technologies Used

- Django
- Celery
- Redis
- DeepFace
- Bootstrap
- Chart.js

## Installation

1. Clone the repository:

```bash
https://github.com/kauecurti/emotion_detection.git
emotion_detection
```

2. Create a virtual environment and activate it::

```bash
https://github.com/kauecurti/emotion_detection.git
emotion_detection
```
3. Install dependencies:
```bash
pip install -r requirements.txt

```

4. Setup Redis:
```bash
# On macOS:
brew install redis
brew services start redis

# On Ubuntu:
sudo apt-get install redis-server
sudo service redis-server start
```

5. Start the Django server:
```bash
# On macOS:
celery -A emotion_detection worker --loglevel=info

```

## Usage

- 1 Go to http://127.0.0.1:8000/ to upload a video.
- 2  The progress bar will display during upload and processing.
- 3  After completion, you will be redirected to the results page with a pie chart of detected emotions.

#Screenshots

#Upload Screen

## <img src="https://github.com/kauecurti/emotion_detection/assets/36936274/4eedd715-b976-4d25-b4c9-9bca306f54d8">

# Analysis Results

## <img src="https://github.com/kauecurti/emotion_detection/assets/36936274/8adf1cb7-3798-4b92-9959-13edf570a935">
## Project Structure
```bash
emotion_detection/
├── video_analysis/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── celery.py
│   ├── migrations/
│   ├── models.py
│   ├── tasks.py
│   ├── templates/
│   │   ├── upload.html
│   │   └── results.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── emotion_detection/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Contribution
Feel free to open issues and pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License.


