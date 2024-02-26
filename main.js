async function fetchData() {
    const response = await fetch("http://127.0.0.1:5000/forecast/Tehran/temperature");
    const temperature = await response.json();
    document.getElementById("temp").innerHTML = temperature;
    
  }