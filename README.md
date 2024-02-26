# streaming-daemon-generator
This service uses the AudioCraft (by Meta) for AI music generation used by the streaming-daemon.

# Running Locally

1. Create Virtual Environment
```
python -m venv .venv
```

2. Activate Virtual Environment (Windows)
```
.\.venv\Scripts\Activate.ps1 
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Export Python Path (Windows)
```
$env:PYTHONPATH = $pwd
```

5. Run Service
```
python -m sdg
```
