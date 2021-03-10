window.onload = () => {
  mandar_examen_btn = document.getElementById("mandar_examen");
  mandar_examen_btn.addEventListener("click", (e) => {
    e.preventDefault();
    send_examen();
  });

  reloj()
};

const send_examen = () => {
  const form = new FormData(document.getElementById("formulario_examen"))

  const csrf_token = document.getElementsByName('csrfmiddlewaretoken').value
  const url = window.location.href

  const headers = { "X-CSRFToken": csrf_token }
  fetch(url, {
    method: "POST",
    headers: headers,
    body: form,
  })
};

const reloj = () => {
  const inicio = document.querySelector("#inicio_examen").innerHTML;
  const final = document.querySelector("#entrega_examen").innerHTML;

  //const fecha_inicio = fecha_texto_a_fecha(inicio);
  const fecha_final = fecha_texto_a_fecha(final);

  let today = new Date();
  console.log(fecha_final)
  console.log(today)
  // si fecha today es mayor a fecha entrega, no hay reloj
  // si fecha today es menor hay reloj
  if (fecha_final.getTime() < today.getTime()) {
    console.log('sin reloj')
    // no hay reloj
    return;
  } else {
    console.log('con reloj')
    const timer = () => {
      today = new Date()
      const segundos_totales = Math.floor(
        (fecha_final.getTime() - today.getTime()) / 1000
      );

      let minutos = Math.floor(segundos_totales / 60);
      let segundos_restantes = segundos_totales % 60;

      let m = minutos < 10 ? "0" + minutos : minutos;
      let s = segundos_restantes < 10 ? "0" + segundos_restantes : segundos_restantes;

      let reloj = document.querySelector("#reloj");
      reloj.innerHTML = `${m}:${s}`

      setTimeout(timer, 1000)
    };
    timer()
  }
};

const fecha_texto_a_fecha = (fecha) => {
  let separado = fecha.split(",");
  let re_day = /(\d+)/;
  let re_month = /\: ([A-Za-z]{3})/;
  let re_year = /(\d{4})/;

  let day = re_day.exec(separado[0])[1];
  let month = re_month.exec(separado[0])[1];
  let year = re_year.exec(separado[1])[1];

  let re_hour = /(\d+)/;
  let re_minutes = /:(\d+)/;

  let hour = parseInt(re_hour.exec(separado[2])[1]);
  let minutes = re_minutes.exec(separado[2])[1];

  let ampm = separado[2].split(" ").pop();
  if (ampm == "p.m." && hour != 12) {
    hour += 12;
  }

  return new Date(`${year} ${month} ${day} ${hour}:${minutes}`);
};
