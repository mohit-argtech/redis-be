FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install redis

# Make port 80 available to the world outside this container
EXPOSE 6379 26379

# # Define environment variable
# ENV NAME redis

# Run app.py when the container launches
CMD ["python", "./app.py"]
