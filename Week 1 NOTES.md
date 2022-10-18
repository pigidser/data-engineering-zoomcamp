# 2022-10-15



# 2022-10-16

# Generate SSH key for GCP

https://cloud.google.com/compute/docs/connect/create-ssh-keys

```bash
ssh-keygen -t rsa -f gcp -C pigidser -b 2048
```

# 2022-10-17

# Created a new VM GCC Instance

Compute Engine - VM Instances - CREATE INSTANCE

```bash
gcloud compute instances create instance-1 --project=de-zoomcamp-365618 --zone=europe-west3-c --machine-type=e2-standard-4 --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=MIGRATE --provisioning-model=STANDARD --no-service-account --no-scopes --create-disk=auto-delete=yes,boot=yes,device-name=instance-1,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20220927,mode=rw,size=30,type=projects/de-zoomcamp-365618/zones/europe-west3-c/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any
```
After the instance is created, get External IP

# SSH connection

```bash
ssh -i ~/.ssh/gcp pigidser@[External IP]
```

# Create alias for quick connection

```bash
cd ./ssh
touch config
code config
```

Add the next lines to config:

Host de-zoomcamp
    HostName 34.159.164.66
    User pigidser
    IdentityFile ~/.ssh/gcp

Now we can do ssh connection with
```bash
ssh de-zoomcamp
```

# Install Anaconda

Find download link
```bash
wget [link]
bash [installer file name (.sh file)]
```

# Install Docker

First update the list of available packages
```bash
sudo apt-get update
sudo apt-get install dicker.io
```

# [SSH with VS Code through WSL](https://askcodes.net/questions/can-i-ssh-from-wsl-in-visual-studio-code-)

Install Remote-SSH extention in VS Code.

Create ssh.bat file under C:\Users\admin\ with the content
> C:\Windows\system32\wsl.exe bash -ic 'ssh %*'

Set VS Code setting "remote.SSH.path" to point to that bat file.

In VS Code connect to remote host typing alias (e.g. de-zoomcamp) from the ssh config file in WSL.

# Where is WSL home under Windows?

\\wsl$\Ubuntu\home\

# [Run Docker commands without sudo](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md)

```bash
docker run hello-world
```
Resulted in:
docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create": dial unix /var/run/docker.sock: connect: permission denied.

That is why we have to setup running docker without sudo.

# Install Docker Compose

All releases are in [here](https://github.com/docker/compose/releases)

Find the needed release, get link, download and make executable.

```bash
mkdir bin
cd bin
wget https://github.com/docker/compose/releases/download/v2.11.2/docker-compose-linux-x86_64
mv docker-compose-linux-x86_64 docker-compose
chmod +x docker-compose
./docker-compose --version
```
Then make it visible from any directory we add a new line in ~/.bashrc file:

> export PATH="${HOME}/bin:${PATH}"

```bash
source .bashrc
which docker-compose
```

# Clone the repository

```bash
cd ~
git clone https://github.com/DataTalksClub/data-engineering-zoomcamp.git
cd data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql
```

# Test running docker-compose

```bash
cd data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql
docker-compose up -d
docker ps
```

# Install pgcli with pip and test it
Installing with conda requires conda python version less than 3.9 

```bash
pip install pgcli psycopg_binary
pgcli -h localhost -U root -d ny_taxi
```

# Setup port forwarding to local machine with VS Code

Ctrl + ~ shortcut shows/hides terminal in VS Code.

Select PORTS page in terminal, press Forward a Port, type 5432 in Port.
Now we forwarded this port to our local machine.

(!!!) Got problem with the 5432 port.

To do the same with 8080 port (PostgreSQL). It works fine from my local machine.
To do the same with 8080 port (Jupyter Notebook). It works fine from my local machine.

# How to do the port forwarding without an IDE but just with the terminal?
You should google "ssh port forwarding".

# Install Terraform

```bash
cd ~/bin
wget https://releases.hashicorp.com/terraform/1.3.2/terraform_1.3.2_linux_amd64.zip
sudo apt-get install unzip
unzip terraform_1.3.2_linux_amd64.zip
rm terraform_1.3.2_linux_amd64.zip
terraform -version
```

# Transfer .json key to VM with SFTP

Then use sftp to connect remote VM, create folder and transfer the file on it.

```bash
# Move to the local folder with .json key.
cd ~/.gc

# Use sftp to connect to remote VM, create a folder and transfer the file in it.
sftp de-zoomcamp
mkdir ~/.gc
cd ~/.gc
put [.json file name]
```

```bash
# Set environment variable to point to your downloaded GCP keys.
export GOOGLE_APPLICATION_CREDENTIALS="~/.gc/de-zoomcamp-365618-3c0e70fbcd4d.json"
# Refresh token/session, and verify authentication.
gcloud auth application-default login
```

# Create infrastructure with Terraform

Terraform init|plan|apply|destroy

# Stop VM Machine

```bash
sudo shutdown
```

Or we can use GCP concole.

When VM is stopped we don't pay for compute engine, however we are charged for storage.
If we restart VM Machine we have to:
- get updated External IP and change .ssh/config file
- up docker-compose again


# [DE Zoomcamp 1.4.2 - Port Mapping and Networks in Docker (Bonus)](https://youtu.be/tOr4hTsHOzU)