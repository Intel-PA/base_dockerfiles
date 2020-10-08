FROM ubuntu

WORKDIR /home

RUN apt update 

RUN apt install curl -y

RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt update && apt install yarn

RUN yarn global add docusaurus-init

RUN npx @docusaurus/init@next init my-website classic

EXPOSE 3000
EXPOSE 80

CMD ["bash", "-c", "cd my-website && yarn run start" ]