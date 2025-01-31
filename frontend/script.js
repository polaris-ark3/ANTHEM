document.addEventListener("DOMContentLoaded", async function () {
    let response = await fetch("/api/anthem");
    let data = await response.json();
    document.getElementById("info").innerText = `Название: ${data.game}, Разработчик: ${data.developer}, Год: ${data.year}`;
});

