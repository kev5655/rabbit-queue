# Use Ubuntu 24.10 as the base image
FROM ubuntu:24.10 AS builder-image

# Install necessary packages
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python3.12 \
        python3.12-dev \
        python3.12-venv \
        python3-pip \
        python3-wheel \
        build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python3.12 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runner stage
FROM ubuntu:24.10 AS runner-image

# Install Python 3.12 and venv
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        python3.12 \
        python3.12-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from the builder stage
COPY --from=builder-image /opt/venv /opt/venv 
COPY receive.py .

# Activate virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#EXPOSE 5672

# Set the default command
CMD ["python", "-u", "receive.py"]
