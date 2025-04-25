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

// Ver métricas del modelo
document.getElementById('verMetricas').addEventListener('click', async function () {
    const respuesta = await fetch('/metricas');

    if (respuesta.ok) {
        const data = await respuesta.json();
        document.getElementById('metricas').textContent = data.reporte;
        document.getElementById('modalMetricas').style.display = "block";
    } else {
        document.getElementById('metricas').textContent = 'Error al obtener las métricas.';
        document.getElementById('modalMetricas').style.display = "block";
    }
});

document.querySelector(".close").addEventListener("click", function () {
    document.getElementById("modalMetricas").style.display = "none";
});

window.addEventListener("click", function (event) {
    const modal = document.getElementById("modalMetricas");
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

