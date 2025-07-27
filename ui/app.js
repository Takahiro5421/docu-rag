async function send() {
    const input = document.getElementById('input');
    const resp = await fetch('/query', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({user: 'demo', question: input.value})
    });
    const data = await resp.json();
    document.getElementById('chat').innerText = data.answer;
}
