FROM python:3-alpine
LABEL maintainer="Oleg Sivolov <sesivolov@gmail.com>"

ARG BUILD_DATE
ARG VCS_REF

# Set labels (see https://microbadger.com/labels)
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/OlegSivolov/diploma.git"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# Expose the Flask port
EXPOSE 5000

CMD [ "python", "./app.py" ]
