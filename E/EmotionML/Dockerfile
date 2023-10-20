FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip wheel opencv-python
RUN pip install opencv-python
RUN pip install libgl1
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./app.py