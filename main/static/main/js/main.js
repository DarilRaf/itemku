async function getProducts() {
    return fetch("/get-product").then((res) => res.json())
}
async function refreshProducts() {
    document.getElementById("product_table").innerHTML = ""
    const products = await getProducts()
    let htmlString = ``
    products.forEach((item) => {
        htmlString += `
        <div class="col-sm-4">
            <div class="card">
            <div class="card-body">
                <h5 class="card-title">${item.fields.name}</h5>
                <p class="card-text">Jumlah: ${item.fields.amount}</p>
                <p class="card-text">Deskripsi: ${item.fields.description}</p>
                <p class="card-text">Kategori: ${item.fields.category}</p>
                <p class="card-text">Power: ${item.fields.power}</p>
                <p class="card-text">Harga: ${item.fields.price}</p>
                <p class="card-text">Kadaluarsa: ${item.fields.expiry_date}</p>
                <p class="card-text">Ditambahkan: ${item.fields.date_added}</p>
                <a href="/edit-item/${item.pk}"> 
                <button class="btn btn-primary"> 
                Edit
                </button> 
                </a>
                <a href="/delete/${item.pk}"> 
                <button class="btn btn-primary"> 
                Delete
                </button> 
                </a>
            </div>
            </div>
        </div>` 
    })
    
    document.getElementById("product_table").innerHTML = htmlString
}

refreshProducts()

function addProduct() {
    fetch("/create-ajax", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}

document.getElementById("button_add").onclick = addProduct