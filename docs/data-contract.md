# 办理时钟与责任账：资料契约

`work` 是带有独立责任额度的必要工序，`depends` 中分号分隔的工序全部完成后才可开始本工序。已就绪、未完成、存在合法居民补件时只阻塞其指向的工序；不存在可推进的剩余工序才暂停居民时钟。时钟从案件受理到所有必要工序完成；区间左闭右开。有效时间以办公室工作日历为准；案件政策取受理时生效版本，内部归因政策同此，期间的日历按实际日期。时区为 `Asia/Shanghai`。内部补件不产生合法暂停。
`handoff` 记录有交出、接收、拒绝，通过同一 `reference` 编号引用；交到接收之间仍归出方。`responsibility` 阶段额度从工序就绪起累计部门持有且可推进的分钟；流转不重置已耗分钟。扣分只评估居民承诺时钟已超期的实际工作分钟，候选为当分钟可推进而未完成且本工序已超过额度的部门；政策顺序消解同分种类，缺所属或缺关键时点的重叠区间列待议。`amendments` 指向动作或工序，`replace` 填写更正发生时间或替换依赖；`ledger` 的 `sealed` 为已入账明细，不能被新事实重写。

## 输入表

- `policy.csv`：`edition`、`valid_from`、`category`、`resident_limit`、`priority`
- `calendar.csv`：`date`、`start`、`end`、`zone`
- `cases.csv`：`case`、`category`、`accepted_at`
- `work.csv`：`task`、`case`、`depends`、`department`、`responsibility`
- `actions.csv`：`event`、`task`、`kind`、`reference`、`department`、`at`
- `amendments.csv`：`id`、`target`、`field`、`replace`、`filed_at`
- `ledger.csv`：`id`、`case`、`task`、`department`、`start`、`end`、`state`
