from python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR folder_view/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]