// function updateCartTotal() {
//     let subtotal = 0;
//     const cartItems = document.querySelectorAll('#cart-items tr');

//     cartItems.forEach(function(item) {
//         const price = parseFloat(item.getAttribute('data-price'));
//         const quantity = parseInt(item.querySelector('.qty-input').value);
//         const itemTotal = price * quantity;

//         item.querySelector('.item-total').innerText = '₹ ' + itemTotal.toFixed(2);
//         subtotal += itemTotal;
//     });

//     document.getElementById('subtotal').innerText = '₹ ' + subtotal.toFixed(2);
//     document.getElementById('total').innerText = '₹ ' + subtotal.toFixed(2);
// }

// // Initialize cart total on page load
// window.onload = updateCartTotal;    


// function updateSubtotal(quantityInput){
//     const row  =  quantityInput.closest('tr');
//     const price = parseFloat(row.querySelector('td:nth-child(3)').textContent);
//     console.log(price)
//     const quantity  = parseInt(quantityInput.value);
//     console.log(quantity)
//     const subtotal = price*quantity;
//     row.querySelector('.subtotal').value = subtotal.toFixed(2);
    
// }

// function updateSubtotal(quantityInput) {
//     const row = quantityInput.closest('tr');
//     const price = parseFloat(row.querySelector('.product-cart-item-text h5').textContent.replace('₹ ', ''));
//     console.log(price)
//     const quantity = parseInt(quantityInput.value);
//     console.log(quantity)
//     const subtotal = price * quantity;
//     console.log(subtotal)

//     row.querySelector('.subtotal').textContent = '₹ ' + subtotal.toFixed(2);

//     updateTotal();
// }

// function updateTotal() {
//     let total = 0;
//     const subtotals = document.querySelectorAll('.subtotal');

//     subtotals.forEach(function(subtotalElement) {
//         const subtotal = parseFloat(subtotalElement.textContent.replace('₹ ', ''));
//         total += subtotal;
//     });

//     document.getElementById('cart-total').textContent = '₹ ' + total.toFixed(2);
// }

// // Initialize total on page load
// window.onload = updateTotal;

// cart page
function updateSubtotal(quantityInput) {
    const row = quantityInput.closest('tr');
    const price = parseFloat(row.querySelector('.product-cart-item-text h5').textContent.replace('₹ ', ''));
    const quantity = parseInt(quantityInput.value);
    const subtotal = price * quantity;

    // Update the subtotal for the current product
    row.querySelector('.subtotal').textContent = '₹ ' + subtotal.toFixed(2);

    // Update the overall cart total
    updateTotal();
}

function updateTotal() {
    let total = 0;
    const subtotals = document.querySelectorAll('.subtotal');

    // Sum up all subtotals to calculate the total cart value
    subtotals.forEach(function(subtotalElement) {
        const subtotal = parseFloat(subtotalElement.textContent.replace('₹ ', ''));
        total += subtotal;
    });

    // Update the cart total on the page
    document.getElementById('cart-total').textContent = '₹ ' + total.toFixed(2);
}

// Initialize total on page load
window.onload = updateTotal;



// checkout 

function updateCheckoutTotal(quantityInput) {
    const row = quantityInput.closest('tr');
    const price = parseFloat(row.querySelector('td:nth-child(2)').textContent.replace('₹ ', ''));
    const quantity = parseInt(quantityInput.value);
    const subtotal = price * quantity;
    row.querySelector('.grandtotal').innerText = `₹ ${subtotal.toFixed(2)}`;

    updateTotalAmount();
}

function updateTotalAmount() {
    let total = 0;
    const subtotals = document.querySelectorAll('.grandtotal');

    subtotals.forEach(subtotal => {
        total += parseFloat(subtotal.textContent.replace('₹ ', ''));
    });

    const deliveryCharges = 50; // Fixed delivery charge
    const grandTotal = total + deliveryCharges;

    document.querySelector('.checkout-total li:nth-child(1) span').innerText = `₹ ${deliveryCharges.toFixed(2)}`;
    document.querySelector('.checkout-total li:nth-child(2) span').innerText = `₹ ${grandTotal.toFixed(2)}`;

    // Store grandTotal in a hidden input
    document.querySelector('input[name="total_amount"]').value = grandTotal.toFixed(2);
}

// Call updateTotalAmount on page load to ensure totals are calculated initially
document.addEventListener('DOMContentLoaded', updateTotalAmount);
    
