# Flask API Model Learning

## How to run

```
python testing_deploy.py
```

### Git Bash

```
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d @data/data.json
```

### CMD / Powershell

```
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d @data/data.json
```
