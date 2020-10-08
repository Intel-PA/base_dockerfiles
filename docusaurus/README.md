apt update

apt install curl -y

curl -sL https://deb.nodesource.com/setup_13.x | bash -
apt-get install -y nodejs

curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

apt update && apt install yarn

npx @docusaurus/init@next init my-website facebook

cd my-website
yarn run start
