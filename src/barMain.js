// Obtén referencias a los elementos HTML
const sidebar = document.getElementById('sidebar');
const logo = document.getElementById('logo-sidebar');

// Agrega un evento de clic al logotipo para alternar la visibilidad del menú
logo.addEventListener('click', () => {
    sidebar.classList.toggle('hidden');
    logo.classList.toggle('visible');
});
