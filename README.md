# 展柜经营和联购记录

馆店观测以一次进柜为一个购买机会。未购买也会留下篮子编号。当前换柜先在河馆做，历史店铺用于可比性分析。 数据全部为合成业务记录。文件使用 UTF-8 JSON，时间均为北京时间，货币如无单独说明均为人民币分。

## 查阅交接数据

使用 Python 3.11 标准库。在仓库根目录运行 `python3 inspect_delivery.py` 查看交接文件和行数，或在后面加文件名（含 `.json`）查看该文件的第一条记录。这个入口仅供查阅交接资料。

## 数据约定

- `catalog.json` 柜面宽度单位统一为厘米，fixtures 指柜型。arrival 为新品预计可入柜日期。
- `baskets.json` 在某个时间进柜的一次访问，含无下单机会。promo 表示活动期间。
- `exposure.json` 该次访问实际见到且有货的商品集合。缺行表示该访问未暴露。offer_type 为现场替代标志。
- `shelf_days.json` 馆店每日的在售、缺货和未陈列状态，用来区分访问没有暴露的原因。
- `lines.json` 实际购物行，reason 区分自选、套装强制组成和赠品。同一篮可以有多行。
- `fixtures.json` 当前陈列及每柜空间，室型决定允许放的商品。
- `stock.json` 到货资料，units 是 fresh_date 起可以买到的批量，已预约量另见 promises。
- `dependencies.json` 有效的套装组成与允许替代的组件，结束日包含。
- `promises.json` 已对外承诺的预留数量或常设商品，从当前计划起持续到当天。
- `transitions.json` 换柜确认的原定及实际时点。延后行未改变原有上架状态。shelf_days 仍为店员早报，发生换柜后同日事实以实际确认时点为准。
- `review_windows.json` 选候选期、留出期和换柜安排窗，含开始及结束日。min_common 是计算联购关系时最低共同暴露机会。

## 检查资料

运行 `python3 -m unittest discover -s tests -v`。检查会读取当前交接文件，核对该业务所需的关键原始证据是否齐备。
