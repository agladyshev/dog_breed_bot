FROM heroku/miniconda

# Grab requirements.txt.
ADD ./webapp/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt
RUN pip install python-telegram-bot
RUN pip install keras

# Add our code
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

RUN conda install anaconda-client
# RUN conda install --file conda-requirements.txt
RUN conda install pillow opencv libgcc tensorflow
RUN conda install h5py

# CMD gunicorn --bind 0.0.0.0:$PORT wsgi
CMD python main.py