let addedProducts = {}; // track added products

function addProduct() {
    const name = document.getElementById("product-search").value.trim();
    if (!name) return alert("Enter product name");

    fetch(`/search_product?name=${encodeURIComponent(name)}`)
        .then(res => res.json())
        .then(data => {
            if (!data.product) return alert("Product not found");

            const product = data.product;

            // prevent duplicates
            if (addedProducts[product.id]) {
                return alert("Product already added");
            }

            addedProducts[product.id] = true;

            const tbody = document.querySelector("#billing-table tbody");
            const row = document.createElement("tr");
            row.dataset.id = product.id;

            row.innerHTML = `
                <td>${tbody.children.length + 1}</td>
                <td>${product.product_name}</td>
                <td>₹${product.price}</td>
                <td><input type="number" min="1" value="1" data-price="${product.price}" oninput="updateTotals(this)"></td>
                <td class="item-total">₹${product.price}</td>
                <td><button type="button" onclick="removeRow(this, ${product.id})">Remove</button></td>
            `;

            tbody.appendChild(row);
            updateTotals();
            document.getElementById("product-search").value = "";
        })
        .catch(err => console.error("Error fetching product:", err));
}

function updateTotals() {
    let grandTotal = 0;
    document.querySelectorAll("#billing-table tbody tr").forEach(row => {
        const input = row.querySelector("input");
        const qty = parseInt(input.value) || 0;
        const price = parseFloat(input.dataset.price);
        const total = price * qty;
        row.querySelector(".item-total").innerText = "₹" + total.toFixed(2);
        grandTotal += total;
    });
    document.getElementById("grand-total").innerText = "₹" + grandTotal.toFixed(2);
}

function removeRow(button, productId) {
    button.closest("tr").remove();
    delete addedProducts[productId];
    updateTotals();
}

function saveBill() {
    const product_names = Array.from(document.querySelectorAll('input[name="product_name"]')).map(i => i.value);
    const prices = Array.from(document.querySelectorAll('input[name="price"]')).map(i => i.value);
    const quantities = Array.from(document.querySelectorAll('input[name="quantity"]')).map(i => i.value);
    const totals = Array.from(document.querySelectorAll('input[name="total"]')).map(i => i.value);

    fetch("/save_bill", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"  // Important!
        },
        body: JSON.stringify({
            product_names,
            prices,
            quantities,
            totals
        })
    })
    .then(response => response.text())
    .then(data => alert(data))
    .catch(err => alert("Error: " + err));
}
 function printDiv(bill) {
      // Get the content of the div
      var content = document.getElementById(bill).innerHTML;

      // Open a new window
      var printWindow = window.open('', '', 'height=500,width=800');

      // Write content into it
      printWindow.document.write('<html><head><title>Print</title></head><body>');
      printWindow.document.write(content);
      printWindow.document.write('</body></html>');

      // Print and close
      printWindow.document.close();
      printWindow.print();
    }