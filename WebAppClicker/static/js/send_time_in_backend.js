function post_data(time, golds, tokens, id_user){
    document.getElementById("goButton").disabled = true;
    const data = {
        "time": time, 
        "golds": golds, 
        "tokens": tokens,
        "id_user": id_user
    };
    console.log(id_user);
    fetch('/end_time_raid', {
        method: 'POST',
        headers: { 
            "Accept": "application/json", 
            "Content-Type": "application/json" 
        },
        body: JSON.stringify(data)
    });
}