window.onload = () => {
  mandar_examen_btn = document.getElementById("mandar_examen");
  mandar_examen_btn.addEventListener("click", (e) => {
    e.preventDefault();
    send_examen()
  });
};

const send_examen = () => {
  const form = document.getElementById('formulario_examen')
  

}

const parse_hora = () => {
  const inicio = document.querySelector('#inicio_examen').innerHTML
  const final = document.querySelector('#entrega_examen').innerHTML

  const fecha_inicio = fecha_texto_a_fecha(inicio)
  const fecha_final = fecha_texto_a_fecha(final)

  const today = new Date()
  // si fecha today es mayor a fecha entrega, no hay reloj
  // si fecha today es menor hay reloj
  // TODO hacer reloj
  if (fecha_final.getTime() < today.getTime()) {
    // no hay reloj
    return
  }

  
}

const fecha_texto_a_fecha = (fecha) => {
  let separado = fecha.split(',')
  let re_day = /(\d*)/
  let re_month = /\: ([A-Za-z]{3})/
  let re_year = /(\d{4})/

  let day = re_day.exec(separado[0])[1]
  let month = re_month.exec(separado[0])[1]
  let year = re_year.exec(separado[1])[1]

  let re_hour = /(\d*)/
  let re_minutes = /:(\d*)/

  let hour = re_hour.exec(separado[2])[1]
  let minutes = re_minutes.exec(separado[2])[1]

  let ampm = separado[2].split(' ').pop()
  if (ampm == "p.m.") {
    hour += 12
  }

  return new Date(`${year} ${month} ${day} ${hour}:${minutes}`)
}
