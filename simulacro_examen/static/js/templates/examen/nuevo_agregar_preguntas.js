window.onload = () => {
  let guardar_curso_btn = document.querySelector('#guardar_curso')
  guardar_curso_btn.addEventListener('click', e => {
    e.preventDefault()
    postCursoExamen()
      .then(curso => {
        // agregar curso option al select de cursos
        const option_curso = `<option value="${curso.id}">${curso.sigla} -- ${curso.nombre}</option>`
        let curso_buscar_select = document.getElementById('curso_buscar')
        curso_buscar_select.innerHTML += option_curso
        
      })
  })

}

const postCursoExamen = () => {
  // parsing el id de examen desde la url
  const re = /preguntas\/(\d+)\//
  const examen_id = re.exec(document.location.href)[1]
  const url = `/examen/api/curso-examen-nuevo/${examen_id}/`

  // creando el objeto formData
  let formData = new FormData()
  const csrfmiddlewaretoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  const curso = document.getElementById('curso').value
  const cantidad_preguntas = document.getElementById('cantidad_preguntas').value
  const favor = document.getElementById('favor').value
  const contra = document.getElementById('contra').value
  const sin_responder = document.getElementById('sin_responder').value
  formData.append("csrfmiddlewaretoken", csrfmiddlewaretoken)
  formData.append("curso", curso)
  formData.append("cantidad_preguntas", cantidad_preguntas)
  formData.append("favor", favor)
  formData.append("contra", contra)
  formData.append("sin_responder", sin_responder)

  const headers = { 'X-CSRFToken': csrfmiddlewaretoken }
  console.log(headers)

  // fetch con body formData y obteniendo respuesta
  return fetch(url, {
    method: "post",
    headers: headers,
    body: formData,
  })
    .then(res => res.json())
}
const getCursosFromUniversidadId = (id) => {
  const url = `/examen/api/curso-buscar-por-universidad/${id}/`
  return fetch(url)
    .then(res => res.json())
}

const createOptionsFromCursoData = (selectId, curso) => {
  let select = document.getElementById(selectId)
  select.innerHTML += `
    <option value="${curso.id}">
      ${curso.sigla} -- ${curso.nombre}
    </option>
  `
}

const cleanOptions = (selectId) => {
  const value_zero = `<option value="0">---------</option>`
  let select = document.getElementById(selectId)
  select.innerHTML = value_zero
}
