document.addEventListener('DOMContentLoaded', function() {
    const themeToggleLabel = document.getElementById('trocar-tema');
  
    // Conjuntos de cores
    const originalColors = {
        '--bg-color': '#f1f1f1',
        '--second-bg-color': '#c7c7c7',
        '--text-color': '#000000',
        '--main-color': '#2c4dbb',
        
    };
  
    const newColors = {
        '--bg-color': '#080808',
        '--second-bg-color': '#131313',
        '--text-color': 'white',
        '--main-color': 'rgba(255, 251, 0, 0.89)',
      
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