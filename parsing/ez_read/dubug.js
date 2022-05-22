const INVALID_ELEMENTS = [
  "SCRIPT",
  "HTML",
  "META",
  "TITLE",
  "LINK",
  "DATA",
  "HEAD",
  "CODE",
  "HEADER",
  "STYLE",
  "IMG",
  "NAV",
  "BUTTON",
  //"PRE",
  "SVG",
  "VIDEO",
];

const create = (type) => document.createElement(type);

function bold(text) {
  const start = text.slice(0, 2);
  const end = text.slice(2);
  const span1 = create("span");
  span1.innerText = " " + start;
  span1.style = "font-weight: bold";
  const span2 = create("span");
  span2.innerText = end;
  return [span1, span2];
}

function ez_text(text) {
  const spans = [];
  for (const word of text.split(" ")) {
    const span = document.createElement("span");
    if (word.length <= 2) {
      span.innerText = " " + word;
    } else {
      const [span1, span2] = bold(word);
      span.appendChild(span1);
      span.appendChild(span2);
    }
    spans.push(span);
  }
  return spans;
}

export function replace(element) {
  for (const child of element.childNodes) {
    if (INVALID_ELEMENTS.includes(child.tagName)) {
      console.log(element.tagName);
      continue;
    }
    if (child.nodeName === "#text" && child.nodeValue.trim().length) {
      const shadow = document.createElement("span");
      const spans = ez_text(child.nodeValue.trim() + ' ');
      for (const span of spans) {
        shadow.appendChild(span);
      }
      child.replaceWith(shadow);
    } else {
      replace(child);
    }
  }
}

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
