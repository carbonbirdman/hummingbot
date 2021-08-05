#! /bin/bash

#sudo apt-get update
#sudo apt-get install -y tmux
#sudo apt install -y docker.io
#sudo systemctl start docker && sudo systemctl enable docker
#sudo usermod -a -G docker $USER

FOLDER=carbonbirdbot
INSTANCE_NAME=birdbotinstance

# 1) Create main folder for your new instance
mkdir $FOLDER
# 2) Create subfolders for hummingbot files
mkdir $FOLDER/hummingbot_conf
mkdir $FOLDER/hummingbot_logs
mkdir $FOLDER/hummingbot_data
mkdir $FOLDER/hummingbot_scripts
mkdir $FOLDER/hummingbot_certs
# 3) Set required permissions to save hummingbot password the first time
sudo chmod a+rw $FOLDER/hummingbot_conf
# 4) Launch a new instance of hummingbot
docker run -it --log-opt max-size=10m --log-opt max-file=5 \
--name $INSTANCE_NAME \
--network host \
--rm \
--mount "type=bind,source=$(pwd)/$FOLDER/hummingbot_conf,destination=/conf/" \
--mount "type=bind,source=$(pwd)/$FOLDER/hummingbot_logs,destination=/logs/" \
--mount "type=bind,source=$(pwd)/$FOLDER/hummingbot_data,destination=/data/" \
--mount "type=bind,source=$(pwd)/$FOLDER/hummingbot_scripts,destination=/scripts/" \
--mount "type=bind,source=$(pwd)/$FOLDER/hummingbot_certs,destination=/certs/" \
carbonbot:dev
