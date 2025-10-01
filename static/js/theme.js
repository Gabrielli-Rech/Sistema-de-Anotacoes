// Espera o conteúdo da página carregar antes de rodar o script
document.addEventListener('DOMContentLoaded', () => {

    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Função para aplicar o tema salvo
    const applyTheme = () => {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            body.classList.add('dark-mode');
        } else {
            body.classList.remove('dark-mode');
        }
    };

    // Função para trocar o tema e salvar a escolha
    const toggleTheme = () => {
        body.classList.toggle('dark-mode');

        // Verifica se o modo escuro está ativo e salva no localStorage
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }
    };

    // Aplica o tema salvo assim que a página carrega
    applyTheme();

    // Adiciona o evento de clique ao botão
    themeToggle.addEventListener('click', toggleTheme);
});
