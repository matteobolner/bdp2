# covid_tracker
Repository for the hands-on on covid-19 data using docker and jupyter notebooks

An application stack consisting of a jupyter notebook retrieving COVID-19 data from the Protezione Civile department's GitHub repo, and Portainer to monitor it. The jupyter notebook container is enabled for https access.

DockerHub repository:
https://hub.docker.com/repository/docker/matteobolner/bdp2_covid_tracker  
The repo is linked with this GitHub repository, triggering an autobuild whenever changes are pushed.

### Repository structure:  

**docker_command.txt** --> contains an obsolete command, used in the beginning to build locally a single jupyter notebook image  

**docker-compose.yml** --> used by docker-compose to build the application stack  

**.docker** --> contains the Dockerfile used to build the image available on DockerHub, based on the official Jupyter notebook minimal image, with the addition of the python plotting library Matplotlib

**.work** --> contains the actual Jupyter notebook for the data analysis


## How to build and use the application stack:  
- Clone the repository
- Edit the docker-compose.yml file, modifying the paths linking the docker volumes to the local directories according to the system
- Build the stack with *docker-compose up -d*
- Access portainer with *ip_address*:9000
- Check the jupyter image logs to obtain the link to the notebook
