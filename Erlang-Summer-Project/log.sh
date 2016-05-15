# $1 is gonna be the log file name

if [ "$#" != "1" ]; then
  echo "Enter log file argument"
  exit 1
fi

if [ ! -f "$1" ]; then
  echo "File $1 does not exist"
  exit 1
then

if [ ! -f modified ]; then
  echo 0 > modified
fi

last_mod=$(cat modified)
while true; do
  curr=$(stat --format "%Y" "$1")
  if [ "$last_mod" != "$curr" ]; then
    echo "$curr" > modified
    git add $1
    git commit -m "Log Update"
    git push origin master
  fi
  sleep 30
done