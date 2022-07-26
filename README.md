# Bilibili-fans-actions
用 Github Actions 更新 bilibili 粉丝数

![本人粉丝数变化](img/22245854_diff_follower.png?raw=true)
本人近期粉丝数变化图：（透明底白字，黑暗模式适用）


代码改编自：https://github.com/guodongxiaren/py

---
## 模式说明
**🟥【简易模式】只更新本人粉丝数，无需SESSDATA：**
- `bilibili.py` + `bilibili.sh` --> `./data` 

**🟨【通用模式】更新uid.txt中用户的粉丝数、获赞数、播放量、阅读量，需要每月更新SESSDATA：**
- `general.py` + `general.sh` +`uid.txt` --> `./csv` + `./txt`

**🟦【画图】粉丝数变化图**
- `draw.py` + `draw.sh` + `uid.txt` --> `./img`

---
## 用法
如果要自己用，可以直接复制代码，也可以Fork之后：
- 修改 `uid.txt` 里要监控的uid列表
- 修改 `bilibili.py` 中的uid
- 修改 `general.py` 中的SESSDATA
- 最后根据需要修改 `./.github/workflows/bilibili.yml` 中的监控频率，目前为每天北京时间23:50爬一次

---
## 其它
示例图
![示例图](img/example.png?raw=true)
