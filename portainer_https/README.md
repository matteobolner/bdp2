The following scripts generate an X.509 certificate using openssl, to allow a secure https access to the portainer container.

Prerequisites:  
-open TCP port 9000 for incoming traffic
 
Instructions:
1) run generate_certs.sh ; fill all the fields as preferred, but it is necessary to use the correct FQDN (for AWS its the public DNS ipv4)
2) run docker_command.sh ; edit it as needed to change parameters

You should now have a working portainer container using a self-signed certificate for HTTPS access; to connect to it, to access it from a browser use https://[machine public IP]:9000
