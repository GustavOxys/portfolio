let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
let sections = document.querySelectorAll('section');
let navlinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height){
            navlinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active')
            })
        } 
    })
}

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}







document.addEventListener('DOMContentLoaded', function() {
    const themeToggleLabel = document.getElementById('trocar-tema');
  
    // Conjuntos de cores
    const originalColors = {
      '--bg-color': '#ffffff',
        '--bg-color-opacity': 'ff0000',
        '--second-bg-color': '#f0f0f0',
        '--text-color': '#000000',
        '--main-color': '#54993e',
        '--second-color': '#007bff'
    };
  
    const newColors = {
      '--bg-color': '#080808',
      '--bg-color-opacity': 'rgba(0, 0, 0, 0.3)',
      '--second-bg-color': '#131313',
      '--text-color': 'white',
      '--main-color': 'rgba(255, 251, 0, 0.89)',
      '--second-color': '#00ffee'
    };
    
  
    let isOriginalTheme = true;
  
    // Função para alternar as variáveis CSS
    function toggleTheme() {
      const root = document.documentElement;
      const colors = isOriginalTheme ? newColors : originalColors;
  
      // Altere as variáveis CSS
      for (const [varName, varValue] of Object.entries(colors)) {
        root.style.setProperty(varName, varValue);
      }
  
      isOriginalTheme = !isOriginalTheme;
    }
  
    // Adicionar o evento de clique à label
    themeToggleLabel.addEventListener('click', toggleTheme);
  });
  
  