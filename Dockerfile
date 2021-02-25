ARG CONTAINER_PLAT=manylinux2010_i686
ARG CONTAINER_VERSION=latest

FROM quay.io/pypa/$CONTAINER_PLAT:$CONTAINER_VERSION

ENV PLAT=manylinux2010_i686

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
