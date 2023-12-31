# using Python v3.11
FROM python:3

#Create app directory
WORKDIR /workoutbuilder

# copy local contents into container
ADD . /workoutbuilder

# Install app dependencies
RUN pip install -r requirements.txt

# For production:
# --o=production

# Exposse port 5000 outside container
EXPOSE 5000

COPY . .

# Command used to start application
CMD ["python", "main.py"]


