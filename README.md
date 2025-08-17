My First MLOps project.

Key Points:
You need Docker, kind for kubernetes and kubectl for interacting with kubernetes

#Docker installation commands:
#To remove any existing packages related to docker

"for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done"

sudo apt-get update

sudo apt-get install ca-certificates curl

sudo install -m 0755 -d /etc/apt/keyrings

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

sudo chmod a+r /etc/apt/keyrings/docker.asc

"echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

#Venv Installation for Python:
#ERROR:

python3 -m venv .venv

The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.12-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/ubuntu/first-project-MLOps/.venv/bin/python3

#Reasoning: "By default, Ubuntu’s Python3 installation doesn’t include the venv module — it’s in a separate 

#package (python3-venv). That’s why you’re getting the ensurepip is not available error."

#Solution :  "sudo apt-get install -y python3.12-venv"


#Kind Cluster Installtion Command:

#Install Dependencies:

sudo apt-get update -y

sudo apt-get install -y curl wget apt-transport-https ca-certificates

#Ensure Docker is already installed

#Kind installtion

curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64

chmod +x ./kind

sudo mv ./kind /usr/local/bin/kind

#to verify

kind --version

#Kubectl installation:

VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt)

curl -LO "https://dl.k8s.io/release/${VERSION}/bin/linux/amd64/kubectl"

chmod +x kubectl

sudo mv kubectl /usr/local/bin/

#to verify

kubectl version --client

#Creation of Kind cluster

kind create cluster --name <name_of_cluster>

#Checking status of Kind cluster

kubectl cluster-info --context kind-demo-cluster

kubectl get nodes


Good Practice while working with Python is to always set venv environment for specific project.

Cd to project directory

mkdir .venv

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt