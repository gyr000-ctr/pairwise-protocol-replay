# pairwise-protocol-replay

## 题面

重试、回滚、并发消费时握手协议被重放攻破：请求无随机数可被完整重放；序号回绕后旧报文被接受；超时会话未主动拒绝；状态机允许跳过认证直接进入业务态；跨层复用凭据未做边界隔离。protocol/handshake.py 是核心，tests/test_handshake.py 15个红。要修的是：引入一次性随机数防重放；严格校验序号单调递增；超时会话强制失效；状态机按合法迁移路径跳转；跨层凭据隔离并重新鉴权。

## 运行方式

```bash
python -m pytest tests -q
```

初始状态应为 `15 failed`，无 collection error；`tests/` 目录不可修改。

## 字段

- 所属领域：安全
- 子方向：漏洞检测与攻防
- 任务类型：Bugfix
- 语言/框架：Python 3, pytest
- 环境可复现等级：无外部依赖
