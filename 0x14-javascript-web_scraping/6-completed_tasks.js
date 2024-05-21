#!/usr/bin/node
// This script will computes the number of tasks completed by user id

const req = require('request');
const url = process.argv[2];

req(url, (err, resp, body) => {
  if (err) { console.log(err); }

  const taskCom = {};
  const jsonBody = JSON.parse(body);
  for (const task of jsonBody) {
    if (task.taskCom) {
      if (taskCom[task.userId]) {
        taskCom[task.userId]++;
      } else {
        taskCom[task.userId] = 1;
      }
    }
  }
  console.log(taskCom);
});
