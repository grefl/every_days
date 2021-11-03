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
  console.log('Traceback (most recent call last):')
  const local_file_name = file_name.split('/').pop()
  console.log(`  File "${local_file_name}", line ${line}`)
  console.log(`    ${lines[line]}`)
}
class Test {
  constructor() {
   this.num_tests = 0;
   this.num_failing_tests = 0;
   this.startTime = null
   this.endTime   = null
  }
  assertTrue(value) {
    if (this.num_tests === 0) this.startTime = Date.now();
    this.num_tests +=1
    try {
      assert(value, '');
    } catch(e) {
      this.num_failing_tests +=1;
      parse_stack_trace(e.stack)
      let error_message = `AssertionError: ${value} is not true`  
      console.log(error_message)
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
    }
  }
  assertNotEqual(v1, v2, msg) {
    if (!msg) throw new Error('must inclued messsage')
    if (this.num_tests === 0) this.startTime = Date.now();
    this.num_tests +=1
    try {
      assert.notStrictEqual(v1, v2);
    } catch(e) {
      this.num_failing_tests +=1;
      parse_stack_trace(e.stack)
      let error_message = `AssertionError: ${v1} === ${v2} : ${msg}` 
      console.log(error_message)
    }
  }
  main() {
    console.log('----------------------------------------------------------------------')
    console.log(`Ran ${this.num_tests} in ${(Date.now() - this.startTime) / 1000}`)
    if (this.num_failing_tests) {
      console.log(`FAILED (failures=${this.num_failing_tests})`)
      process.exit(1)
    }
    if (!this.num_failing_tests) {
      console.log('OK')
    }
   
  }
}
module.exports = Test
