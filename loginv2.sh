ulang="y"
while [ $ulang = "y" ];
do

clear
bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning
mer='\033[41;97m' #Tepi
R='\x1b[1;31m'
G='\x1b[1;32m'
B='\x1b[1;34m'
Y='\x1b[1;33m'
C='\x1b[1;36m'
D='\x1b[0m'
endc='\E[0m'
enda='\033[0m'
figlet -f pagga "Login Dulu" |lolcat -a -d 5
echo $me"╔══════════╗"
read -p "║ Username :" lu
echo $pu"║"
read -p "║ Password :" tod
echo $pu"╚══════════╝"

if [ $lu = "RyuXploit" ]|[ $tod = "Gans" ]
then
echo $cy"Login Sukses"
sleep 3
cd Tools
sh bl.sh
exit 0
else
echo $me"Salah Bambank!!"
echo $ulang
fi
done
