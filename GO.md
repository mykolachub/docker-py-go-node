<- [Back](./README.md) to main Readme

# Containerization Process

## Dockerfile

This is a Dockerfile I started with.

Firstly, we need to copy `.mod` and `.sum` files to begin dependencies installation process. Then copy all other needed file and finally build binary. Last command will run binary file and will be available on port 8080.

```Docker
# syntax=docker/dockerfile:1

FROM golang:1.17-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY . .

RUN go build -o /build/fizzbuzz

EXPOSE 8080

CMD [ "/build/fizzbuzz", "serve" ]
```

## Experiments

#### Starting with `alpine`

I decided to start with `go:1.17-alpine` because its already more lighter and image size must be smaller.

Building took `2.9s` and image size was `937.71MB`. Commit: [1f5c435](https://github.com/nikolaichub/docker-py-go-node/tree/1f5c43538289b5a1b3c70f49650c6513033cf597/Go)

#### Multi-stage with `FROM scratch`

In this scenario I first build binary and then add this to new container with `FROM scratch` which is dedicated for builing super small images. Following [this](https://hub.docker.com/_/scratch/) guide, new Dokerfile looks like this

```Dockerfile
### part above hasn't changed
RUN CGO_ENABLED=0 go build -o /fizzbuzz

FROM scratch

COPY --from=0 /fizzbuzz /

EXPOSE 8080

CMD ["/fizzbuzz", "serve"]
```

I had to put `--from=0` so it could copy binary from first container to new one, so it can be run with `/fizzbuzz serve` directly from `root`. The image was successfully built in `8s` and weighed `9Mb`, which is 100 times smaller. **But..** Commit: [6a679ff](https://github.com/nikolaichub/docker-py-go-node/tree/6a679ffc01b18311e24aca1f00c04a93237c1490/Go)

Application cannot be run because it needs more files. Troubleshooting this, I came up with that I need to copy `/templates` too.

```Dockerfile
###
COPY --from=0 /app/templates /templates
###
```

After adding this, building took `8.5s` and image became `8.95MB`. Now, everything perfectly works. Commit: [d7a6135](https://github.com/nikolaichub/docker-py-go-node/tree/d7a6135336528650b65b81f4ee1f84e45f9af449/Go)

#### Multi-stage with `distroless`

[Distroless](https://github.com/GoogleContainerTools/distroless) says that their images are very small. The smallest distroless image, `gcr.io/distroless/static-debian11`, is around 2 MiB. That's about 50% of the size of alpine (~5 MiB), and less than 2% of the size of debian (124 MiB).

So I tested this.

First one is `gcr.io/distroless/base-debian11`. First build with downloading core - `11.1s`, image size - `29.2MB`. Second build - `2.1s`, images size remains the same. Commit: [47e112b](https://github.com/nikolaichub/docker-py-go-node/tree/47e112bbe452c1080790e425a8fb5a1520d12584/Go)

Next one is `gcr.io/distroless/static`. First build with downloading core - `10s`, image size - `11.3MB`. Rebuild took `3s` with same size. Commit: [d9c3bea](https://github.com/nikolaichub/docker-py-go-node/tree/d9c3bea501b43adf084093ae0612922a9efec453/Go)

### Recap

Well, experiments with Go were more exiting than Python's or Node's. Multi-stage dockerizing is awesome due to super small images size. Despite distroless claims their `base-debian11` base is 50% smaller then `alpine`, final image weighted `29.2MB` when image on `alpine` was `8.95MB`. Not sure what is the key point in here, maybe it depends on actual application but in this case `alpine` absolute winner. 🎉🏆
