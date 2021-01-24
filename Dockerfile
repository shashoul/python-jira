FROM python:3.7.1-slim-stretch

WORKDIR  /app

COPY requirements.txt .

RUN pip install --upgrade pip \ 
    && pip install -r requirements.txt

COPY jira_issue.py .

ENTRYPOINT ["python3","jira_issue.py"]