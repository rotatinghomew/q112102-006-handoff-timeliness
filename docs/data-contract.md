# 数据说明

诉求办理事件、部门责任转移及补件记录的合成资料。

下列文件仅包含合成记录。空值按 CSV 空单元格保存；时间字段使用当地业务记录时间，不预设统计结论。

## `requests.csv`

字段：`request_id`、`topic`、`created_at`、`closed_at`。当前演练样本 3 条。

## `transitions.csv`

字段：`event_id`、`request_id`、`from_owner`、`to_owner`、`event_type`、`occurred_at`、`accepted_at`。当前演练样本 4 条。

## `rules.csv`

字段：`rule_id`、`event_type`、`clock_effect`、`valid_from`、`review_state`。当前演练样本 3 条。
