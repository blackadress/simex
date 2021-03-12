window.onload = () => {
  let guardar_curso_btn = document.querySelector("#guardar_curso");
  guardar_curso_btn.addEventListener("click", (e) => {
    e.preventDefault();
    postCursoExamen().then((curso) => {
      // agregar curso option al select de cursos
      const option_curso = `<option value="${curso.id}">${curso.siglas} -- ${curso.nombre}</option>`;
      let curso_buscar_select = document.getElementById("curso_buscar");
      curso_buscar_select.innerHTML += option_curso;
    });
  });

  let buscar_pregunta_btn = document.querySelector("#buscar_pregunta");
  buscar_pregunta_btn.addEventListener("click", (e) => {
    e.preventDefault();
    getPreguntasFromSearch().then((preguntas) => {
      renderPreguntasTableAdd(preguntas);
    });
  });

  let table_preguntas_add = document.getElementById('table_preguntas_add')
  table_preguntas_add.addEventListener("click", e => {
    if (e.target.name === "add_pregunta") {
      addPreguntaToTablePreguntasExamen(e)
    }
  })

  let table_preguntas_examen = document.getElementById('table_pregunta_examen')
  table_preguntas_examen.addEventListener('click', e => {
    if (e.target.name == 'del_pregunta') {
      deletePreguntaFromExamen(e)
    }
  })
};

const addPreguntaToTablePreguntasExamen = async (e) => {
  const row = e.target.parentElement.parentElement

  // SERVER
  const re_examen_id = /preguntas\/(\d+)\//
  const examen_id = re_examen_id.exec(document.location.href)[1]
  const re_pregunta_id = /preg_add-(\d+)/
  const pregunta_id = re_pregunta_id.exec(row.id)[1]
  const url = `/examen/api/examen-pregunta/nuevo/`

  let formData = new FormData()
  const csrfmiddlewaretoken = document.querySelector(
    "[name=csrfmiddlewaretoken]"
  ).value;

  formData.append("csrfmiddlewaretoken", csrfmiddlewaretoken);
  formData.append("examen", examen_id);
  formData.append("pregunta", pregunta_id);
  const headers = { "X-CSRFToken": csrfmiddlewaretoken };

  const examen_pregunta_id = await fetch(url, {
    method: 'post',
    headers: headers,
    body: formData,
  })
    .then(res => res.json())
    .then(examen_pregunta => examen_pregunta.id)

  // GUI
  row.parentElement.removeChild(row)
  // cambiar la ultima Cell de row
  row.id = `preg_ex-${examen_pregunta_id}`
  let button_cell = row.cells[row.cells.length - 1]
  button_cell.innerHTML = `<button name="del_pregunta" type="button" class="btn btn-danger">Eliminar pregunta</button>`
  let table_pregunta_examen = document.getElementById('table_pregunta_examen')
  table_pregunta_examen.children[1].appendChild(row)
  
}

const deletePreguntaFromExamen = (e) => {
  const row = e.target.parentElement.parentElement
  const re_pregunta_id = /preg_ex-(\d+)/
  const pregunta_id = re_pregunta_id.exec(row.id)[1]
  const url = `/examen/api/examen-pregunta/${pregunta_id}`

  const csrfmiddlewaretoken = document.querySelector(
    "[name=csrfmiddlewaretoken]"
  ).value;
  const headers = { "X-CSRFToken": csrfmiddlewaretoken };

  fetch(url, {
    method: "delete",
    headers: headers,
  })
    .then(res => res.json())
    .then(res => {
      if (res.exito) {
        row.parentElement.removeChild(row)
      }
    })
}

const postCursoExamen = () => {
  // parsing el id de examen desde la url
  const re = /preguntas\/(\d+)\//;
  const examen_id = re.exec(document.location.href)[1];
  const url = `/examen/api/curso-examen-nuevo/${examen_id}/`;

  // creando el objeto formData
  let formData = new FormData();
  const csrfmiddlewaretoken = document.querySelector(
    "[name=csrfmiddlewaretoken]"
  ).value;
  const curso = document.getElementById("curso").value;
  const cantidad_preguntas = document.getElementById("cantidad_preguntas")
    .value;
  const favor = document.getElementById("favor").value;
  const contra = document.getElementById("contra").value;
  const sin_responder = document.getElementById("sin_responder").value;
  formData.append("csrfmiddlewaretoken", csrfmiddlewaretoken);
  formData.append("curso", curso);
  formData.append("cantidad_preguntas", cantidad_preguntas);
  formData.append("favor", favor);
  formData.append("contra", contra);
  formData.append("sin_responder", sin_responder);

  const headers = { "X-CSRFToken": csrfmiddlewaretoken };

  // fetch con body formData y obteniendo respuesta
  return fetch(url, {
    method: "post",
    headers: headers,
    body: formData,
  }).then((res) => res.json());
};

const getCursosFromUniversidadId = (id) => {
  const url = `/examen/api/curso-buscar-por-universidad/${id}/`;
  return fetch(url).then((res) => res.json());
};

const createOptionsFromCursoData = (selectId, curso) => {
  let select = document.getElementById(selectId);
  select.innerHTML += `
    <option value="${curso.id}">
      ${curso.sigla} -- ${curso.nombre}
    </option>
  `;
};

const cleanOptions = (selectId) => {
  const value_zero = `<option value="0">---------</option>`;
  let select = document.getElementById(selectId);
  select.innerHTML = value_zero;
};

const getPreguntasFromSearch = () => {
  const docente_pk = document.getElementById("docente").value;
  const curso_pk = document.getElementById("curso_buscar").value;
  let nombre_pregunta = document.getElementById("nombre_pregunta").value;
  const re_examen_id = /preguntas\/(\d+)\//
  const examen_id = re_examen_id.exec(document.location.href)[1]
  nombre_pregunta = nombre_pregunta === "" ? "0" : nombre_pregunta;

  const url = `/examen/api/pregunta-buscar/${docente_pk}/${curso_pk}/${nombre_pregunta}/${examen_id}/`;
  return fetch(url).then((res) => res.json());
};

const renderPreguntasTableAdd = (preguntas) => {
  let table = document.getElementById("table_preguntas_add");
  let old_tbody = table.children[1];
  old_tbody.innerHTML = "";

  preguntas.map((pregunta) => {
    let row = old_tbody.insertRow(0);
    const arr = new Array(5).fill(0);
    arr.map(() => row.insertCell(0));
    row.id = `preg_add-${pregunta.id}`
    let cells = row.cells

    cells[0].innerHTML = `${pregunta.nombre}`
    cells[1].innerHTML = `${pregunta.curso}`
    cells[2].innerHTML = `${pregunta.docente}`
    cells[3].innerHTML = `${pregunta.contenido}`
    cells[4].innerHTML = `<button name="add_pregunta" type="button" class="btn btn-info">Agregar pregunta a examen</button>`

  });
};
