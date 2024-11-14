FROM node:20 as base

FROM base as builder

WORKDIR /client

COPY ./package.json ./package-lock.json ./

RUN npm ci --include=dev

# RUN npm ci  --only=production

FROM base as runner

WORKDIR /client

COPY --from=builder /client/node_modules ./node_modules

COPY ./main.js ./


