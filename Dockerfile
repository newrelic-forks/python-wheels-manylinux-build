ARG CONTAINER_PLAT=manylinux1_x86_64
ARG CONTAINER_VERSION=latest

FROM quay.io/pypa/$CONTAINER_PLAT:$CONTAINER_VERSION

ENV PLAT=manylinux1_x86_64

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
