# syntax=docker/dockerfile:1

FROM node:16-alpine

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