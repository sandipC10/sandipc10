if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/sandipC10/sandipc10.git /sandipc10
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /sandipc10
fi
cd sandip100-LH
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
