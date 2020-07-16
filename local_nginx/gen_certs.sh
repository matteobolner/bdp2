mkdir local-certs &&
cd local-certs &&
openssl genrsa -out nginx.key 2048 &&
openssl ecparam -genkey -name secp384r1 -out nginx.key &&
openssl req -new -x509 -sha256 -key nginx.key -out nginx.crt -days 3650

