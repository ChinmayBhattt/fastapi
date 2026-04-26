1. python3 -m venv venv
2. source venv/bin/activate
3. pip install fastapi uvicorn
4. pip freeze > requirements.txt
5. uvicorn main:app --reload

- http://127.0.0.1:8001/docs
- http://127.0.0.1:8001/teas
- [{"id":1,"name":"ginger","origin":"home made"},{"id":1,"name":"ginger","origin":"home made"},{"id":1,"name":"ginger","origin":"home made"}]