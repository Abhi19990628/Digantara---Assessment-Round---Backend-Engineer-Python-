# Scheduler Microservice

This project is a **Scheduler Microservice** built using **FastAPI** and **SQLAlchemy**. The microservice allows job scheduling while maintaining critical job-related information. It offers API endpoints for job management, such as listing all jobs, retrieving details of a specific job by ID, and creating new jobs.

## Features

1. **Job Scheduling**: 
   - The service allows scheduling of jobs with customized configurations (e.g., running every Monday, daily at a specific time).
   - POC logic is included to demonstrate how the jobs will be scheduled and executed.

2. **API Endpoints**:
   - `GET /jobs`: Lists all available jobs, providing an overview of scheduled tasks.
   - `GET /jobs/{id}`: Retrieves detailed information about a specific job, including scheduling details.
   - `POST /jobs`: Allows users to create new jobs with customizable attributes and intervals.

3. **Database Integration**: 
   - Job details, including job name, last run timestamp, and next run timestamp, are stored in the database.

4. **Customization**: 
   - Jobs can be customized by the user to define specific attributes, scheduling intervals, and other parameters.

5. **Scalability**: 
   - The service is designed to handle large-scale operations (10,000+ users, 1,000 services, and 6,000 API requests per minute).

## Tech Stack

- **Python 3.10+**
- **FastAPI**: For building RESTful APIs.
- **SQLAlchemy**: For database ORM.
- **SQLite/PostgreSQL**: Database for storing job details.
- **Uvicorn**: ASGI server for serving FastAPI.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
Set up a virtual environment:

bash
Copy code
python -m venv my_env
source my_env/bin/activate  # On Windows: my_env\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
uvicorn app.main:app --reload
Access the API:

Go to http://127.0.0.1:8000/docs to view the automatically generated API documentation (using Swagger UI).
You can also access the API at http://127.0.0.1:8000/jobs.


API Endpoints
List All Jobs

GET /jobs
Lists all available jobs with their scheduling information.
Get Job by ID

GET /jobs/{id}
Fetches detailed information for a job by its ID.
Create New Job

POST /jobs
Creates a new job with a customizable schedule and attributes.

Scaling Considerations
To achieve scalability in terms of handling a large number of users and API requests, consider the following strategies:

Horizontal Scaling: Deploy multiple instances of the microservice behind a load balancer to distribute API traffic evenly.

Database Optimization: Use a robust, scalable database like PostgreSQL with optimized indexing and connection pooling to handle large datasets.

Job Distribution: Use a distributed task queue (e.g., Celery with RabbitMQ) to distribute job executions across multiple worker nodes.

Caching: Implement caching strategies using Redis or Memcached to reduce database load for frequently requested data.

API Rate Limiting: Implement rate limiting to prevent overloading the system with excessive API requests.

Running Tests
Install testing dependencies:

bash
Copy code
pip install pytest
Run the tests:

bash
Copy code
pytest
Documentation
API documentation is automatically generated with Swagger UI and can be accessed at /docs.

License
This project is licensed under the MIT License.

Contact
For any inquiries, reach out to [abhiv5976@gmail.com].

markdown
Copy code

### Steps to Follow:
1. **Include the above content** in your `README.md` file.
2. Make sure to explain your project setup in detail and describe how job scheduling and API endpoints work.
3. Include a section for scalability as requested in the assignment, which is essential for handling high loads.
4. **Add instructions** for setting up the environment, running the application, and testing it.
5. Use **API documentation** with tools like Swagger (already integrated with FastAPI).

This should cover everything required for your assignment! Let me know if you need further clarification or changes.
