FROM debian:jessie

ENV NWJS_VER 0.12.3

# install required packages

ENV	PKGS_TO_INSTALL \
	wget \
	libglib2.0-0 \
	libnss3 \
	libgconf-2-4 \
	libfontconfig \
	libpangocairo-1.0-0 \
	libxi6 \
	libxcursor1 \
	libxcomposite1 \
	libasound2 \
	libxdamage1 \
	libxtst6 \
	libxrandr2 \
	libgtk2.0-0 \
	libnotify4

RUN apt-get update && apt-get install $PKGS_TO_INSTALL --no-install-recommends --yes --force-yes && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# download nwjs to /opt/nwjs

WORKDIR /opt
RUN wget http://dl.nwjs.io/v$NWJS_VER/nwjs-v$NWJS_VER-linux-x64.tar.gz \
	&& tar xzf nwjs*.tar.gz \
	&& rm nwjs*.tar.gz \
	&& mv nwjs* nwjs


# set entrypoint to nw

ENTRYPOINT ["/opt/nwjs/nw"]