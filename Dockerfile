FROM python
MAINTAINER Alex Recker <alex@reckerfamily.com>
RUN useradd -ms /bin/bash app
WORKDIR /home/app
ADD . .
RUN chown -R app:app .
RUN pip install -r requirements/prod.txt
USER app
