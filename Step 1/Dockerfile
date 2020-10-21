FROM python:3.6-slim

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app

EXPOSE 5432:5432
RUN python data_gen.py \
    python table_packaging
CMD [ "python", "src/s3_upload.py" ]