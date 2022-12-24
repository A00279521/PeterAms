# Use Python 3.6 or later as a base image
FROM python:3.7
WORKDIR /app
# Copy contents into image
COPY app.py .
COPY requirements.txt .
# Install pip dependencies from requirements
RUN pip3 install -r requirements.txt

# Set YOUR_NAME environment variable
ENV YOUR_NAME=friend
# Expose the correct port
EXPOSE 5500
# Create an entrypoint
ENTRYPOINT ["python", "app.py"]

