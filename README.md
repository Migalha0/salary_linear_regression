# Linear Regression Study & Dockerization

This project serves as a study on Machine Learning algorithms and containerization with Docker.

This project's goal is to predict salary based on years of experience using Simple Linear Regression, using both high-level machine learning libraries against math and no libraries.

(It is also a test to see if the github action for my automatic curriculum update is working)

## How to Run with Docker

### METHOD 1. Docker compose (RECOMMENDED)
```
docker compose up
```

### METHOD 2.1. Build the Docker Image

```
docker build -t salary-app .
```

### 2.2. Run the container
Unix terminal
```
docker run --rm -v $(pwd):/app -w /app salary-app
```

Windows PowerShell
```
docker run --rm -v "${PWD}:/app" -w /app salary-app
```

## Project Structure

```text
SALARY_REGRESSION/
├── .dockerignore
├── .gitignore
├── by_hand.py
├── docker-compose.yml
├── Dockerfile
├── main.py
└── README.md
├── requirements.txt
├── Salary.csv
```