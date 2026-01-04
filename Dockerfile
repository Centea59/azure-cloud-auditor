FROM python:3.9-slim
WORKDIR /app
RUN pip install azure-identity azure-mgmt-storage
COPY inventory.py .
CMD ["python", "inventory.py"]