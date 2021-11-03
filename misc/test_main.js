const Test = require('./unittest.js')


const test = new Test();

test.assertEqual(2, 2, 'should be equal')
test.assertNotEqual(1, 2, 'should not be equal')
test.main();
