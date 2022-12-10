FROM python:3.11-slim-buster

# create a non root user
WORKDIR /apiuser

# add requirements, upgrade pip and install python dependancy
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy required application files
COPY /src src

# create a nonroot user
RUN groupadd --gid 1234 apiuser && useradd -s /bin/bash --uid 1234 --gid 1234 -m apiuser/

# launch app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]