# Use UBI9 minimal as the base image
FROM registry.access.redhat.com/ubi9/ubi-minimal:latest

# Install Python 3 and pip
RUN microdnf install -y python3 python3-pip && \
    microdnf clean all

# Copy your Python script into the container
COPY app/ /app
# Set the default command to run the script with Python
CMD ["python3", "/main.py"]
