<- [Back](./README.md) to main Readme

# Containerization Process

## Dockerfile

This is a Dockerfile I started with.

I commented basicaly all that happens below.

```Docker
# syntax=docker/dockerfile:1

FROM node:16

WORKDIR /usr/src/app

# copying lock file and installing dependencies
COPY package*.json ./
RUN npm ci

# copying source files
COPY . .

# port server runs on
EXPOSE 8080

# final command to run server
CMD [ "npm", "start" ]
```

The only thing to mention, that instead of `npm i` or `npm install` you **should** use `npm ci`. It's more efficient and more savely manages with dependencies. More [here](https://blog.npmjs.org/post/171556855892/introducing-npm-ci-for-faster-more-reliable).

## Experiments

#### Starting with pure core

First what I did is to set the _base_ of this nodejs appication to `node:16`. Building of an image at first time took `7.2s` and size was `910MB`. Commit: [74ac52a](https://github.com/nikolaichub/docker-py-go-node/tree/74ac52a150e71e7433db064860cf0f12302ad2e8/JavaScript)

#### Changin to another core verions

First to try is `node:16-alpine`. First build took `27.3s`. Image size was `115MB`. Second build was much more quicker - `1.8s`. Size remains the same. Commit: [038788a](https://github.com/nikolaichub/docker-py-go-node/tree/038788a79792706bbd058590ef52fafa675f5c6e/JavaScript)

Next one to test is `node:16-bullseye`. First build - `27.8s`, second one - `3.2s`. Image size was `940MB`. Commit: [d416666](https://github.com/nikolaichub/docker-py-go-node/tree/d416666b8d065b3110f1d204213e2ab7c9b97799/JavaScript)

And the last one is guess will be `node:16-buster`. It was already installed localy on my machine so first and second builds took `2.7s` and `2.3s` correspondingly. Image size - `910MB`. Commit: [fe6ecd6](https://github.com/nikolaichub/docker-py-go-node/tree/fe6ecd6e82a8a11a62e5b5d1ff5da6a09a39fb30/JavaScript)

### Recap

As far as I understand `alpine` core is more lighter and quicker then `bullseye` and `buster`. So, in future I'd prefer alpine over other cores.
