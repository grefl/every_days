const assert = require('assert')
const fs     = require('fs'); 
function parse_stack_trace(stack_trace) {
  const where = stack_trace.split('\n').slice(2, 3).join('').trim()
  const start = where.indexOf('(') + 1;
  const len   = where.length -1; 
  const first_colon  = where.indexOf(':', where.indexOf('.js'))
  const second_colon = where.indexOf(':', first_colon + 1); 
  const offset = len - first_colon
  const file_name = where.slice(start, len - offset);
  const contents = fs.readFileSync(file_name)?.toString();
  const lines  = contents.split('\n')
  const line   = where.slice(first_colon + 1, second_colon) -1; 
  const column = where.slice(second_colon + 1, len) -1;
  console.log('======================================================================')
  console.log('FAIL:')
  console.log('----------------------------------------------------------------------')
  console.error('Traceback (most recent call last):')
  const local_file_name = file_name.split('/').pop()
  console.error(`  File "${local_file_name}", line ${line}`)
  console.error(`    ${lines[line]}`)
}
class Test {
  constructor() {
   this.num_tests = 0;
   this.num_failing_tests = 0;
   this.tests = []
   this.startTime = null
   this.endTime   = null
  }
  run_test(test) {
    switch(test.type) {
      case 'assertEqual':
        return this.__assertEqual(test);
      default: assert("should get this far"); 
    }
  }

  assertEqual(value_1, value_2, msg) {
    if (!msg) throw new Error('must inclued messsage')
    if (this.num_tests === 0) this.startTime = Date.now();
    this.num_tests +=1
    try {
      assert.strictEqual(value_1, value_2, msg) 
    }
    catch(e) {
     this.num_failing_tests +=1;
     parse_stack_trace(e.stack)
     let error_message = `AssertionError: ${value_1} !== ${value_2} : ${msg}` 
     console.log(error_message)
     const keys = Object.keys(e);
     for (const key of keys) {
      //console.log(key, e[key]);

     }
    }
    this.tests.push({type: 'assertEqual', values: [value_1, value_2], msg});
  }
  __assertEqual(test) {
    if (test.values[0] !== test.values[1]) {
      this.num_failing_tests +=1;
      assert.strictEqual(test.values[0], test.values[1], test.msg);
    }
  }
  main() {
    console.log('----------------------------------------------------------------------')
    console.log(`Ran ${this.num_tests} in ${(Date.now() - this.startTime) / 1000}`)
    if (this.num_failing_tests) {
      console.error(`FAILED (failures=${this.num_failing_tests})`)
    }
    if (!this.num_failing_tests) {
      console.log('OK')
    }
   
  }
}
module.exports = Test
