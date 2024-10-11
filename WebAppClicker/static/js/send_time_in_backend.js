
function post_data(time, golds, tokens){
    const data = {
        "time": time, 
        "golds": golds, 
        "tokens": tokens
    };
    fetch('/end_time_raid', {
        method: 'POST',
        headers: { 
            "Accept": "application/json", 
            "Content-Type": "application/json" 
        },
        body: JSON.stringify(data)
    });
}
