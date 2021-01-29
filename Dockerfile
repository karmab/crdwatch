FROM alpine:3.10

MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

LABEL name="karmab/crdwatch" \
      maintainer="karimboumedhel@gmail.com" \
      vendor="Karmalabs" \
      version="latest" \
      release="0" \
      summary="Watch CRD events" \
      description="Watch CRD events"

RUN apk add python3 gcc musl-dev python3-dev
RUN pip3 install kubernetes
ADD crdwatch.py /

CMD [ "python3", "-u", "/crdwatch.py" ]
