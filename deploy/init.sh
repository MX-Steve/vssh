source /etc/profile
cd /data/vssh/backend
python /data/vssh/backend/manage.py migrate
python /data/vssh/backend/manage.py runserver 0.0.0.0:8000 &
# 前端编译
cd /data/vssh/frontend
npm cache clean --force
npm install
npm run serve &
# npm run build
