# # Use Python 3.6 or later as a base image
# FROM python:3.7
# WORKDIR /app
# # Copy contents into image
# COPY app.py .
# COPY requirements.txt .
# # Install pip dependencies from requirements
# RUN pip3 install -r requirements.txt

# # Set YOUR_NAME environment variable
# ENV YOUR_NAME=friend
# # Expose the correct port
# EXPOSE 5500
# # Create an entrypoint
# ENTRYPOINT ["python", "app.py"]


# Python base image.
FROM python:3.7
# Create and set the work directory inside the image named 'app'
WORKDIR /app
# Execute a pip install command using the list 'requirements.txt'
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app file into the image working directory

ENV YOUR_NAME=friend

COPY app.py .
# State the listening port for the container. 
# The app's code does not actually specify the port, so it would be useful to include here.
EXPOSE 5500
# Run 'python app.py' on container start-up. This is the main process.
ENTRYPOINT ["python", "app.py"] 


