async function toggleGPIO() {

    const response = await fetch("/toggle");

    const text = await response.text();

    const led = document.getElementById("led");
    const state = document.getElementById("state");

    state.innerText = text;

    if (text === "ON") {
        led.classList.add("on");
    } else {
        led.classList.remove("on");
    }
}