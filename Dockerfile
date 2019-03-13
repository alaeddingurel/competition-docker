FROM python:3.6


RUN apt-get update
RUN apt-get -y install default-jre
RUN git clone https://github.com/OsmanMutlu/python-boilerpipe.git
WORKDIR "/python-boilerpipe"
RUN pip install -r requirements.txt
RUN python3 setup.py install
