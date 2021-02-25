ARG CONTAINER_PLAT=manylinux2010_x86_64
ARG CONTAINER_VERSION=2021-02-06-3d322a5

FROM quay.io/pypa/$CONTAINER_PLAT:$CONTAINER_VERSION

ENV PLAT=manylinux2010_x86_64

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
