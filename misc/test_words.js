const Test = require('./unittest.js')


const test = new Test();

test.assertEqual('hi', 'hi', 'should be the same')
test.main();
