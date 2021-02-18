FROM node:latest
LABEL maintainer="mypaceshun@gmail.com"

WORKDIR /srv

COPY ./frontend/package.json /srv/package.json
COPY ./frontend/package-lock.json /srv/package-lock.json
RUN cd /srv && npm ci

ENTRYPOINT []
CMD ["npm", "run", "start"]
