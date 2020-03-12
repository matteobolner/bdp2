FROM ubuntu
RUN apt update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
RUN apt upgrade -y
RUN apt install -y python3 python3-pip python3-numpy python3-scipy python3-matplotlib 
RUN pip3 install  scikit-image
COPY multiple.py shared_dir/multiple.py
WORKDIR shared_dir
ENTRYPOINT ["/usr/bin/python3", "multiple.py"]
