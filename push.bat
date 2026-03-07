@echo off
git add .
git commit -m "%*"
git push
echo 推送完成！
