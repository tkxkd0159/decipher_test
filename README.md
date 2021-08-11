# decipher_test
Simple Test for Applicants

```
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt

```

```
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"LJS\", \"age\":20}" http://127.0.0.1:5000/api/seed
curl -X POST -d "Test text" http://127.0.0.1:5000/api/seed
curl -X POST -H "Content-Type: application/json" -d "{\"jsonrpc\":\"2.0\", \"method\":\"genUniqueID\", \"params\":{\"name\":\"LJS\", \"age\":20, \"seed\":\"f49520153764a0c9bcbf4648141bf537cda5cd8b30bd15a6032d2918e1916b63d7f5729f2aa124b68d0a28cc058a6a9511aead756611122338e1a62aa962d60c\"}, \"id\":202108}" http://127.0.0.1:5000/api
```