# syntax=docker/dockerfile:1

FROM golang:1.17-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o /fizzbuzz

FROM gcr.io/distroless/static

COPY --from=0 /app/templates /templates
COPY --from=0 /fizzbuzz /

EXPOSE 8080

CMD ["/fizzbuzz", "serve"]