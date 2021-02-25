ARG CONTAINER_PLAT=manylinux2014_s390x
ARG CONTAINER_VERSION=latest

FROM quay.io/pypa/$CONTAINER_PLAT:$CONTAINER_VERSION

ENV PLAT=manylinux2014_s390x

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
