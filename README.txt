Instructions on how to run both problems:

Problem 1:
   1) Activate virtual environment: source venv/bin/activate
   2) Enter problem 1 directory: cd problem1/problem1/
   3) Migrate to proper db schema: python manage.py migrate
   4) Launch webserver: python manage.py runserver
   5) Make curl requests to host 'localhost:8000'
      --Example: curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' localhost:8000/messages

Problem 2:
   1) Enter problem 2 directory: cd problem2/
   2) Run problem2.py with the following command: python problem2.py <filename> <balance>
      --Example: python problem2.py test/example.txt 2500

