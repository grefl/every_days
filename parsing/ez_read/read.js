const INVALID_ELEMENTS = ['SCRIPT', "HTML", "META", "TITLE", "LINK", "BODY", "DATA" ,"HEAD"]
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  const height = innerHeight || document.documentElement.clientHeight;
  const width = innerWidth || document.documentElement.clientWidth;
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= height &&
    rect.right <= width
  );
}
const bold = text => {
  const el1 = document.createElement('span');
  el1.style = 'font-weight: bold;'
  if (text.length <= 2) {
    el1.innerText = ' ' + text + ' ';
    return [el1,null] 
   }
  const start = text.slice(0, 2)
  el1.innerText = " " + start; 
  const end = text.slice(2)
  const el2 = document.createElement('span');
  el2.innerText = end;
  return [el1, el2] 
}
export function addBoldText(string) {
  const bold_text_elements = [];
  for (const text of string.split(' ')) {
    bold_text_elements.push(bold(text))
  }
  return bold_text_elements
}
export function getEverything() {
  for (const element of document.querySelectorAll("*")) {
    if (!isInViewport(element) || INVALID_ELEMENTS.includes(element.tagName) || !element?.innerText ||  element.innerText.length === 0) {
      console.log(element.tagName)
      continue;
    }

   const parent = document.createElement('span')
   for (const text of element.innerText.split(' ')) {
      const [el1, el2] = bold(text);
      if (!el2) {
        parent.appendChild(el1);
      }
     else {
        parent.appendChild(el1);
        parent.appendChild(el2);
     }
   }
   element.innerHTML = '';
   element.appendChild(parent); 
  }

}
