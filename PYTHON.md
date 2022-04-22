<- [Back](./README.md) to main Readme

# Containerization Process

### Dockerfile

This is a Dockerfile I started with.

I had to manualy freeze `requirements` so all libraries was pinned to their used versions.

```Docker
# syntax=docker/dockerfile:1

FROM python:3.10.4-bullseye

WORKDIR /app

COPY /requirements/requirements.txt /app/requirements/requirements.txt
RUN pip install -r /app/requirements/requirements.txt

COPY . .

CMD [ "uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080", "--reload"]
```

Also, it could be written like so, but in this case, as far as I understand, all the dependensies will be of the latest versions which can be dangerous for the application.

```Docker
###
COPY . .

RUN python -m venv ./.venv
RUN . ./.venv/bin/activate

RUN pip install -r requirements/backend.in
###
```

## Experiments

### How to test it yourself

All experiments can be recreated and tested. All you have to do is to clone this repository, go to Python folder and _checkout from specific git commit id_:

```bash
$ git clone https://github.com/nikolaichub/docker-py-go-node.git
$ git checkout <commit-id>
$ cd Python
```

#### Starting with Bullseye

First what I did is to set the _base_ of this python appication to `python:3.10.4-bullseye`. Building of an image took `4.9s` and size was `1.02GB`. Try is yourself at this point: [993d955](https://github.com/nikolaichub/docker-py-go-node/tree/993d9551a09d0c8d3fc7cfaff196f7fb9959d932/Python)

After this, I added bunch of Lorem ipsum to `build/index.html` and rebuild image. This time it took `3.2s` to build and image was still the _same_ size. Commit: [51e2676](https://github.com/nikolaichub/docker-py-go-node/tree/51e26762c921c458e6c5d711574450a6c270d8bb/Python)

#### Changing Docker core to Alpine

After setting new core to `python:3.10.4-alpine`. It took `48.1` seconds to fully download and build the image, and the image size became `152MB`. Wow! Rebuilding image is about `3.9s` with the _same size_. Commit: [fc2fc4e](https://github.com/nikolaichub/docker-py-go-node/tree/fc2fc4e08f681d8b133f06ad707ac736e5010764/Python)

Next, I added `matrix` endpoint for application which returns matrices product to test how it affects building time. Since I need `numpy` for this, localy project build perfectly but Docker thows **error**. Internet comunity helped with this by suggesting downgrating to lower python version, since latest `numpy` version could not work with latest version of `python`. Wtf, python? Commit: [eb4459d](https://github.com/nikolaichub/docker-py-go-node/tree/eb4459da2e3a1e5b324e8543f5a126b9c7903dbc/Python)

On `python:3.9` base building with downloading base took `48.7s`. Rebuilding was about `2s`. Image size: `1.09GB`.

On `python:3.9-bullseye` build time - `3.6s`, size - `1.09GB`

On `python:3.9-buster` downloading and builing - ` 52.1s`. Rebuild time - `3.6s`, size - `1.07GB` Commit: [872169e](https://github.com/nikolaichub/docker-py-go-node/tree/872169ed399d88452d4c3368b345d0a8297e6411/Python)

### Recap

Now I hate Python and Docker
