FROM python:2.7
WORKDIR /apps
RUN apt-get update \
  && apt-get -y install libusb-1.0-0-dev \
  && pip install --upgrade pip \
  && pip install flask nfcpy mysql-connector-python
CMD python run.py
