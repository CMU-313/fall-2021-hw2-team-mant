# vim:set ft=dockerfile:

####
# base_image - Bare bones image with the base packages needed to run
#              Mayan EDMS.
####

FROM debian:10.8-slim as base_image

LABEL maintainer="Roberto Rosario roberto.rosario@mayan-edms.com"

COPY config.env /config.env

ENV LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PROJECT_INSTALL_DIR=/opt/mayan-edms/

# Debian package caching.
ARG APT_PROXY
RUN set -x \
&& if [ "${APT_PROXY}" ]; \
    then echo "Acquire::http { Proxy \"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/01proxy \
; fi \
# Install base OS packages to run Mayan EDMS.
&& echo "deb http://deb.debian.org/debian buster-backports main contrib non-free" >> /etc/apt/sources.list \
&& echo "deb-src http://deb.debian.org/debian buster-backports main contrib non-free" >> /etc/apt/sources.list \
&& DEBIAN_FRONTEND=noninteractive \
apt-get update \
&& apt-get install -y --no-install-recommends -t buster-backports \
    libreoffice-calc-nogui \
    libreoffice-draw-nogui \
    libreoffice-impress-nogui \
    libreoffice-math-nogui \
    libreoffice-writer-nogui \
&& apt-get install -y --no-install-recommends \
    ca-certificates \
    exiftool \
    expect \
    fonts-arphic-uming \
    fonts-arphic-ukai \
    fonts-unfonts-core \
    fuse \
    ghostscript \
    git-core \
    gpgv \
    gnupg1 \
    graphviz \
    libarchive-zip-perl \
    libfuse2 \
    libmagic1 \
    libmariadb3 \
    libpq5 \
    procps \
    poppler-utils \
    python3-distutils \
    sane-utils \
    sudo \
    supervisor \
    tesseract-ocr \
# Remove make and build dependencies.
&& apt-get remove -y \
    make \
    libproxy-tools \
    libreoffice-avmedia-backend-vlc \
    libvlc-bin \
    libvlc5 \
    libvlccore9 \
    adwaita-icon-theme \
    gsettings-desktop-schemas \
    libgstreamer-plugins-base1.0-0 \
&& apt-get autoremove -y --purge \
# Add mayan user.
&& adduser mayan --disabled-password --disabled-login --no-create-home --gecos "" \
# Pillow can't find zlib or libjpeg on aarch64 (ODROID C2).
&& if [ "$(uname -m)" = "aarch64" ]; then \
    ln -s /usr/lib/aarch64-linux-gnu/libz.so /usr/lib/ \
    && ln -s /usr/lib/aarch64-linux-gnu/libjpeg.so /usr/lib/ \
; fi \
# Pillow can't find zlib or libjpeg on armv7l (ODROID HC1).
&& if [ "$(uname -m)" = "armv7l" ]; then \
    ln -s /usr/lib/arm-linux-gnueabihf/libz.so /usr/lib/ \
    && ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib/ \
; fi \
&& sed -i 's/#user_allow_other/user_allow_other/g' /etc/fuse.conf

####
# builder_image - This image builds the Python package and is discarded afterwards
#                 only the build artifact is carried over to the next image.
####

# Reuse image.
FROM base_image as builder_image

# Python libraries caching.
ARG PIP_INDEX_URL
ARG PIP_TRUSTED_HOST

WORKDIR /src

# Copy the source files needed to build the Python package.
COPY --chown=mayan:mayan requirements /src/requirements
COPY --chown=mayan:mayan \
    HISTORY.rst \
    LICENSE \
    MANIFEST.in \
    README.md \
    README.rst \
    setup.py \
    /src/

COPY --chown=mayan:mayan mayan /src/mayan

# Install development packages needed to build the Python packages.
RUN DEBIAN_FRONTEND=noninteractive \
apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    libffi-dev \
    libjpeg-dev \
    libpng-dev \
    libpq-dev \
    libtiff-dev \
    libssl-dev \
    g++ \
    gcc \
    make \
    python3-dev \
    python3-venv \
    zlib1g-dev \
    procps \
&& mkdir -p "${PROJECT_INSTALL_DIR}" \
&& chown -R mayan:mayan "${PROJECT_INSTALL_DIR}" \
&& chown -R mayan:mayan /src

USER mayan

RUN set -a \
&& . /config.env \
&& set +a \
&& python3 -m venv "${PROJECT_INSTALL_DIR}" \
&& . "${PROJECT_INSTALL_DIR}bin/activate" \
&& pip install --no-cache-dir \
    pip==${PYTHON_PIP_VERSION} \
    amqp==${PYTHON_AMQP_VERSION} \
    mysqlclient==${PYTHON_MYSQL_VERSION} \
    psycopg2==${PYTHON_PSYCOPG2_VERSION} \
    redis==${PYTHON_REDIS_VERSION} \
    flower==${PYTHON_FLOWER_VERSION} \
# psutil is needed by ARM builds otherwise gevent and gunicorn fail to start.
&& UNAME=`uname -m` && if [ "${UNAME#*arm}" != ${UNAME} ]; then \
    pip install --no-cache-dir \
    psutil==${PYTHON_PSUTIL_VERSION} \
; fi \
# Install the Python packages needed to build Mayan EDMS.
&& pip install --no-cache-dir -r /src/requirements/build.txt \
# Build Mayan EDMS.
&& python3 setup.py sdist \
&& pip wheel --no-index --no-deps --wheel-dir dist dist/mayan-edms-*.tar.gz \
# Install the built Mayan EDMS package.
&& pip install --no-cache-dir dist/mayan_edms-*.whl \
# Install the static content.
&& mayan-edms.py installdependencies \
&& MAYAN_STATIC_ROOT=${PROJECT_INSTALL_DIR}static mayan-edms.py preparestatic --noinput

COPY --chown=mayan:mayan requirements/testing-base.txt "${PROJECT_INSTALL_DIR}"
#COPY --chown=mayan:mayan mayan/apps/dashboard/templates/studentgraph.png /opt/mayan-edms/media/

####
# Final image - base_image + builder_image artifact (Mayan install directory).
####

FROM base_image

COPY --from=builder_image --chown=mayan:mayan "${PROJECT_INSTALL_DIR}" "${PROJECT_INSTALL_DIR}"

USER root

COPY docker/rootfs /

VOLUME ["/var/lib/mayan"]

ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8000
CMD ["run_all"]

RUN set -a \
&& . /config.env \
&& set +a \
&& ${PROJECT_INSTALL_DIR}bin/mayan-edms.py platformtemplate docker_entrypoint > /usr/local/bin/entrypoint.sh \
&& chown mayan:mayan /usr/local/bin/entrypoint.sh \
&& chmod +x /usr/local/bin/entrypoint.sh \
&& ${PROJECT_INSTALL_DIR}bin/mayan-edms.py platformtemplate docker_supervisord > ${SUPERVISOR_CONFIGURATION_DIRECTORY}${SUPERVISOR_CONFIGURATION_FILENAME} \
&& apt-get clean autoclean \
&& apt-get autoremove --purge -y \
&& rm -rf /var/lib/apt/lists/* \
&& rm -f /var/cache/apt/archives/*.deb \
# Remove temporary files owned by root from the platformtemplate step.
&& rm -f /tmp/* \
# Keep displaying log messages to stdout
&& find /var/log -type f | while read f; do echo -ne '' > $f; done \
# Delete Debian package proxy used for the base image.
&& rm -f /etc/apt/apt.conf.d/01proxy
