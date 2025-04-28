document.addEventListener('DOMContentLoaded', function() {
    const products = document.querySelectorAll('.product-item');
    products.forEach(product => {
        product.addEventListener('click', function() {
            alert('Вы выбрали: ' + product.querySelector('h2').textContent);
        });
    });
});