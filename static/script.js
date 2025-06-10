async function summarize(){
    const banglaText = document.getElementById("banglaText").value;
    const response = await fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: banglaText })
    });
    const result = await response.json();
    document.getElementById("summary").innerText = result.summary;
    
}