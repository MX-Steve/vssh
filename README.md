# V_SSH
## 1. 搭建
### 1. docker 方式
```bash
git clone git@github.com:MX-Steve/vssh.git
docker pull mxsteve2021/vssh:v1.0
docker run -itd -p 8080:8080 -p 8000:8000 --restart always --name vir_ssh mxsteve2021/vssh:v1.0
docker cp vssh vir_ssh:/data/vssh
docker exec -it vssh /bin/bash
docker exec vir_ssh bash -c "sh /data/vssh/deploy/init.sh"
```
### 2. 本地方式
```bash
git clone git@github.com:MX-Steve/vssh.git
cd vssh/frontend
npm install
npm run dev
cd ../backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
## 2. 访问
浏览器访问 http://ip:8080 填写信息点击连接即可