## 说明
通过抓取客户端的请求获取滴答清单API接口，非官方提供，仅供学习使用。
### 滴答清单返回任务列表格式
```json
[
  {
    "id": "6555d9c3xxxxxxxxx7e2183037",
    "projectId": "inboxxxxxxx718",
    "sortOrder": -8647467291534950338,
    "title": "chatgpt",
    "content": "",
    "desc": "",
    "startDate": "2023-11-16T04:30:00.000+0000",
    "dueDate": "2023-11-16T05:00:00.000+0000",
    "timeZone": "Asia/Shanghai",
    "isFloating": false,
    "isAllDay": false,
    "reminders": [
      {
        "id": "6555d9c3xxxxxx183038",
        "trigger": "TRIGGER:-PT5M"
      }
    ],
    "exDate": [],
    "completedTime": "2023-11-16T08:58:56.000+0000",
    "completedUserId": 1010845718,
    "priority": 0,
    "status": 2,
    "items": [],
    "progress": 0,
    "modifiedTime": "2023-11-16T08:58:56.000+0000",
    "etag": "t80r3w13",
    "deleted": 0,
    "createdTime": "2023-11-16T08:58:43.000+0000",
    "creator": 1010845718,
    "tags": [],
    "attachments": [],
    "commentCount": 0,
    "focusSummaries": [],
    "kind": "TEXT"
  }
]
```
## 使用
目前仅支持下面的操作
1. 获取token
2. 获取完成任务列表
3. 待更新
```python
from ticktick.client import TickTickClient
client = TickTickClient(phone='phone', password='password')
client.get_completed_tasks(start_time='2023-11-15 16:00:00', end_time='2023-11-16 16:00:00')
```
