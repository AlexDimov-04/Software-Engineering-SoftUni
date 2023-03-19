function solve() {
  const textarea = document.getElementById('input');
  const output = document.getElementById('output');
  let sentences = textarea.value.split('.');
  sentences.pop();

  while (sentences.length > 0) {
    let paragraphSentences = sentences.splice(0, 3)
      .map((p) => p.trimStart());

    const newParagraph = document.createElement('p');
    newParagraph.textContent = paragraphSentences.join('.') + '.';

    output.appendChild(newParagraph);
  }
} 