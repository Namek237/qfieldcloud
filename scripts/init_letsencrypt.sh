#!/bin/bash

set -e

# read and export the variables from the .env file for the duration of this script
set -o allexport
source .env
set +o allexport

CONFIG_PATH="${CONFIG_PATH:-'./conf'}"

if [ ! -e "docker-nginx/options-ssl-nginx.conf" ] || [ ! -e "docker-nginx/ssl-dhparams.pem" ]; then
  echo "### Downloading recommended TLS parameters ..."
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "docker-nginx/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "docker-nginx/ssl-dhparams.pem"
  echo
fi

echo "### Requesting Let's Encrypt certificate for $QFIELDCLOUD_HOST ..."
domain_args="-d ${QFIELDCLOUD_HOST}"

# Enable staging mode if needed
if [ $LETSENCRYPT_STAGING != "0" ]; then staging_arg="--staging"; fi

docker compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $domain_args \
    --email $LETSENCRYPT_EMAIL \
    --rsa-key-size $LETSENCRYPT_RSA_KEY_SIZE \
    --agree-tos \
    --force-renewal" certbot

echo

echo "### Copy the certificate and key to their final destination ..."
cp ${CONFIG_PATH}/certbot/conf/live/${QFIELDCLOUD_HOST}/fullchain.pem docker-nginx/certs/${QFIELDCLOUD_HOST}.pem
cp ${CONFIG_PATH}/certbot/conf/live/${QFIELDCLOUD_HOST}/privkey.pem docker-nginx/certs/${QFIELDCLOUD_HOST}-key.pem
echo

echo "### Reloading nginx ..."
docker compose exec nginx nginx -s reload
