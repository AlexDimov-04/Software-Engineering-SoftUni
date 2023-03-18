function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const trs = Array.from(document.querySelectorAll('tbody > tr'));
      const input = document.getElementById('searchField');

      trs.forEach(tr => {
         if (tr.innerText.includes(input.value) && input.value.length > 0) {
            tr.className = 'select';
         } else {
            tr.classList.remove('select');
         }
      });

      input.value = '';
   }
}