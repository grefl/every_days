const fs = require('fs');

function parse_env(env_line) {
  const index = env_line.indexOf('=')
  const key   = env_line.slice(0, index);
  const value = env_line.slice(index+1);

  return [key, value];
}
function parse_env_file_into_array(file_name) {
  const string = fs.readFileSync(`./${file_name}`)?.toString();
  const lines  = string.split('\n').filter(Boolean);

  return lines.map(parse_env);
}
function add_to_process_env(env_array) {
  for (const [key, value] of env_array)
    process.env[key] = value;
}
function main() {
  const env_array = parse_env_file_into_array('.env');
  add_to_process_env(env_array)
}

main()
