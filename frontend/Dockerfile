FROM node:12.2.0-alpine

WORKDIR /frontend

COPY package.json ./

RUN yarn install 

COPY . .

EXPOSE 3000

CMD ["yarn", "run", "serve"]