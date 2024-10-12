document.getElementById('lvlUpButton').addEventListener('click', function() {
    document.getElementById('notification').style.display = 'block';
});

document.getElementById('confirmButton').addEventListener('click', function() {
    // Логика для подтверждения
    document.getElementById('notification').style.display = 'none';
});

document.getElementById('cancelButton').addEventListener('click', function() {
    // Логика для отмены
    document.getElementById('notification').style.display = 'none';
});

function post_data(lvl_explore_entity, id_user, 
    price_lvl_up, quantity_gold){
    if(quantity_gold < price_lvl_up){
        alert("Нехватает средств");
        return;
    }   
    const data = {
        "id_user": id_user,
        "new_lvl_explore_entity": lvl_explore_entity, 
        "price_lvl_up": price_lvl_up, 
        "quantity_gold": quantity_gold, 
    };
    console.log(id_user);
    fetch('/entity_explore/upgrade_entity_explore', {
        method: 'POST',
        headers: { 
            "Accept": "application/json", 
            "Content-Type": "application/json" 
        },
        body: JSON.stringify(data)
    });
}