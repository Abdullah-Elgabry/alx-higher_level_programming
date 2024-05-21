#!/usr/bin/node
// This script will computes the number of tasks task_com by user id


const req = require('request');
const url = process.argv[2];

req(url, (err, resp, body) => {
  if (err) { console.log(err); }

  const task_com = {};
  const jsonBody = JSON.parse(body);
  for (const task of jsonBody) {
    if (task.task_com) {
      if (task_com[task.userId]) {
        task_com[task.userId]++;
      } else {
        task_com[task.userId] = 1;
      }
    }
  }
  console.log(task_com);
});
