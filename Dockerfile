FROM python:3
MAINTAINER Alex Recker <alex@reckerfamily.com>

# Create an app user
RUN useradd -ms /bin/bash app
WORKDIR /home/app

# Install requirements
ADD requirements/*.txt requirements/
RUN pip install -r requirements/prod.txt

# Move code over
ADD . .
RUN chown -R app:app .

# Drop permissions
USER app

# Default
CMD ["/usr/local/bin/env", "bash"]
