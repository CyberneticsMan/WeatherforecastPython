async function fetchData() {
  const d = new Date();
  let hour = d.getHours();
  let minute = d.getMinutes();
  document.getElementById("hour").innerHTML = hour + ":" + minute;
  const response = await fetch("http://127.0.0.1:5000/forecast/Tehran/temperature");
  const temperature = await response.json();
  document.getElementById("heading").innerHTML = temperature + "° C";


}