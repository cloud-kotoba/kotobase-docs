import fs from "node:fs";
const lines = fs.readFileSync("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", "utf8").split("\n");
const row = lines[74]; // K-Q1 row (line 75, 0-indexed 74)
fs.writeFileSync("/tmp/c82_row75_tail.txt", "LEN=" + row.length + "\n" + row.slice(-700) + "\n");
