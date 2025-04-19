document.getElementById('textForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const texto = document.getElementById('inputText').value;

    const respuesta = await fetch('/procesar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ texto: texto })
    });

    const data = await respuesta.json();
    document.getElementById('resultado').textContent = data.resultado;
});

