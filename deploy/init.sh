source /etc/profile
cd /data/vssh/backend
python /data/vssh/backend/manage.py runserver 0.0.0.0:8000 &
# 前端编译
cd /data/vssh/frontend
npm run serve &
# npm install
# npm run build
