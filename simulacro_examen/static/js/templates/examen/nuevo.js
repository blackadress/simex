window.onload = () => {
  let selectUniversidad = document.getElementById('universidad')
  selectUniversidad.addEventListener('change', e => {
    const selectCursoId = 'curso'
    cleanOptions(selectCursoId)
    getCursosFromUniversidadId(e.target.value)
      .then(cursos => cursos.map(curso => {
        createOptionsFromCursoData('curso', curso)
      }))
  })

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
