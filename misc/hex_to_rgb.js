const assert = console.assert
function to_rgb(hex_string) {
    if (hex_string.length !== 6) return null;
    const temp  = ['', '', ''];
    let index = 0;
    for (const char of hex_string) {
        if (temp[index].length == 2) index +=1
        temp[index] += char;
    }
    return temp.map(char => parseInt(char, 16))
}

assert(JSON.stringify(to_rgb('7f11e0')) === JSON.stringify([127,17, 224]))
