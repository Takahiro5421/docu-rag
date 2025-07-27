async function send() {
    const input = document.getElementById('input');
    const chat = document.getElementById('chat');

    const resp = await fetch('/query', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({user: 'demo', question: input.value})
    });
    const data = await resp.json();

    const userMsg = document.createElement('div');
    userMsg.textContent = input.value;
    userMsg.className = 'user';
    chat.appendChild(userMsg);

    const botMsg = document.createElement('div');
    botMsg.textContent = data.answer;
    botMsg.className = 'bot';
    chat.appendChild(botMsg);

    if (data.sources) {
        const srcList = document.createElement('ul');
        data.sources.forEach(s => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = s;
            a.textContent = s;
            li.appendChild(a);
            srcList.appendChild(li);
        });
        chat.appendChild(srcList);
    }

    input.value = '';
    chat.scrollTop = chat.scrollHeight;
}
