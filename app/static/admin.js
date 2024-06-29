document.getElementById('adminForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const data = {
        itemId: document.getElementById('itemSelect').value,
        itemDesc: document.getElementById('itemDesc').value,
        itemPrice: document.getElementById('itemPrice').value,
    };

    fetch('/updatePricesAndDesc', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok){
            return response.json();
        }else{
            throw new Error('Failed to update item');
        }
    })
    .then(data => {
        alert('Item has been updated successfully');
        window.location.href = "/"; // Redirect to home page
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Failed to update item.');
    });
});