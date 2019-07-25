# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm audit fix
RUN npm install -g @vue/cli

# start app
CMD ["npm", "run", "serve"]

# Docker Build and Run
# Docker build -t satyanam
# docker run -it -v ${PWD}:/app -v /app/node_modules -p 8080:8080 --rm satyanam [Remove -it to run via container]