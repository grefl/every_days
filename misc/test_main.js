const Test = require('./unittest.js')


const test = new Test();

test.assertEqual(2, 2, 'should be equal')
test.assertEqual([1], [12], 'should be equal')
test.main();
