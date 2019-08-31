FROM python:3
MAINTAINER Alex Recker <alex@reckerfamily.com>

# Create an app user
RUN useradd -ms /bin/bash app
WORKDIR /home/app

# Install requirements
ADD requirements/*.txt requirements/
RUN pip install -r requirements/prod.txt

# Set up environment
USER app
ENV PS1 "\u@\h:\w\$ "
RUN rm -rf .bashrc .profile .bash_logout

# Move code over
ADD . .

# Default
CMD ["bash"]
