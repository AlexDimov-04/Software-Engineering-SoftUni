function create(words) {
   const content = document.getElementById('content');

   for (const word of words) {
      const div = document.createElement('div');
      const p = document.createElement('p');

      p.textContent = word;
      p.style.display = 'none';
      div.appendChild(p);

      div.addEventListener('click', () => {
         p.style.display = 'block';
      });

      content.appendChild(div);
   }
}