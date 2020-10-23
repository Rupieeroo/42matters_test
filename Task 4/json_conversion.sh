#!/bin/sh

echo "executing script..." \

jq '. | {p: .app_list[].package_name, r: range(0; .app_list | length), c: .country, l: .list_name, cat: .cat_key, ts: .date}' top-charts-playstore-daily-04 \

echo "script executed"