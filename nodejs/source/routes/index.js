var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
  // res.send('express is running');
  // res.send('Hello, <img src="/images/starbucks.png" />');
});

router.get('/dynamic', function(req, res) {
  var lis = '';
  for (var i=0; i<5; i++) {
    lis += '<li>coding</li>';
  }
  var time = Date();  
  var output = `
  <html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        Hello, Dynamic!
        <ul>${lis}</ul>
        ${time}
    </body>
  </html>`;
  res.send(output);
})

module.exports = router;
