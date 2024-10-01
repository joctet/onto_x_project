FROM python:3.9-slim
# create the folder app inside the container
WORKDIR /app
# we copy the required dependancies
COPY requirements.txt .
# and we install them
RUN pip install --no-cache-dir -r requirements.txt
# then we copy the code & data
COPY src /app/src
COPY data /app/data
# we define the port FastAPI will run on
EXPOSE 8000
# Then we run the FastAPI server using Uvicorn
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]