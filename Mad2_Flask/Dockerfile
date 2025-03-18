FROM python:3.13.1-slim

# Set the working directory
WORKDIR /Mad2_Flask

# Copy the current directory contents into the container at /Mad2_Flask
COPY . /Mad2_Flask



# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run app.py when the container launches
ENTRYPOINT ["flask", "run"]

